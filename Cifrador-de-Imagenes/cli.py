# main.py

import sys
import utils
import salsa20
import secrets
import attack


def generar_clave_nonce():
    key = secrets.randbits(256).to_bytes(32, "little")
    nonce = secrets.randbits(64).to_bytes(8, "little")
    return key, nonce

def cifrar_personalizado():
    img_path = input("Ruta de la imagen a cifrar: ").strip()
    out_path = input("Ruta para guardar la imagen cifrada: ").strip()
    key_path = input("Ruta para guardar la clave y nonce (ej. clave.key): ").strip()

    key, nonce = generar_clave_nonce()
    original_bytes = utils.read_image(img_path)
    encrypted_bytes = salsa20.salsa20_encrypt(key, nonce, original_bytes)
    size = utils.get_image_size(img_path)
    utils.write_image(out_path, encrypted_bytes, size)
    utils.guardar_clave_nonce(key, nonce, key_path)

def descifrar_personalizado():
    img_path = input("Ruta de la imagen cifrada: ").strip()
    key_path = input("Ruta del archivo de clave y nonce: ").strip()
    out_path = input("Ruta para guardar la imagen descifrada: ").strip()

    key, nonce = utils.cargar_clave_nonce(key_path)
    encrypted_bytes = utils.read_image(img_path)
    decrypted_bytes = salsa20.salsa20_encrypt(key, nonce, encrypted_bytes)
    size = utils.get_image_size(img_path)
    utils.write_image(out_path, decrypted_bytes, size)
    print(f"[OK] Imagen descifrada guardada en {out_path}")

def cifrar_y_descifrar(img_path, output_enc_path, output_dec_path):
    key, nonce = generar_clave_nonce()
    print(f"[INFO] Cifrando imagen: {img_path}")

    original_bytes = utils.read_image(img_path)
    encrypted_bytes = salsa20.salsa20_encrypt(key, nonce, original_bytes)
    size = utils.get_image_size(img_path)
    utils.write_image(output_enc_path, encrypted_bytes, size)
    print("[OK] Imagen cifrada correctamente.")

    print(f"[INFO] Descifrando imagen: {output_enc_path}")
    decrypted_bytes = salsa20.salsa20_encrypt(key, nonce, encrypted_bytes)
    utils.write_image(output_dec_path, decrypted_bytes, size)

    print(f"[OK] Imagen descifrada y guardada en {output_dec_path }")


def cifrar_atacar_descifrar(img_path, output_enc_path, attacked_path, attacked_decrypted_path):
    key, nonce = generar_clave_nonce()
    print(f"[INFO] Cifrando {img_path} para ataque...")

    original_bytes = utils.read_image(img_path)
    encrypted_bytes = salsa20.salsa20_encrypt(key, nonce, original_bytes)
    size = utils.get_image_size(img_path)
    utils.write_image(output_enc_path, encrypted_bytes, size)
    print("[OK] Imagen cifrada correctamente.")

    print("[INFO] Atacando imagen cifrada...")
    attack.atacar_archivo_cifrado(output_enc_path, attacked_path)

    try:
        attacked_bytes = utils.read_image(attacked_path)
        decrypted_attacked_bytes = salsa20.salsa20_encrypt(key, nonce, attacked_bytes)
        utils.write_image(attacked_decrypted_path, decrypted_attacked_bytes, size)
        print("[OK] Imagen atacada descifrada (puede estar corrupta visualmente).")
    except Exception as e:
        print(f"[ERROR] Fallo al procesar imagen atacada: {e}", file=sys.stderr)
        sys.exit(1)


def mostrar_menu():
    print("""
==== CIFRADOR DE IMÁGENES CON SALSA20 ====
Seleccione una opción:
1. Cifrar y descifrar imagen de prueba (demo de cifrado y descifrado)
2. Cifrar, atacar y descifrar imagen de prueba (demo de ataque)
3. Cifrar imagen personalizada (guarda clave y nonce)
4. Descifrar imagen personalizada (usando clave y nonce)
5. Generar y guardar clave + nonce manualmente
6. Salir
""")


def main():
    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            cifrar_y_descifrar(
                img_path="imagenes/imagen_original.bmp",
                output_enc_path="imagenes/imagen_cifrada.bmp",
                output_dec_path="imagenes/imagen_descifrada.bmp"
            )

        elif opcion == "2":
            cifrar_atacar_descifrar(
                img_path="imagenes/imagen_original.bmp",
                output_enc_path="imagenes/imagen_cifrada.bmp",
                attacked_path="imagenes/imagen_atacada.bmp",
                attacked_decrypted_path="imagenes/imagen_atacada_descifrada.bmp"
            )

        elif opcion == "3":
            cifrar_personalizado()

        elif opcion == "4":
            descifrar_personalizado()

        elif opcion == "5":
            key, nonce = generar_clave_nonce()
            path = input("Ruta para guardar clave y nonce (ej. clave.key): ").strip()
            utils.guardar_clave_nonce(key, nonce, path)

        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("[ERROR] Opción inválida, intente nuevamente.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[main][ERROR] {e}", file=sys.stderr)
        sys.exit(1)

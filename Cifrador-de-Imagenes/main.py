"""
Main module for the image encryption application.
"""

# Python
import sys

# Project
import utils
import salsa20
import secrets
import attack


def main():
    """
    Main function to run the image encryption application.
    """
    print("Hola, Cifrador de Imágenes Salsa20!")

    # Definir rutas de las imágenes
    img_path = "imagenes/imagen_original.bmp"
    img_cifrada_path = "imagenes/imagen_cifrada.bmp"
    img_descifrada_path = "imagenes/imagen_descifrada.bmp"
    img_atacada_path = "imagenes/imagen_atacada.bmp"
    img_atacada_descifrada_path = "imagenes/imagen_atacada_descifrada.bmp"

    # Generar clave y nonce aleatorios
    key = secrets.randbits(256)
    nonce = secrets.randbits(64)
    key = key.to_bytes(32)
    nonce = nonce.to_bytes(8)

    # Cifrar la imagen original
    imagen_en_bytes = utils.read_image(img_path)
    imagen_cifrada = salsa20.salsa20_encrypt(key, nonce, imagen_en_bytes)

    size = utils.get_image_size(img_path)

    # Guardar la imagen cifrada
    utils.write_image(img_cifrada_path, imagen_cifrada, size)

    # Leer y descifrar la imagen cifrada
    imagen_en_bytes = utils.read_image(img_cifrada_path)
    imagen_descifrada = salsa20.salsa20_encrypt(key, nonce, imagen_en_bytes)

    # Guardar la imagen descifrada
    utils.write_image(img_descifrada_path, imagen_descifrada, size)

    # Atacar la imagen cifrada
    attack.atacar_archivo_cifrado(img_cifrada_path, img_atacada_path)

    # Leer y descifrar la imagen atacada como binario, ya que como producto
    # del ataque, se encuentra corrupta y PIL no puede leerla como imagen.
    try:
        imagen_atacada_en_bytes = utils.read_image(img_atacada_path)
        imagen_descifrada_atacada = salsa20.salsa20_encrypt(key, nonce, imagen_atacada_en_bytes)
        utils.write_image(img_atacada_descifrada_path, imagen_descifrada_atacada, size)
    except Exception as e:
        print(f"[main][ERROR] No se pudo leer o procesar la imagen atacada como binario: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[main][ERROR] {e}", file=sys.stderr)
        sys.exit(1)

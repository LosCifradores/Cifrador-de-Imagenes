"""
Utils functions for image encryption and decryption.
"""
from pathlib import Path
from PIL import Image


def guardar_clave_nonce(key, nonce, path):
    """
    Guarda la clave y el nonce en un archivo binario.
    :param key:
    :param nonce:
    :param path:
    :return:
    """
    with open(path, "wb") as f:
        f.write(key + nonce)
    print(f"[OK] Clave y nonce guardados en {path}")


def cargar_clave_nonce(path):
    """
    Carga la clave y el nonce desde un archivo binario.
    :param path:
    :return:
    """
    with open(path, "rb") as f:
        data = f.read()
        key = data[:32]
        nonce = data[32:40]
    return key, nonce


def get_image_size(img_path):
    """
    Obtiene el tamaño (width, height) de una imagen.
    """
    with Image.open(img_path) as img:
        return img.size

def read_image(path: str) -> bytes:
    """
    Lee una imagen (PNG, JPG, etc.) y devuelve sus bytes crudos.
    """
    img_path = Path(path)
    if not img_path.is_file():
        raise FileNotFoundError(f"No existe el archivo de imagen: {path}")
    with Image.open(img_path) as img:
        img = img.convert("RGB")
        return img.tobytes()


def write_image(path: str, data: bytes, size: tuple[int, int]) -> None:
    """
    Crea y guarda una imagen RGB a partir de un array de bytes y un tamaño.
    """
    img = Image.frombytes("RGB", size, data)
    img.save(path)
    print(f"[utils] Imagen guardada en: {path}")


def read_bytes(path: str) -> bytes:
    """
    Lee un archivo binario completo y devuelve su contenido.
    """
    with open(path, "rb") as f:
        return f.read()


def write_bytes(path: str, data: bytes) -> None:
    """
    Escribe bytes en un archivo binario.
    """
    with open(path, "wb") as f:
        f.write(data)
    print(f"[utils] Bytes escritos en: {path}")


# Function to test the utility functions
def test_utils():
    # 1. Leer una imagen y obtener sus bytes
    img_path = "imagenes/imagen_original.png"
    data = read_image(img_path)
    print(f"[test] Leídos {len(data)} bytes de la imagen '{img_path}'")

    # 2. Guardar esos bytes en un archivo binario
    bin_path = "imagenes/test.bin"
    write_bytes(bin_path, data)
    print(f"[test] Bytes escritos en '{bin_path}'")

    # 3. Leer de nuevo los bytes desde el .bin
    bin_data = read_bytes(bin_path)
    print(f"[test] Leídos {len(bin_data)} bytes de '{bin_path}'")

    # 4. Reconstruir la imagen a partir de los bytes leídos
    #    Necesitamos conocer el tamaño (width, height) de la imagen original:
    size = get_image_size(img_path)

    out_img_path = "imagenes/test.png"
    write_image(out_img_path, bin_data, size)
    print(f"[test] Imagen reconstruida guardada en '{out_img_path}'")

"""
Utils functions for image encryption and decryption.
"""
import sys
from pathlib import Path
from PIL import Image


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
    print(f"[utils] Imagen guardada en: {path}", file=sys.stderr)


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
    print(f"[utils] Bytes escritos en: {path}", file=sys.stderr)


# Function to test the utility functions
def test_utils():
    # 1. Leer una imagen y obtener sus bytes
    img_path = "imagenes/imagen_original.png"
    data = read_image(img_path)
    print(f"[main] Leídos {len(data)} bytes de la imagen '{img_path}'")

    # 2. Guardar esos bytes en un archivo binario
    bin_path = "imagenes/test.bin"
    write_bytes(bin_path, data)
    print(f"[main] Bytes escritos en '{bin_path}'")

    # 3. Leer de nuevo los bytes desde el .bin
    bin_data = read_bytes(bin_path)
    print(f"[main] Leídos {len(bin_data)} bytes de '{bin_path}'")

    # 4. Reconstruir la imagen a partir de los bytes leídos
    #    Necesitamos conocer el tamaño (width, height) de la imagen original:
    with Image.open(img_path) as img:
        size = img.size  # (width, height)
    out_img_path = "imagenes/test.png"
    write_image(out_img_path, bin_data, size)
    print(f"[main] Imagen reconstruida guardada en '{out_img_path}'")

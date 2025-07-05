"""
Main module for the image encryption application.
"""

# Python
import sys

# Project
import utils
import salsa20
import secrets
from PIL import Image


def main():
    """
    Main function to run the image encryption application.
    """
    print("Hola, Cifrador de Imágenes!")
    img_path = "imagenes/imagen_original.png"
    img_cifrada_path = "imagenes/imagen_cifrada.png"
    img_descifrada_path = "imagenes/imagen_descifrada.png"
    key = secrets.randbits(256)
    nonce = secrets.randbits(64)
    key = key.to_bytes(32)
    nonce = nonce.to_bytes(8)

    imagen_en_bytes = utils.read_image(img_path)
    imagen_cifrada = salsa20.salsa20_encrypt(key, nonce, imagen_en_bytes)

    with Image.open(img_path) as img:
        size = img.size

    utils.write_image(img_cifrada_path, imagen_cifrada, size)

    imagen_en_bytes = utils.read_image(img_cifrada_path)
    imagen_descifrada = salsa20.salsa20_encrypt(key, nonce, imagen_en_bytes)
    utils.write_image(img_descifrada_path, imagen_descifrada, size)


    


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[main][ERROR] {e}", file=sys.stderr)
        sys.exit(1)

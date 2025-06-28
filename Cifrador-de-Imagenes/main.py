"""
Main module for the image encryption application.
"""

# Python
import sys

# Project
from utils import test_utils


def main():
    """
    Main function to run the image encryption application.
    """
    print("Hola, Cifrador de Imágenes!")


if __name__ == "__main__":
    try:
        main()
        test_utils()
    except Exception as e:
        print(f"[main][ERROR] {e}", file=sys.stderr)
        sys.exit(1)

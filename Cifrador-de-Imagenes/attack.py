"""
Módulo de ataque para el Sistema de Cifrado de Imágenes
Este script simula un ataque que altera una imagen cifrada con Salsa20
para demostrar el principio de confusión en criptografía.

El principio de confusión establece que la relación entre la clave y el
texto cifrado debe ser lo más compleja posible. Este módulo demuestra que
modificaciones mínimas (0.1% del archivo) en el archivo cifrado
producen cambios catastróficos en la imagen descifrada.

Uso: python attack.py archivo_cifrado.bin archivo_atacado.bin
"""

import sys
import os
import random
from utils import read_bytes, write_bytes

def atacar_archivo_cifrado(ruta_entrada, ruta_salida):
    """
    Ataca un archivo cifrado modificando unos pocos bytes.
    
    La modificación de solo 0.1% (o 5 bytes máximo) demuestra el
    principio de confusión en algoritmos criptográficos robustos como Salsa20.
    Esta prueba muestra el efecto avalancha donde un cambio mínimo en la
    entrada produce un cambio máximo en la salida.
    
    Parámetros:
        ruta_entrada (str): Ruta al archivo cifrado
        ruta_salida (str): Ruta para guardar el archivo atacado
    """
    try:
        # Cargar el archivo cifrado usando utils.py
        print(f"Cargando archivo cifrado desde: {ruta_entrada}")
        datos_cifrados = read_bytes(ruta_entrada)
        
        # Convertir a bytearray para poder modificarlo
        datos_modificados = bytearray(datos_cifrados)
        total_bytes = len(datos_modificados)
        
        # Determinar cuántos bytes modificar (0.1% o 5 bytes máximo)
        # Justificación: Esta pequeña alteración es suficiente para demostrar
        # la robustez del cifrado frente a ataques de modificación
        bytes_a_modificar = min(5, max(1, int(total_bytes * 0.001)))  # 0.1% o 5 bytes máximo
        
        print(f"Archivo cifrado: {total_bytes} bytes totales")
        print(f"Se modificarán {bytes_a_modificar} bytes")
        
        # Modificar bytes aleatorios (cambio de un solo bit por byte)
        for _ in range(bytes_a_modificar):
            posicion = random.randint(0, total_bytes - 1)
            posicion_bit = random.randint(0, 7)
            datos_modificados[posicion] ^= (1 << posicion_bit)  # Invertir un bit
            print(f"Byte modificado en posición {posicion}, bit {posicion_bit}")
            
        # Guardar el archivo atacado usando utils.py
        print(f"Guardando archivo atacado en: {ruta_salida}")
        write_bytes(ruta_salida, datos_modificados)
            
        print(f"¡Ataque completado con éxito!")
        return True
        
    except Exception as e:
        print(f"Error durante el ataque: {e}")
        return False


def main():
    # Verificar argumentos
    if len(sys.argv) != 3:
        print("Uso: python attack.py archivo_cifrado.bin archivo_atacado.bin")
        return 1
    
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    
    # Validar archivo de entrada
    if not os.path.exists(archivo_entrada):
        print(f"Error: El archivo '{archivo_entrada}' no existe.")
        return 1
    
    # Realizar el ataque
    exito = atacar_archivo_cifrado(archivo_entrada, archivo_salida)
    
    return 0 if exito else 1

if __name__ == "__main__":
    sys.exit(main())
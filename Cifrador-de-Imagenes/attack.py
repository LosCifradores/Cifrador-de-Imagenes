"""
Módulo de ataque para el Sistema de Cifrado de Imágenes
Este script simula un ataque que altera una imagen cifrada con Salsa20
para demostrar la vulnerabilidad de los cifrados de flujo sin protección
de integridad.

Salsa20 es un cifrador de flujo que genera un keystream que se combina con
el texto plano mediante XOR. Esta implementación demuestra cómo un atacante
puede modificar bits específicos en un archivo cifrado y causar modificaciones
predecibles en la imagen descifrada, sin conocer la clave.

Uso: python attack.py archivo_cifrado.bin archivo_atacado.bin
"""

import sys
import os
import random
from utils import read_bytes, write_bytes

def atacar_archivo_cifrado(ruta_entrada, ruta_salida):
    """
    Ataca un archivo cifrado modificando un porcentaje de sus bytes.
    
    Este ataque aprovecha una característica de los cifradores de flujo como Salsa20:
    si se modifica un bit en el archivo cifrado, exactamente el mismo bit se modificará
    en la imagen descifrada. Esto permite a un atacante alterar la imagen final 
    de manera predecible sin conocer la clave de cifrado.
    
    Parámetros:
        ruta_entrada (str): Ruta al archivo cifrado
        ruta_salida (str): Ruta para guardar el archivo atacado
    """
    try:
        # Cargar el archivo cifrado usando utils.py
        print(f"[attack] Cargando archivo cifrado desde: {ruta_entrada}")
        datos_cifrados = read_bytes(ruta_entrada)
        
        # Convertir a bytearray para poder modificarlo
        datos_modificados = bytearray(datos_cifrados)
        total_bytes = len(datos_modificados)
        
        # Modificar un 50% de los bytes del archivo cifrado
        # Este alto porcentaje mostrará claramente el efecto en la imagen descifrada
        porcentaje = 50.0
        bytes_a_modificar = max(1, int(total_bytes * porcentaje / 100))
        
        # Evitar modificar el encabezado BMP (primeros 54 bytes)
        # para preservar la estructura del archivo
        offset_header = 54
        
        # Modificar bytes aleatorios (cambio de un solo bit por byte)
        modificados = 0
        for _ in range(bytes_a_modificar):
            posicion = random.randint(offset_header, total_bytes - 1)
            posicion_bit = random.randint(0, 7)
            datos_modificados[posicion] ^= (1 << posicion_bit)  # Invertir un bit
            modificados += 1
            
        # Guardar el archivo atacado usando utils.py
        print(f"[attack] Se modificaron {modificados} bytes ({porcentaje}%)")
        print(f"[attack] Guardando archivo atacado en: {ruta_salida}")
        write_bytes(ruta_salida, datos_modificados)
            
        print(f"[attack] ¡Ataque completado con éxito!")
        return True
        
    except Exception as e:
        print(f"[attack] Error durante el ataque: {e}")
        return False

def attack():
    # Verificar argumentos
    if len(sys.argv) != 3:
        print("[attack]  Uso: python attack.py archivo_cifrado.bin archivo_atacado.bin")
        return 1
    
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    
    # Validar archivo de entrada
    if not os.path.exists(archivo_entrada):
        print(f"[attack] Error: El archivo '{archivo_entrada}' no existe.")
        return 1
    
    # Realizar el ataque
    exito = atacar_archivo_cifrado(archivo_entrada, archivo_salida)
    
    return 0 if exito else 1

if __name__ == "__main__":
    sys.exit(attack())
"""
Primitive Salsa20 cipher implementation.
This module provides implementation of the Salsa20 stream cipher,
which is a cryptographic algorithm designed for high performance and security.
"""
import struct


def rotate(v, c):
    """
    Rotación de 32 bits hacia la izquierda
    """
    return ((v << c) & 0xffffffff) | (v >> (32 - c))


def add(x, y):
    """
    Suma módulo 2^32
    """
    return (x + y) & 0xffffffff


def quarterround(y0, y1, y2, y3):
    """
    Función Quarterround de Salsa20
    """
    y1 ^= rotate(add(y0, y3), 7)
    y2 ^= rotate(add(y1, y0), 9)
    y3 ^= rotate(add(y2, y1), 13)
    y0 ^= rotate(add(y3, y2), 18)
    return y0, y1, y2, y3


def rowround(y):
    """
    Aplica quarterround por filas
    """
    z = y[:]
    z[0], z[1], z[2], z[3] = quarterround(z[0], z[1], z[2], z[3])
    z[5], z[6], z[7], z[4] = quarterround(z[5], z[6], z[7], z[4])
    z[10], z[11], z[8], z[9] = quarterround(z[10], z[11], z[8], z[9])
    z[15], z[12], z[13], z[14] = quarterround(z[15], z[12], z[13], z[14])
    return z


def columnround(x):
    """
    Aplica quarterround por columnas
    """
    z = x[:]
    z[0], z[4], z[8], z[12] = quarterround(z[0], z[4], z[8], z[12])
    z[5], z[9], z[13], z[1] = quarterround(z[5], z[9], z[13], z[1])
    z[10], z[14], z[2], z[6] = quarterround(z[10], z[14], z[2], z[6])
    z[15], z[3], z[7], z[11] = quarterround(z[15], z[3], z[7], z[11])
    return z


def doubleround(x):
    """
    Aplica una columnround seguida de una rowround
    """
    return rowround(columnround(x))


def little_endian_words(b):
    """
    Convierte 64 bytes en 16 palabras de 32 bits (little-endian)
    """
    return list(struct.unpack('<16I', b))


def words_to_bytes(words):
    """
    Convierte 16 palabras de 32 bits a 64 bytes (little-endian)
    """
    return struct.pack('<16I', *words)


def salsa20_hash(input_):
    """
    Aplica 20 rondas (10 doublerounds) al estado
    """
    x = input_[:]
    for _ in range(10):
        x = doubleround(x)
    return [(x[i] + input_[i]) & 0xffffffff for i in range(16)]


def create_state(key, nonce, counter):
    """
    Construye el estado de 64 bytes con key, nonce y contador (Salsa20 estándar)
    """
    assert len(key) == 32
    assert len(nonce) == 8
    assert len(counter) == 8

    constants = b"expand 32-byte k"
    # Formato estándar: c0 k0 c1 n c2 k1 c3
    # c0=0:4, c1=4:8, c2=8:12, c3=12:16
    state_bytes = (
            constants[0:4] + key[0:16] + constants[4:8] + counter + nonce +
            constants[8:12] + key[16:32] + constants[12:16]
    )
    assert len(state_bytes) == 64, \
        f"El estado debe tener 64 bytes, tiene {len(state_bytes)}"
    return little_endian_words(state_bytes)


def salsa20_encrypt(key, nonce, plaintext):
    """
    Cifra o descifra datos con Salsa20 (XOR con keystream)
    """
    assert len(key) == 32
    assert len(nonce) == 8

    ciphertext = bytearray()
    total_len = len(plaintext)
    block_count = (total_len + 63) // 64

    for i in range(block_count):
        counter = struct.pack('<Q', i)  # contador de 8 bytes
        state = create_state(key, nonce, counter)
        keystream = words_to_bytes(salsa20_hash(state))

        block = plaintext[i * 64:(i + 1) * 64]
        # Solo usa la parte del keystream necesaria para el bloque
        encrypted = bytes(
            [b ^ k for b, k in zip(block, keystream[:len(block)])])
        ciphertext.extend(encrypted)

    return bytes(ciphertext)


def test_salsa20():
    """
    Función de prueba para verificar el cifrado Salsa20
    """
    key = b"0123456789ABCDEF0123456789ABCDEF"  # 32 bytes
    nonce = b"12345678"  # 8 bytes
    plaintext = b"Hello, Salsa20! This is a test message." * 2  # Datos de prueba

    ciphertext = salsa20_encrypt(key, nonce, plaintext)
    decrypted = salsa20_encrypt(key, nonce, ciphertext)

    assert decrypted == plaintext, \
        "El descifrado no coincide con el texto original"
    print("Prueba Salsa20 exitosa: cifrado y descifrado coinciden.")

# 🛡️ Cifrador de Imágenes con Salsa20

## **Universidad Nacional de La Matanza**  
**Asignatura:** Matemática Aplicada  
**Trabajo Práctico Final de Criptografía**

---
### 👨‍👩‍👦‍👦 Integrantes

- **Federico Sabadini**
- **Juan Diego Moscoso Rendon**
- **Franco Damian Sabes**
- **Facundo Acevedo**
- **Ramiro Medina**

---
## 📜 Descripción del Trabajo Práctico
### 🧠 Objetivo

El propósito de este trabajo práctico es el desarrollo de un sistema informático capaz de **cifrar y descifrar archivos de imagen** utilizando la primitiva criptográfica **Salsa20**.

El sistema deberá permitir:
- Cifrar una imagen con una clave secreta.
- Recuperar (descifrar) la imagen original desde su versión cifrada.
- Simular un ataque de modificación sobre la imagen cifrada y analizar su impacto al intentar descifrar.

El trabajo será acompañado por una **exposición oral** y opcionalmente por una presentación visual, en la cual se demostrará el funcionamiento del sistema desarrollado.

---

### 🔐 Primitiva Criptográfica Utilizada

**Salsa20** es un algoritmo de cifrado simétrico en flujo diseñado por Daniel J. Bernstein. Se caracteriza por:
- Alta velocidad de procesamiento.
- Seguridad probada frente a ataques conocidos.
- Amplio uso en bibliotecas modernas como `PyCryptodome`.

---

### 🧰 Herramientas Utilizadas

- **Lenguaje de programación:** Python 3.x
- **Librerías principales:**
    - `PyCryptodome` para el cifrado Salsa20.
    - `Pillow` para la manipulación de imágenes.
    - `argparse` o interfaz gráfica (según la implementación) para la ejecución del script.

---

### 📁 Estructura del Proyecto (TENTATIVO)
```
Cifrador-de-Imagenes/
├── src/ # Código fuente
│ ├── encryptor.py
│ └── utils.py # Funciones auxiliares
├── assets/
│ ├── original.png
│ ├── encrypted.bin
│ ├── decrypted.png
│ └── tampered.bin # Versión modificada por un atacante
├── demo/
│ └── demo.mp4
│ └── presentation.pptx
├── README.md
└── informe_final.pdf
```

---

## 📦 Entregables

- ✅ Código fuente del programa (carpeta `src/`)
- ✅ Archivo de imagen original, cifrado, descifrado y alterado (carpeta `assets/`)
- ✅ Video o presentación mostrando la ejecución (carpeta `demo/`)
- ✅ Informe final con:
    - Descripción del sistema
    - Explicación de la primitiva Salsa20
    - Análisis de seguridad del sistema

---

## 🎯 Ejecución del Proyecto

### Requisitos

### Uso

---

## 🧪 Simulación de Ataque

---

## 📄 Licencia

Proyecto académico sin fines comerciales. Licencia MIT.

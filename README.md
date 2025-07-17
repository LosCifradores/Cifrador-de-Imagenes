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

### 📁 Estructura del Proyecto
```
├── Cifrador-de-Imagenes-Salsa20
│ ├── Cifrador-de-Imagenes
│ │ ├── __init__.py
│ │ ├── attack.py
│ │ ├── main.py
│ │ ├── salsa20.py
│ │ ├── utils.py
│ │ ├── imagenes
│ │ │ ├── imagen_original.png
│ │ │ ├── imagen_cifrada.png
│ │ │ ├── imagen_descifrada.png
│ │ │ └── imagen_alterada.png
│ ├── CONTRIBUTING.md
│ ├── demo
│ │ └── demo_salsa20.pptx
│ ├── README.md
│ ├── requirements.txt
│ ├── TASKS.md
│ └── venv

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
- Python 3.x instalado.
- Virtual environment (opcional pero recomendado).
- Dependencias detalladas en `requirements.txt` instaladas

### 🚀 Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/LosCifradores/Cifrador-de-Imagenes.git
   cd Cifrador-de-Imagenes
   ```

2. **Crear y activar un entorno virtual**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .venv\Scripts\activate      # Windows
   ```
3. **Instalar dependencias**
   ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

### Uso

Para ejecutar el programa, inicia el archivo `cli.py`. Se mostrará un menú interactivo en consola con las siguientes opciones:

1. **Cifrar y descifrar imagen de prueba:**  
   Cifra y luego descifra una imagen de ejemplo ubicada en la carpeta `imagenes/`.

2. **Cifrar, atacar y descifrar imagen de prueba:**  
   Cifra una imagen de ejemplo, simula un ataque modificando el archivo cifrado, y luego intenta descifrar la versión atacada.

3. **Cifrar imagen personalizada:**  
   Permite seleccionar una imagen, cifrarla y guardar la clave y el nonce generados en un archivo.

4. **Descifrar imagen personalizada:**  
   Descifra una imagen previamente cifrada utilizando la clave y el nonce guardados.

5. **Generar y guardar clave + nonce:**  
   Genera una clave y un nonce nuevos y los guarda en un archivo.

6. **Salir:**  
   Finaliza el programa.

> Para iniciar el menú, ejecuta en la terminal:
> ```bash
> python3 Cifrador-de-Imagenes/cli.py
> ```

Sigue las instrucciones en pantalla para seleccionar la opción deseada e ingresar las rutas de los archivos correspondientes.

---

## 🧪 Simulación de Ataque
Salsa20 solo asegura la confidencialidad de los datos, pero no la autenticidad ni la integridad. Para mostrar esta vulnerabilidad de los cifradores de flujo como Salsa20, realizamos la siguiente simulación:

1. Ciframos una imagen usando Salsa20.
2. Modificamos algunos bytes del archivo cifrado de forma aleatoria.
3. Desciframos el archivo modificado con la clave y nounce originales.

El resultado es que algunos píxeles de la imagen cambiaron de color, pero el resto de la imagen se muestra perfectamente. Esto ocurre porque los mismos bytes que fueron modificados en la imagen cifrada también se ven modificados después del descifrado. Como Salsa20 procesa cada bit de manera independiente, no hay efecto cascada: un cambio en un bit solo afecta ese mismo bit al descifrar.

Para proteger la integridad y autenticidad de los datos, es necesario agregar un mecanismo de verificación, como un MAC, o utilizar cifrados autenticados como ChaCha20-Poly1305.

---

## 📄 Licencia

Proyecto académico sin fines comerciales. Licencia MIT.

# 🚀 CreacionAPI - Ejemplo básico con FastAPI

Este proyecto es una API básica creada con **FastAPI** en Python.  
Incluye tres endpoints de ejemplo:  

- `/` → Mensaje de bienvenida.
- `/hello` → Devuelve un saludo.
- `/status` → Indica que la API funciona correctamente.

---

## 📦 Requisitos

- Python 3.9 o superior
- pip (instalador de paquetes de Python)

---

## 🛠 Instalación

1. **Clonar el repositorio**
   ```bash
   https://github.com/JoseAntonio1306/CreacionAPI
   cd CreacionAPI
   ```
2. **Crear un entorno virtual**
   ```bash
   python -m venv .venv
    ```
3. **Activar el entorno virtual**
    #### Windows (PowerShell)
    ```powershell   
   .\.venv\Scripts\Activate.ps1
    ```
    #### Linux/Mac
    ```bash  
   source .venv/bin/activate

4. **Instalar dependencias**
    ```bash
   pip install -r requirements.txt
    ```
## ▶ Ejecución
#### Iniciar el servidor con:
```bash
    uvicorn main:app --reload
```

## 📂 Estructura del proyecto

```aiignore
CreacionAPI/
│
├── main.py            # Código principal de la API
├── requirements.txt   # Dependencias del proyecto
└── .gitignore         # Archivos/carpetas a ignorar por Git

```

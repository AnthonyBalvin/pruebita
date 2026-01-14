# Usamos una imagen base ligera de Python
FROM python:3.11-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos las dependencias y las instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código fuente
COPY src/ ./src/

# Comando por defecto al ejecutar el contenedor (solo para probar que funciona)
CMD ["python", "src/main.py"]
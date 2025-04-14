# Usamos una imagen de Python
FROM python:3.13.3-alpine

# Establececemos la carpeta de trabajo
WORKDIR /app

# Copiamos los archivos a la carpeta de trabajo
COPY . .

# Instalamos las dependencias necesarias
RUN pip install -r requirements.txt

# Establecemos el comando que se ejecutará al iniciar el contenedor
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]

# Usamos una imagen oficial de Python como base
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requerimientos
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el archivo Python desde el directorio anterior
COPY predictor.py .

# Exponer el puerto en el que se ejecutará Streamlit
EXPOSE 8501

# Comando para ejecutar la aplicación de Streamlit
CMD ["streamlit", "run", "predictor.py", "--server.port=8501", "--server.enableCORS=false"]

# Imagen base
FROM python:3.11

# Creamos una carpeta
RUN mkdir /src

# La establecemos como directorio de trabajo
WORKDIR /src

# Añadimos el contenido de src a src
ADD ./app /src
ADD ./requirements.txt /src

# Instalamos las dependencias de python
RUN pip install -r requirements.txt

# Model
RUN mkdir /src/model
ADD ./model /src/model

# Ejecutamos el comando para lanzar la API
#CMD ["streamlit", "run", "app.py"]
CMD ["fastapi", "run", "api.py"]

# Exponemos el puerto del backend
EXPOSE 8000
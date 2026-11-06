FROM python:3.11-slim

WORKDIR /capa_de_procesamiento

COPY /requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY data_processing.py ./

CMD ["python","data_processing.py"]
#FROM python:3.10-slim
#
#WORKDIR /app
#
#COPY . .
#
#RUN pip install --upgrade pip && \
#    pip install -r requirements.txt && \
#    pip install pyarrow
#
#CMD ["bash", "-c", "python etl/generate_batches.py && python etl/save_parquet.py"]

FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install pyarrow pytest

CMD bash -c "python etl/generate_batches.py && \
             python etl/save_parquet.py && \
             pytest tests/"

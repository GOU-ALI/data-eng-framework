FROM bitnami/spark:latest

USER root

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip install pyspark boto3

USER 1001

FROM ubuntu:latest

COPY . /app

WORKDIR /app

RUN apt-get update \
    && apt-get install -y python3 \
    && apt-get install -y python3-pip \
    && pip install -r /app/requirements.txt

EXPOSE 5123

CMD ["bash", "start.sh"]
# ADOFAI_DELETE_TOOL_WEB-DOCKER

[简体中文](./README.md) | English

A web tool for deleting ADOFAI effects, built with the Flask framework.

All debugging of this program is based on Ubuntu.

## Deployment

### Prerequisites
- A Linux server
---

### Installation (Direct installation)

```shell
apt update

apt install -y python3

apt install -y python3-pip

pip3 install -r requirements.txt

./start.sh
```

### Docker installation
```shell
docker run leonleeli/adofaitool:v1 -p YourPort:5123
```

## Build Docker image
```shell
./build.sh
```
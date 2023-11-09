# ADOFAI_DELETE_TOOL_WEB-DOCKER

简体中文 | [English](./README_en.md)

一个删除 ADOFAI 特效的web小工具,使用flask框架

此程序一切调试皆基于Ubuntu

## 部署

### 前提条件
- 一台linux服务器
---

### 安装(直接安装)

```shell
apt update

apt install -y python3

apt install -y python3-pip

pip3 install -r requirements.txt

./start.sh
```

### docker方式安装
```shell
docker run leonleeli/adofaitool:v1 -p YourPort:5123
```


## 构建dockers镜像
```shell
./build.sh
```
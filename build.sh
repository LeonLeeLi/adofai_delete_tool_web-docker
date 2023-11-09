SHELL_FOLDER=$(cd "$(dirname "$0")";pwd)

docker build -f $SHELL_FOLDER/Dockerfile -t adofaitool:v1 .
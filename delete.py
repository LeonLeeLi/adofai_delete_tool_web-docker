import subprocess
import time
import shutil

# 启动 app.py 并获取其 pid
process = subprocess.Popen(['python', 'app.py'])

while True:
    # 在指定时间关闭 app.py
    current_time = time.strftime("%H:%M", time.localtime())
    if current_time == "00:00":
        # 检查子进程是否正在运行
        if process.poll() is None:
            process.terminate()
            process.wait()

        # 删除 "upload" 和 "modify" 文件夹
        shutil.rmtree("upload")
        shutil.rmtree("modify")

    # 在指定时间重新启动 app.py
    current_time = time.strftime("%H:%M", time.localtime())
    if current_time == "00:10":
        process = subprocess.Popen(['python', 'app.py'])

    time.sleep(25)

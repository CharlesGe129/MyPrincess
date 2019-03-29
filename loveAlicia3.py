import time
import os


start = 1553705927
end = 1558371527
while True:
    time.sleep(1)
    cur = int(time.time())
    os.system("clear")
    print(f"宝贝回来还有{end-cur}秒，进度条{round((cur-start)/(end-start), 7)}%")

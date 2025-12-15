import os
import time

while True:
    os.system("git pull origin main")
    os.system("upload.bat")
    time.sleep(60)

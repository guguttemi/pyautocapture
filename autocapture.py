import os
import time
from datetime import datetime
import winsound as sd
import sys
import subprocess

# 외부 모듈 자동 설치
try:
    import schedule
    import pyautogui
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'schedule'])
    time.sleep(1)
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pyautogui'])
    time.sleep(1)
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pillow'])
    import schedule
    import pyautogui

today_folder_name = '{:%y%m%d}'.format(datetime.now())

os.mkdir(today_folder_name)

def job():
    now = datetime.now()
    sd.Beep(2000, 1000)
    time.sleep(5)
    print("[작업 수행 시각] {:%H:%M:%S}".format(now)) # 커맨드 창에 동작 수행시간 출력 후
    captured_image = pyautogui.screenshot()

    if now.hour < 13:
        file_name = '{:%y%m%d}-김연지-오전-{:%H_%M}'.format(now,now)+'.png'
    else:
        file_name = '{:%y%m%d}-김연지-오후-{:%H_%M}'.format(now,now)+'.png'
        
    suffix_path = f'\{today_folder_name}\{file_name}'
    captured_image.save(os.getcwd() + suffix_path)

# 9시
schedule.every().day.at('09:05').do(job)
schedule.every().day.at('09:50').do(job)

# 10시 ~ 
hour = 10
minutes = '05'
for _ in range(1, 8):
    print(f'{hour} hour scheduling..')
    schedule.every().day.at(f'{hour}:{minutes}').do(job)
    schedule.every().day.at(f'{hour}:{minutes[::-1]}').do(job)
    
    # 13시 제외
    if(hour == 12):
        hour += 1
    hour += 1 

print(schedule.jobs) # list type, 예약된 job 확인
while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except Exception as e:
        print("작업 강제 종료", e)
        sd.Beep(5000, 2000)
        schedule.clear()         
        break            

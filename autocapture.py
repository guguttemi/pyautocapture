import os
import schedule
import time
from datetime import datetime
import pyautogui
import winsound as sd

def job():
    now = datetime.now()
    sd.Beep(2000, 1000)
    time.sleep(5)
    print("[작업 수행 시각] {:%H:%M:%S}".format(now)) # 커맨드 창에 동작 수행시간 출력 후
    im = pyautogui.screenshot()
    today_folder_name = '{:%y%m%d}'.format(now)

    if now.hour < 13:
        file_name = '{:%y%m%d}-김연지-오전-{:%H_%M}'.format(now,now)+'.png'
    else:
        file_name = '{:%y%m%d}-김연지-오후-{:%H_%M}'.format(now,now)+'.png'
        
    os.mkdir(today_folder_name)
    suffix_path = f'\{today_folder_name}\{file_name}'
    im.save(os.getcwd() + suffix_path)


# 9시
for _ in range(1):
    schedule.every().day.at('09:05').do(job)
    schedule.every().day.at('09:50').do(job)

# 10시 ~ 
hour = 10
minutes = '50'
for _ in range(1, 8):
    print(f'현재 {hour}시 looping..')
    schedule.every().day.at(f'{hour}:{minutes}').do(job)
    minutes = minutes[::-1]
    schedule.every().day.at(f'{hour}:{minutes}').do(job)
    minutes = minutes[::-1]
    if(hour == 12):
        hour += 1
    hour += 1 

# schedule.every().day.at("09:50").do(job)

# schedule.every().day.at("10:05").do(job)
# schedule.every().day.at("10:50").do(job)

# schedule.every().day.at("11:05").do(job)
# schedule.every().day.at("11:50").do(job)

# schedule.every().day.at("12:05").do(job)
# schedule.every().day.at("12:50").do(job)

# schedule.every().day.at("14:05").do(job)
# schedule.every().day.at("14:50").do(job)

# schedule.every().day.at("15:05").do(job)
# schedule.every().day.at("15:50").do(job)

# schedule.every().day.at("16:05").do(job)
# schedule.every().day.at("16:50").do(job)

# schedule.every().day.at("17:05").do(job)
# schedule.every().day.at("17:50").do(job)

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except Exception as e:
        print("작업 강제 종료", e)
        sd.Beep(5000, 2000)
        schedule.clear()         
        break            

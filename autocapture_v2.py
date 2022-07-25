
import schedule
import os
from pathlib import Path
import time
from datetime import datetime
import pyautogui
import winsound as sd

# pip install pyautogui
# pip install pillow
# pip install schedule

now = datetime.now()

# 지정한 캡처 폴더를 생성하지 않았으면 생성
capture_folder = Path("./"+"{:%y%m%d}".format(now))


if not capture_folder.exists():
    capture_folder.mkdir(parents=True, exist_ok=True)

def job():
    now = datetime.now()   
    file_name1 = "{:%y%m%d}-김연지-오전-{:%H_%M}".format(now,now)+".png" # 선생님 이름으로 바꿔주세요
    file_name2 = "{:%y%m%d}-김연지-오후-{:%H_%M}".format(now,now)+".png" # 선생님 이름으로 바꿔주세요
    
    sd.Beep(2000, 1000) 
    time.sleep(10)
    print("[작업 수행 시각] {:%H:%M:%S}".format(now)) # 커맨드 창에 동작 수행시간 출력 후
    if now.hour < 13:
        pyautogui.screenshot(capture_folder/file_name1) 
                                                    # 전체 화면이 캡처됩니다. 
    else:
        pyautogui.screenshot(capture_folder/file_name2) 



schedule.every().day.at("09:05").do(job)
schedule.every().day.at("09:50").do(job)

schedule.every().day.at("10:05").do(job)
schedule.every().day.at("10:50").do(job)

schedule.every().day.at("11:05").do(job)
schedule.every().day.at("11:50").do(job)

schedule.every().day.at("12:05").do(job)
schedule.every().day.at("12:50").do(job)

schedule.every().day.at("14:05").do(job)
schedule.every().day.at("14:50").do(job)

schedule.every().day.at("15:05").do(job)
schedule.every().day.at("15:50").do(job)

schedule.every().day.at("16:05").do(job)
schedule.every().day.at("16:50").do(job)

schedule.every().day.at("17:05").do(job)
schedule.every().day.at("17:50").do(job)


while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except Exception as e:
        sd.Beep(5000, 3000) 
        print("작업 강제 종료", e)
        schedule.clear()         
        break            

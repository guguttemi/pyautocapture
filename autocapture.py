import time
from datetime import datetime
from pathlib import Path
import winsound as sd
import sys
import subprocess
from pprint import pprint

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

# 지정한 캡처 폴더를 생성하지 않았으면 생성
capture_folder = Path('./'+'{:%y%m%d}'.format(datetime.now()))

if not capture_folder.exists():
    capture_folder.mkdir(parents=True, exist_ok=True)

def job():
    now = datetime.now()
    sd.Beep(2000, 1000)
    time.sleep(5)
    print('[작업 수행 시각] {:%H:%M:%S}'.format(now)) # 커맨드 창에 작업 수행 시각 출력 후 전체 화면이 캡처됩니다. 
    if now.hour < 13:
        file_name_am = '{:%y%m%d}-내이름-오전-{:%H_%M}'.format(now,now)+'.png'
        pyautogui.screenshot(capture_folder/file_name_am) 
    else:
        file_name_pm = '{:%y%m%d}-내이름-오후-{:%H_%M}'.format(now,now)+'.png'
        pyautogui.screenshot(capture_folder/file_name_pm) 

# 9시 scheduling
schedule.every().day.at('09:05').do(job)
schedule.every().day.at('09:50').do(job)

# 10시 scheduling
hour = 10
minutes = '05'
for _ in range(1, 8):
    schedule.every().day.at(f'{hour}:{minutes}').do(job)
    schedule.every().day.at(f'{hour}:{minutes[::-1]}').do(job)
    # 13시 제외
    if(hour == 12):
        hour += 1
    hour += 1 

# 개별적으로 시간을 세팅하고 싶을 경우, ..day.at('원하는 시간')
# schedule.every().day.at("09:05").do(job)
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

pprint(schedule.jobs) # 예약된 job 확인
while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except Exception as e:
        print('작업 강제 종료', e)
        sd.Beep(5000, 2000)
        schedule.clear()         
        break            

# pyautocapture

## 0. Intro
#### 프로그램 기능
특정 시간에 자동으로 화면을 캡쳐하여 파일로 저장해주는 Python 기반 프로그램

## 1. Installation
설치 및 실행 방법은 크게 3단계로 구성됩니다.<br>

1-1. 설치<br>
1-2. 이름 설정<br>
1-3. 실행<br>

### 1-1. 프로그램 설치
**프로그램 설치는 <span style='background-color:#ffdce0'>바탕화면</span>을 root 경로로 지정해주시기 바랍니다.<br>(설정을 통해 변경 가능)**

#### git clone을 통한 설치 
```
$ git clone https://github.com/guguttemi/pyautocapture.git
```

#### Download를 통한 설치
1. [Github 메인 페이지](https://github.com/guguttemi)의 <span style='background-color:#dcffe4'>**Code&darr;**</span> 선택
2. Download ZIP click
3. 바탕화면에 폴더 압축 해제

### 1-2. Configuration
1. code editor를 통해 autocapture.py 열기
2. def job() '내이름'을 자신의 이름으로 변경 후 저장
```
def job():
...
if now.hour < 13:
        file_name_am = '{:%y%m%d}-내이름-오전-{:%H_%M}'.format(now,now)+'.png'
        pyautogui.screenshot(capture_folder/file_name_am) 
    else:
        file_name_pm = '{:%y%m%d}-내이름-오후-{:%H_%M}'.format(now,now)+'.png'
        pyautogui.screenshot(capture_folder/file_name_pm)
```

### 1-3. Run 
#### One-click 실행 :rocket:
_autoplay.bat_ 실행 :arrow_upper_left:

#### 직접 실행
```
python autocapture.py
```

## 2. License

**Project Owner** :  [YeonjiKim0316](https://github.com/YeonjiKim0316) :dog:
<br>**Collaborator** : [guguttemi](https://github.com/guguttemi) :octopus:
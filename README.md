# pyautocapture

## 0. Intro
특정 시간에 자동으로 화면을 캡쳐하여 파일로 저장해주는 Python 기반 프로그램

## 1. Installation
설치 및 실행 방법은 크게 3단계로 구성됩니다.<br>

1-1. Install<br>
1-2. Config<br>
1-3. Run<br>

### 1-1. Install

본 프로그램은 설치 폴더 내에 포함된 autoplay.bat 파일을 통하여 한 번에 실행할 수 있습니다.<br>
단, autoplay.bat 파일을 통하여 프로그램을 실행하기 위해서는 프로그램 설치 시 바탕화면을 root 경로로 지정해야 합니다.<br>
(직접 bat 파일 생성을 통해 변경 가능)

##### git clone을 통한 설치 
```
$ git clone https://github.com/guguttemi/pyautocapture.git
```

##### Download를 통한 설치
1. [Github 메인 페이지]([https://github.com/guguttemi](https://github.com/guguttemi/pyautocapture))의 <span style='background-color:#dcffe4'>**Code&darr;**</span> 선택
2. Download ZIP click
3. 바탕화면에 폴더 압축 해제

### 1-2. Config
0. 압축 해제한 폴더명을 Encore로 변경
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
##### ~.bat 파일로 실행
Encore/_autoplay.bat_ 실행<br>

전제 조건
1. 현재 사용 중인 PC의 사용자 계정명이 Playdata인지 확인
2. autocapture.py파일을 보관 중인 폴더명이 Encore인지 확인<br>

하단의 명령어에서 경로 수정을 통해 실행 위치 변경 가능
```
%windir%\System32\cmd.exe "/K" python C:\Users\Playdata\Desktop\Encore\autocapture.py
```

##### 직접 실행(bat 파일이 동작하지 않을 경우)
```
python autocapture.py
```

## 2. 동작 방식

1. 13시를 제외하고 오전 9시 ~ 18시까지 매 시 05분, 50분마다 캡쳐가 자동으로 진행됨<br>
2. 캡쳐된 이미지는 Encore 폴더 내에 현재 날짜 기준(ex. 220726/)으로 자동 생성된 폴더 내에 저장됨<br>
3. 캡쳐된 이미지 파일명 ex. '20220726-내이름-오전-14_05.png'<br>
4. 정해진 매 분(05, 50) 마다 캡쳐가 진행될 때 '삐' 소리가 울림(sd.Beep(2000, 1000))

## 3. 실행 결과 화면
![processing](https://user-images.githubusercontent.com/88642403/181045855-9ff5666c-4437-4e9c-a02e-8bec661919a9.png)
09:05:00 ~ 17:50:00까지 설정된 상태

## 4. 참고 사항
프로그램 실행 시 자동으로 설치되는 pip module 및 PC 내 존재하는 기존 pip module 간 충돌이 발생할 경우 가상환경 사용 권장
```
- venv를 활용한 가상 환경 설치
# window
python -m venv .venv
.venv\scripts\activate.bat 

# mac
python -m venv .venv
source .venv/bin/activate

- pip modules 일괄 제거
pip freeze > requirements.txt
pip uninstall -r requirements.txt -y
```

## 5. License

**Project Owner** :  [YeonjiKim0316](https://github.com/YeonjiKim0316) :dog:
<br>**Collaborator** : [guguttemi](https://github.com/guguttemi) :octopus:

*잘 되면 내 탓, 안 되면 당신 탓* :ghost:

# pyautocapture

## 0. Intro
#### 프로그램 기능
특정 시간에 자동으로 화면을 캡쳐하여 파일로 저장해주는 Python 기반 프로그램

## 1. Installation
설치 및 실행 방법은 크게 3단계로 구성됩니다.<br>

1-1. Install<br>
1-2. Config<br>
1-3. Run<br>

### 1-1. Install
autoplay.bat 파일을 통하여 프로그램을 실행하기 위해서는 프로그램 설치 시 바탕화면을 root 경로로 지정해야 합니다.<br>
(직접 bat 파일 생성을 통해 변경 가능)

#### git clone을 통한 설치 
```
$ git clone https://github.com/guguttemi/pyautocapture.git
```

#### Download를 통한 설치
1. [Github 메인 페이지](https://github.com/guguttemi)의 <span style='background-color:#dcffe4'>**Code&darr;**</span> 선택
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
#### ~.bat 파일로 실행
_autoplay.bat_ 실행<br>

전제 조건
1. 현재 사용 중인 PC의 사용자 계정명이 Playdata인지 확인
2. autoplay.py파일을 보관 중인 폴더명이 Encore인지 확인<br>
![1](https://user-images.githubusercontent.com/88642403/181035773-2593b458-09f2-42a9-a0e8-6e128168086c.png)

하단의 명령어에서 경로 수정을 통해 실행 위치 변경 가능
```
%windir%\System32\cmd.exe "/K" python C:\Users\Playdata\Desktop\Encore\autocapture.py
```

#### 직접 실행(bat 파일이 잘 안될 경우)
```
python autocapture.py
```

## 2. License

**Project Owner** :  [YeonjiKim0316](https://github.com/YeonjiKim0316) :dog:
<br>**Collaborator** : [guguttemi](https://github.com/guguttemi) :octopus:

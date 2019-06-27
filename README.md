# trydjango19
Try Django 1.9!!

#Try Django 1.9

[유튜브연결](http://http://www.youtube.com/watch?v=yfgsklK_yFo&list=PLEsfXFp6DpzQFqfCur9CJ4QnKQTVXUsRy)

## 1/38 Introduction
- 장고는 파이썬으로 만들어진 대중적으로 많이 쓰이는 웹 프레임 워크다

- 웹 사이트를 만들고 데이터를 정렬 / 저장하고 나누는 좋은 방법

- 우리의 목적은 처음 시작하는 사람들에게 실제 프로젝트를 만들어 보게 하는 것

- 소프트웨어는 매우 매우 좋다

* * *
## 2/38 Walkthrough of our Blog Project

- 우리가 만들 블로그를 빠르게 보여줄게

- 페이스북 공유도 할 수 있고 최근 포스트부터 볼 수 있어 URL 바뀌는 거 봤지? 코멘트 남기는 것도 돼

- admin 계정으로 로그인 할 수 있고 다른 포스트들을 볼 수 있고 새로운 포스트를 작성할 수 있어

- 심플한 검색 창을 볼 수 있어


* * *
## 3/38 Before Getting Started
- 우리 깃에서 레퍼지토리 볼 수 있어

- joincfe.com가입해

- 서브라임 텍스트 쓸거야

* * *

## 4/38 Versions & Install
- 장고 1.9 릴리즈 노트를 볼게 1.8하고 차이점도 보고 지원기간 읽어봐

- LTS(Long Term Support)

- 하나의 가상환경에 하나의 프로젝트가 있는 게 좋다

PIP을 업그레이드 후 설치
```
sudo pip install pip --upgrade
```

virtualenv설치

```
pip install virtualenv --upgrade

mkdir trydjango19
cd trydjango19
virtualenv . 
```

virtualenv 활성화 및 pip 라이브러리 업그레이드 정지
```
source bin/activate
pip freeze
```

장고 설치
```
pip install django==1.9
cd bin
django-admin.py startproject trydjango19
cd trydjango19
```

장고 실행
```
python manage.py runserver
```

이걸 하면 에러메시지가 보이는데 걱정할 필요 없다

브라우저 열어서
127.0.0.1:8000을 들어가면
짜잔 축하해 화면이 보이지
포트를 바꿔볼게

```
python manage.py runserver 8888
```

- 이제 우린 장고에게 다이빙을 한거야
- 다음 시간에는 점프해서 장고 세팅을 많이 바꿔볼게

* * * *
 
## 5/38 Superuser & admin

- 서브라임 텍스트를 써볼게

- Project에서 Save Project As 클릭하고 trydjango19폴더 선택하고 완료

- trydjango19폴더 안에 또 trydjango19가 있는데 상위 폴더 이름을 src로 바꿀게 소스코드란 뜻이야

```
python manage.py runserver
```
를 실행하면

migration이 적용되지않았다라는 메시지가 뜨는데 장고와 DB가 연결되지않았다라는 뜻이야
```
python manage.py migrate
```
로 마이그레이트를 하고 슈퍼유저를 만들어볼게
```
python manage.py createsuperuser
```
이름과 password 설정

```
python manage.py runserver
```
를 한 뒤에
127.0.0.1:8000/admin으로 들어가면 로그인 창을 볼 수 있어
Add user에서 User 추가 가능
마이그레이션에 적용된 거 보이지? 

```
python manage.py
```
를 하면 명령어를 모두 볼 수 있다

* * *
## 6/38 First App & Model
```
python manage.py startapp posts
```
를 하고 나서 서브라임텍스트로 돌아가자

posts폴더 안에 migrations폴더에서
- _init_.py
- admin.py
- apps.py
- models.py
- tests.py
- views.py
를 볼 수 있다

내 생각에는 model이 django app의 핵심이야

models.py파일 내에서 Post클래스를 만들 수 있어
하나의 클래스는 하나의 인스턴스야
우리가 데이터와 일할 수 있게 해줘
```
class Post(models.Model):
```


각 포스트는 title을 가질 수 있어
너가 python3을 쓴다면 __str__을 추가해
settings.py파일을 열고 INSTALLED_APPS에 'posts'를 추가해

`python manage.py runserver`
를 했을 때
오타가 있다면 장고가 알려준다

지금 모델이 변경됐는데 DB와 싱크가 맞지않으니 또 장고가 알려준다
`python manage.py makemigration`
를 통해
야 장고야 우리가 모델을 좀 바꿨어라고 알려준다

`python manage.py migrate`
를 통해 변경된 부분을 적용한다
이제 우리가 만든 Post모델이 적용됐다


* * *
## 7/38 Models to Admin

- 저번 시간에 모델 해봤는데 모델에는 필드타입 종류가 많아
- 장고 공식 도큐먼트를 빠르게 보자
- CharField의 max_length는 유효한 글자 최대치를 말한다
- DateTimeField는 ','로 구분된 필드고 Date와 Time이 들어감




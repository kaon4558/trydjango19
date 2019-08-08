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
- 장고 공식 도큐먼트를 빠르게 보고 레퍼런스를 정리해보자
- CharField의 max_length는 유효한 글자 최대치를 말한다
- max_length써서 무조건 최대 문자 길이 지정해야한다 없으면 에러발생한다
- DateTimeField는 ','로 구분된 필드고 Date와 Time이 들어감

admin.py를 열자
저번에 만들었던 Post 모델을 import해
from posts.models import Post로 적용할 수 있지만 같은 module내에 있으니까 .models라고 입력할 수도 있어
저장하고 서버를 다시 열자(runserver)
browser를 열고 127.0.0.1:8000/admin으로 들어가자
post App하고 Post model을 확인할 수 있어
Posts 선택하고 ADD POST + 버튼 누르고 db에 추가할 수 있어 
Title에 Title이라 줘봐
Title을 엄청나게 길게 시도해볼 수도 있지만 model생성할 때 최대 길이(max_length)120자 제한을 뒀기때문에 그 숫자 넘게는 불가능함
추가한 post들을 지울 수도 있어
다음시간에는 admin을 커스터마이즈 해볼께

## 8/38 Customize Admin

- 우린 이제django admin에  작은 커스터마이징을 할 수 있어
- 우리가 검색할 수 있게 해주고 약간 다르게 보여
- django 문서에서 model admin이라는 걸 살펴보자
- model admin 옵션도 살펴봐

일단 admin.py에 가서 model admin을 만들자
PostAdmin이라는 클래스를 만들어 물론 Post 모델을 붙여서 사용하는 거야
class Meta를 사용해서 Post모델을 사용해
admin.site.register에 추가
이젠 Post랑 PostAdmin이 같이 사용될 거야

* * *
## 9/38 CRUD

- admin은 모델에게 정말 좋은 플레이스야(모델 클래스만 등록하면 조회/추가/수정/삭제 웹 인터페이스를 admin이 제공)
- CRUD가 뭐냐면 Create Retrieve Update Delete를 말해
- 우리 프로젝트 안에 crud.md라는 새 파일을 만들거야
- crud는 너의 앱이 DB와 작동하는 기본적인 방법이야
- list와 search도 볼 수 있어
- create는 뭔가를 만들 수 있고 retrieve는 가져올 수 있고 update는 수정할 수 있고, delete는 지울 수 있어
- 간단하지? 넌 이미 다 했었어
- 무슨 뜻이냐면 너가 페북같은 어떤 어플리케이션을 쓰더라도 넌 이미 경험해봤을 거라는 뜻ㅎ
- list랑 search는 retrieve랑 거의 흡사해 그래서 retrieve안에 넣는 게 나아.
- 이 개념은 django admin에서 엄청 잘 설명된단다
- 만약 우리가 여기로 와서 새로운 post를 추가한다면 뭔가를 생성하는 방법이야
- post를 누르고 바꾸면 이건 update야
- delete버튼이 있고 이걸 누르면 지울 수 있어
- 사이트를 구축하는 다 다른 방법들이야
- 그리고 우리가 기본적으로 우리가 클릭할 때 update기도 하고 retrive이기도 해
- HTTP에 비유한다면 CREATE는 POST, RETRIEVE는 GET, UPDATE는 PUT 혹은 PATCH, DELETE는 DELETE야
- 그래서 이건 HTTP 메소드고 우리가 views에 들어갈 때 얘기할 거야
- views는 우리에게 이 메소드들을 다루는 것을 허용해
- 예를 들면 create view, retrieve view(detailed view같은), update view, delete view
- create/update/delete와는 달리 retrieve는 권한이 필요없다
- CRUD 위키피디아 찾아봐
- READ는 RETRIEVE로 UPDATE는 MODIFY로 DELETE는 DESTROY로 설명 돼
- 너가 하는 모든 프로젝트는 다 이 방법일거야


* * *
## 10/38 Writing our first View

- 이제 우리가 CRUD의 개념에 대해 이해할 시간이야
- 우리는 DB와 함께 작동하는 모델들을 가지고 있어
- 우린 이제 우리가 원하는 방법으로 HTML 컨텐츠를 보여주는 우리의 뷰를 만들 수 있어
- 우리가 List View라고 부르는 게 영상에 있어
- item들의 리스트가 여기 있고 더 길게 만들 수도 있다
- 우린 각 아이템들을 클릭하고 볼 수도 있고
- 이건 우리가 가장 처음 해야하는 거야 왜냐하면 우린 이미 이것들을 DB에 가지고 있거든
- 그래서 이 views.py안에 우리는 list view를 만들거야
- function based views는 더 이해하기 쉬워 왜냐면 이건 단순한 파이썬 기능이거든 class based view에 비해
- function based view를 완전히 마스터하고 class based view를 배우자
- 펑션 베이스드 뷰는 엄청 쉽거든
- 우리의 첫번째 펑션 베이스드 뷰를 만들어보자
- HttpResponse를 import해
- 난 h1 태그로 hello를 리턴할게
- 이 기능을 wrap 해야한다
- 그걸 하기 전에 우리가 이 posts_home을 wrap하는 것은 URL이다
- request 파라미터를 추가해
- 매핑 URL 개념을 배우기 전에 다른 개념을 배우기 좋은 시간이다 멈추고 다음 시간에 봐

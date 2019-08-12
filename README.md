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


* * *
## 11/38 Request & Response

- view 작성을 끝내기 전에 우리는 request와 response의 사이클을 얘기할 거야
- 언제든 너가 웹사이트에 가서 request와 response 사이클에서 뭔가를 할 때!
- 비유하자면 너가 만약 다른 사람의 대문을 노크하고 똑똑똑 야 나 누구누구야라고 하는 걸 request라고 하고
- 가령 다른 문에서 답변을 할 수도 있고 하지 않을 수도 있어
- 너는 이미 이거랑 많이 일하고 있어
- 이건 너가 반드시 어떻게 동작하는 건지 이해해야 하는 것이야
- 내가 만약 링크를 클릭한다면 이건 request야
- 어떤 링크를 클릭하든 다 다른 종류의 request이다
- 난 몇몇의 request를 수행했고 우린 request결과물을 터미널에서 볼 수 있어
- GET GET GET GET GET
- 난 내가 했던 다 다른 request들을 볼 수 있고 admin을 갔거나 내가 갔던 URL들을 볼 수 있지
- 내가 클릭하진 않았지만 웹페이지가 했던 request 결과물들도 볼 수 있지
- 우리가 링크를 클릭하는 모든 순간마다 볼 수 있어
- 내가 만약 not found 페이지를 간다면 보다시피 404 에러를 보여줄거야
- 서버에게 무슨 일이 일어났는지 response를 줄거야
- 나같은 유저가 뭔가를 한다면 서버는 결과물(response)을 돌려주지
- 이 이미지같은 종류의 뭔가가 발생할 때 마다 말이야
- 이 링크를 복사해서 가보면 이미지가 뜨지? 이 이미지를 받는 걸 시도했다는 거야
- 모든 request와 response가 유저한테서만 일어나지 않는다는 거지
- 우리는 우리의 views를 보면서 이 사이클을 이해해야해
- 왜냐하면 요청을 한다면 여기에 있는 response를 리턴하니까
- 만약 우리가 서버라면 이 views에 있는 request들을 다뤄서 response를 준다는 거지 겁나 많이
- 어떤 형태의 HTTP request든 HTTP response로 돌려줘
- request와 response를 하기전에 URL을 사용하는 방법을 알아야해
- view가 이걸 다뤄
- URL은 이걸 매핑하는 패턴이야 담에 봐


* * *
## 12/38 Mapping URLs to Views
- 우린 이제 request를 보내는 곳에 URL 패턴을 만들 수 있어
- 우린 posts를 위한 장소를 봐야해
- urls.py를 열어서 admin을 복붙하고 posts로 바꿀 거야
- URL을 쓰고 달러 표시를 붙여 
- url(r'^posts/$', admin.site.urls)라서 admin으로 들어가
- 우리가 만든 posts_home을 매핑하고 싶어
- admin을 원하는 게 아니지 posts views를 쓰고 싶은거야
- admin.site.urls를 지우고 posts.views.posts_home을 쓰자
- 시도해볼게 무슨 일이 일어나는지 보자 저장하고 새로고침
- post를 찾을 수가 없지 따옴표 붙이고나서 view이름을 제대로 바꿔보자
- 다시 request를 보내면 hello가 나온다
- 이거 세팅 겁나 간단하다
- 다른 방법은 from posts import views하고 views.post_home으로 끝내는 거야
- 난 funcion_based_view에서는 전자를 추천해
- class_based_view에서는 조금 달라

* * *
## 13/38 In App URLs

- 127.0.0.1:8000/admin/어저구저저구라고 치면 admin이랑 관련있는 모든 URL들이 출력돼
- app은 모든 것을 통제해
- post안에 새로운 파일을 만들어보자
- url.py 내부내용들을 전부 복붙하고 admin은 더이상 필요없어서 지우고 달러 사인은 유지해
- urls.py로 돌아가서 include를 import하 달러사인을 지워도 돼
- posts에 접속해보면 다시 Hello를 볼 수 있고 url을 abc$로 바꾸고 새로고침하면 관련된 url로 볼 수 있어
- 자 다시 우리의 view로 돌아가자
- CRUD를 떠올리 detail, list, update, delete를 추가해 url에서도
- 각 링크로 가보명 확인 할 수 있다
- URLs가 어떻게 동작하는지 잘 봤다
- 순서를 바꿔도 동일하다


* * *
## 14/38 Django Templates
- 장고가 최고인 이유중 하나는 Templates를 사용한다는 거야 
- 템플릿은 우리가 우리 웹페이지를 똑똑하게 만들게 도와주고 우리 코드를 효과적으로 만들어줘
- 굉장히 깔끔하게 만들어줘
- import os를 하면 path이슈를 해결해줘
- src안에 Templates 폴더를 만들고 index.html을 만들어
- 내용을 쓰고 우리 urls.py로 돌아가서 적어
- template에도 링크를 바꾸면 TemplateDoesNotExist라는 에러메시지가 나와
- 우리는 약간의 에러를 해결하고 다시 돌아가보면 template is working을 확인 할 수 있다 좋아


* * *
## 15/38 Template Context
- 우린 이제 Template Context를 할거야
- 저번에 render call을 할 때 빈 딕셔너리 기억나?
- 난 좀 더 좋은 걸 알려주고 싶어 template context지
- context를 추가하고 완료해
- 어렵지 않지? 2개의 다른 context 를 추가해보
- context를 추가해봤고 다른 링크에서도 확인 할 수 있어


* * *
## 16/38 QuerySet Basics
- db애서 값을 정렬하는 걸 볼거야
- python manage,py shell를 하면 이건 django project랑 관련된 쉘이 나와
- 앱으로부터 이걸 import해야해
- 장고 쉘을 열고 필터들이 잘 동작하는지 보자
- create 명령어를 반복하면 다 db에 들어간다
- queryset = Post.objeect.all()과 for문으로 전부 출력할 수 도 있어
- django shell 나가고 런서버를 켜고 views에서 from .models import Post로 모델을 추가한 뒤에
- post_list에 queryset = Post.objects.all()을 추가하고 context에도 추가해
- template안에 object_list를 추가할 거야
- 페이지에서 이 posts를 볼 수 았어
- index.html도 수정하고 새로고침을 하면 우린 모든 데이터를 볼 수 있

* * *
## 17/38 Get Item or 404 Query

- 우리의 view에서 각각 아이템 하나씩을 볼 차례야
- post_list를 본다면 각각 아이템을 볼 수 있지
- get_object_or_404 라이브러리를 추가하고
- get_object_or_404는 만약 값이 존재하지 않으면 404에러를 리턴해줘 id가 1이라고 친다면
- post_detail.html을 만들고 index.html을 복사하고 나서 obj를 모두 instance로 바꾸자
- Post는 모델이고 인스턴스로부터 바뀐다는 뜻이야
- 돌려보면 어떻게 URL들이 쿼리들을 이렇게 바꾸는지 궁금하기를 바
- 404에러를 어떻게 해결할지 보여줄게




django 기초
==========
### 한창 파이썬과 웹프레임워크인 장고를 활용하기위해서 서점을 다니며 공부를 했는데 처음 입사한 회사에서 장고를 사용하지 않는 바람에 기억이 가물가물해졌다. 다시 기본에 충실하자는 마인드로 공부하며 정리하려한다.  
#

<center><img src="./다운로드.jpeg" width="300" height="350"></center>  

#
### 이 책을 보면서 공부를 했다. 여러 챕터중에 핵심 이론과 실습을 정리.

# 

> ## DJango 개발환경 구축
>   > 1. Python Programming
>   > 2. Python - django 웹 서버 환경 구축
>   > 3. Django 기본 구조 및 설정
>   > 4. Mysql 환경 구축 및 Django 연동
>   > 5. Django 주요 기능
>   > 6. Django Template Language
>   > 7. Django Database Queryset
>   > 8. Django 예제 프로그램 출력

> ## Web Application 개발 및 배포
>   > 1. 웹 어플리케이션 설계
>   > 2. 웹 어플리케이션 환경 설정
>   > 3. 회원관리 구현
>   > 4. 읿반 게시판 구현
>   > 5. 대화형 게시판 구현
>   > 6. 게시판 댓글 및 추천 구현
>   > 7. 홈페이지 개발
>   > 8. Django 웹 어플리케이션 배포

#
## Django 작동 및 관리 스크립트 파일 - manage.py

    1) Django Framework 웹 서버 작동 - runserver
    python3 manage.py runserver
    
    2) Django 앱 생성 - startapp
    python3 manage.py startapp [앱 이름]

    3) Django DB 모델 생성 - makemigrations
    python3 manage.py makemigrations [앱 이름]

    4) Django DB 모델 변경사항 적용 - migrate
    python3 manage.py migrate

    5) Django DB 모델 클래스 생성 - inspectdb
    python3 manage.py inspectdb [테이블 명]

    Django 모델을 관리하는 models.py에 클래스형태로 기록하기 위해서는 뒤에 '>'를 붙여서 다음과 같이 저장한다.
    python3 manage.py inspectdb [테이블 명] > testapp/models.py

    6) Django 관리자 계정 생성 - createsuperuser
    python3 manage.py createsuperuser 

    7) 정적(Static) 파일 배치 - collectstatic
    python3 manage.py collectstatic

    8) python 코드 수행 - shell
    python3 manage.py shell
   

# 

### Django의 MTV 프레임워크의 각 구성요소 별로 수행하는 역할 (ID와 Password 올바른 지 여부를 판단)

#### - Model : 사용자 정보가 올바른지에 대한 ID, Password를 보관하고 있는 DB 상 데이터
#### - Template : 로그인을 위해서 ID, Password를 입력하고 입력 결과를 전송하기 위한 화면 양식
#### - View : 로그인 기능 수행을 위한 웹페이지를 지정하는 기능과 로그인 정보를 서버로 전송할 때 사용자 정보 DB  데이터를 가져온 후 ID 및 Password가 유효한 지를 검증하고 확인된 결과를 다시 반환하는 기능 수행

#
## Django 프로젝트 기본 파일 구조

    test_proj/              - 프로젝트 포함 디렉토리 
        test_proj/          - 프로젝트 루트 디렉토리 : 장고 프로젝트 수행을 위한 패키지가 저장된 디렉토리
            __pycache__/    - Python3 컴파일 디렉토리 : 'migrate' 명령을 수행했을 때 만들어진다
            __init__.py     - Python3 패키지 디렉토리 명시 파일
            settings.py     - Django 프로젝트 파일
            urls.py         - Django 프로젝트 URL 명시 파일
            wsgi.py         - Django 웹 서비스 호환 파일
        db.sqlite3          - SQLite DB 파일
        manage.py           - Django 프로젝트 실행 파일
        
1. test_proj/ : 프로젝트 파일이 포함된 디렉토리로, 프로젝트 파일을 보관 이외의 용도로는 사용되지 않는다.
2. test_proj/test_proj : 장고 프로젝트 수행을 위한 패키지가 저장된 디렉토리. 매우 중요하므로, 기본 생성된 파일은 반드시 존재해야 한다.
3. test_proj/test_proj/__pycache__: 'migrate' 명령을 수행했을 때 만들어진다.
4. __init__.py : 파일이 위치한 디렉토리가 Python 패키지 디렉토리임을 명시하는 파일이다.
5. settings.py : 장고 프로젝트 상의 모든 환경 설정을 관리하는 파일로, 프로젝트에서 가장 큰 비중을 차지하는 파일이다.
6. urls.py : 장고 프로젝트의 URL을 관리하는 파일이다. 추가 앱 생성 시 앱 별로 URL을 지정할 수는 있지만, 웹 브라우저 상에서 관리되는 모든 URL을 관리하는 파일로 볼 수 있다.
7. wsgi.py : 장고 프로젝트의 웹 서비스를 위한 호환 규격을 명시한 파일.
8. db.sqlite3 : 장고는 처음 설치되었을 때 SQLite DB를 사용하며, 해당 DB와의 연계를 위해 사용되는 파일. 차후 다른 DB를 사용한다면 이 파일은 사용하지 않는다.
9. manage.py : 웹 서버 실행, DB Model 적용을 위한 Migration 등 웹 애플리케이션 실행 및 관리를 위한 파일, 별도의 작업 없이 서버 구동을 위한 용도로 사용된다.

#

## Django 앱 기본 파일 구조
### Django App : 장고 프로젝트 내에는 하나 이상의 장고 앱(App)을 생성 및 관리할 수 있다. 장고 앱이란 장고 프로젝트 내에서 어떠한 특정 기능에 따라 구분된 소규모 프로젝트 단위로 볼 수 있다. __하나의 프로젝트 내에서 여러 개의 앱을 생성하고 관리하며, 또한 같은 기능을 하는 앱을 다른 이름으로 각각 생성하여 관리할 수 있다.__
### 여러 가지 기능을 수행할 경우에는 프로젝트 내에서 앱을 생성하여 기능 별로 구분하여 관리하는 것이 __유지보수 및 확장성 면에서 뛰어나다.__

    python3 manage.py startapp testapp

    testapp/            - 앱(App) 루트 디렉토리
        __init__.p      - Python3 패키지 디렉토리 명시 파일
        admin.py        - 앱 관리자 페이지 등록 Model 정보
        apps.py         - 앱 실행 시 초기 실행 등 설정 파일
        migrations/     - 앱 내 Model 갱신 시 사용
        models.py       - 앱 Model 정보
        tests.py        - 앱 Test 페이지 파일
        views.py        - 앱 View 정보

1. testapp/ : 장고 앱(App) 생성 시 관리되는 루트 디렉토리로, 앱 관리를 위한 파일을 포함하고 있다.
2. __ init__.py : 장고 프로젝트 설치 시 생성되는 파일과 동일한 용도
3. admin.py : 장고 프로젝트는 자체적으로 관리자 페이지를 생성 및 관리하는 기능이 있다. 관리자 페이지는 웹 애플리케이션 상에서 관리되고 있는 데이터를 등록, 조회, 삭제 등의 모든 기능을 수행하기 위한 페이지로, admin.py 파일에서는 관리자 페이지에 들어갈 어떤 데이터가 어떻게 들어갈 것인 지에 대한 정보를 포함하고 있다.
4. apps.py : 장고 앱에 대한 클래스(Class)를 선언 및 정의하는 파일이다. 장고 프로젝트 설정 파일에서 특정 장고 앱을 사용하고자 할때, apps.py 파일에서 선언된 클래스명을 사용하면 해당 앱을 사용할 수 있다.
5. migrations/ : 장고 앱에 대한 DB 변경 사항 발생 시 이에 대한 정보를 포함한 파일을 포함하고 있는 디렉토리, 변경사항이 발생할 때마다 migrations 디렉토리에 파일이 하나씩 생성됨에 따라 변경사항에 대한 이력을 관리한다.
6. models.py : DB에 대한 Model을 정의하는 파일, 해당 DB에서 사용하고자 하는 테이블을 정의 및 관리한다.
7. test.py : 장고 앱 생성 시 테스트 수행을 위해서 자동 생성되는 파일이다.
8. views.py : 장고 앱을 제어하는 View를 정의하는 파일, Model 제어 및 Template 요청사항에 대한 구현을 위한 클래스 및 함수 형태로 구현된다.

#
## Django channel, channel layer update
# 
# Everything you need to know about Django.
    1부 요청 및 응답
    2부 모델과 관리 사이트
    3부 보기 및 템플릿
    4부 양식 및 일반 보기
    5부 테스트
    6부 정적 파일
    7부 관리 사이트 사용자 지정

## 간단한 설문조사 만들어보기
### 1. 사람들이 설문 내용을 보고 직접 투표할 수 있는 개방된 사이트
### 2. 관리자가 설문을 추가, 변경, 삭제할 수 있는 관리용 사이트

    투표 어플리케이션
    polls/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py


    INSTALLED_APPS : 현재 Django 인스턴스에서 활성화된 모든 Django 어플리케이션드의 이름이 담겨 있습니다.
                    
    앱들은 다수의 프로젝트에서 사용되며, 다른 프로젝트에서 쉽게 사용될 수 있도록 패키징하여 배포할 수 있음

 - django.contrib.admin – 관리용 사이트.
 - django.contrib.auth – 인증 시스템.
 - django.contrib.contenttypes – 컨텐츠 타입을 위한 프레임워크.
 - django.contrib.sessions – 세션 프레임워크.
 - django.contrib.messages – 메세징 프레임워크.                  
 - django.contrib.staticfiles – 정적 파일을 관리하는 프레임워크.

        polls/
            models.py 
        
        models.py에 __str__() 메소드를 추가하는것은 
        1. 객체의 표현을 대화식 프롬프트에서 편하게 보려는 이유 말고도,
        2. Django가 자동으로 생성하는 관리 사이트에서도 객체의 표현이 사용되기 때문
            
 #
 ## render ()
 템블릿에 context를 채워넣어 표현한 결과를 HttpResponse 객체와 함께 돌려주는 구문은 자주 쓰는 용법 

 Django는 이런 표현을 쉽게 표현할 수 있도록 단축 기능(shortcuts)를 제공

 render() 함수는 request 객체를 첫번째 인수로 받고, 템플릿 이름을 두번째 인수로 받으며, context 사전형 객체를 세번째 선택적(optional) 인수로 받는다.

 인수로 지정된 context로 표현된 템플릿의 HttpResponse 객체가 반환된다.

 ## get_object_or_404()
 만약 객체가 존재하지 않을 때 get()을 사용하여 Http404 예외를 발생시키는것은 자주 쓰이는 용법

 Django에서 이 기능에 대한 단축 기능을 제공합니다.
 
 get_object_or_404() 함수는 Django 모델을 첫번째 인자로 받고, 몇개의 키워드 인수를 모델 관리자의 get() 함수에 넘깁니다. 만약 객체가 존재하지 않을 경우, Http404 예외가 발생한다.

 ## Python GIL
# Wanted_pre_onboarding
---
## 모델링



## 요구사항 및 구현 설명

1. 상품 등록, 수정, 삭제, 리스트 조회

    주요 고려 사항은 다음과 같습니다.
     - (게시자명, 총펀딩금액, 달성률, D-day, 참여자 수)와 같은 부가 연산을 Model function으로 구현하여 재사용성을 고려하고자 했습니다.
     - 1회 펀딩금액을 product 모델에서 관리하여, 참여자가 버튼을 클릭 할 경우 저장된 금액으로 연산하고 보여줍니다.
     - 정렬에서 기본 정렬은 최근 생성일입니다.
     - 정렬에서 생성일과 총펀딩금액을 if문으로 조건을 나누기보다 dict로 값을 저장하여 정렬하면 더욱 빠른 연산이 가능 할 것으로 생각되어 구현해봤습니다.


## 실행 방법(Local)

1. 해당 프로젝트를 clone하고, 가상환경 생성 및 pip install
~~~
git clone https://github.com/apollo058/wanted_pre_onboarding.git .
pip install -r requirements.txt
~~~

2. SECRET_KEY와 DB PASSWORD 등록
~~~
secret.json을 생성 및 아래 정보 입력

"SECRET_KEY" = "Django SecretKey"
"PASSWORD" = "DB Password"
~~~

3. db table migrate
~~~
python manage.py migrate
~~~

4. 서버 실행
~~~
python manage.py runserver
~~~

## API
1. product 생성, 리스트조회
> http://localhost:8000/products
~~~
# 생성 키값
{
    "title": "의자",
    "publisher": 1,
    "one_price": 10000,
    "amount": 1000000
}
~~~

2. product 상세 조회, 수정, 삭제
> http://localhost:8000/products/<int:pk>

3. User 펀딩 참여 버튼(생성)
> http://localhost:8000/funds
~~~
# 생성 키값
{
    "account": 1,
    "product": 1,
}
~~~

4. Test 실행
~~~
python manage.py test
~~~
---
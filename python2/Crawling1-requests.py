'''
Crawling1-requests.py

requests 라이브러리
    Http 요청을 보내기 위한 간편하고 인기 있는 라이브러리 이다.
    이를 사용하면 웹 페이지를 가져오거나, API와 상호 작용할수 있다.

pip - Python으로 작성된 패키즈를 설치, 관리하는 패키지 시스템
    pip를 이용하여 다른개발자 패키지 쉽게 설치 가능

requests 라이브러리 설치
    pip install requests

    # requests 설치하고 에러발생시 추가 설치
    pip install chardet
    pip install brotli

https://entertain.naver.com/ranking/read?oid=311&aid=0001581475
'''

import requests

url = 'https://entertain.naver.com/ranking/read'
param = {
        'oid': '311',
        'aid':'0001581475'
        }
response = requests.get(url, params=param)
print(response.text)














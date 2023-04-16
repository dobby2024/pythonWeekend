'''
파일명 : Matplotlib1.py

데이터 시각화(data visualiztion) 란
    데이터를 분석한 결과를 사용자가 쉽게 이해할 수 있도록
    표현하여 전달한것을 의미한다.

    1. 많은 양의 데이터 한눈에 살펴볼 수 있다.
    2. 전문지식이 없더라도 누구나 쉽게 해당데이터 인지 사용할 수 있다.
    3. 단순한 데이터의 요약이나 나열보다 더 정확한 데이터 분석 결과를
     얻을 수 있다.
    4. 단순한 데이터에서 알 수 없었던 중요한 정보를 파악할 수 있다.
'''

import matplotlib.pyplot as plt

# 그림을 그릴 Figure 객체 생성
figure = plt.figure()

figure.suptitle('figure suptitle')
plt.title('plt matplotlib1')


# Figure 객체에 Axes 객체 추가
# 행: 2개, 열: 2개, 그리드 인덱스: 1번 (왼쪽 상단)
axes = figure.add_subplot(221)


# x축과 y축 데이터 설정
x = ['Jan', 'Fed', 'Mar', 'Apr', 'May', 'Jun']
y = [1200, 800, 500, 400, 700, 800]

# Axes 객체에 선 그래프 추가
# 선 스타일: 점선(--), 마커: 삼각형(^), 색상: 빨간색
axes.plot(x, y, linestyle='--', marker='^', color='red')

# 그림 출력
plt.show()













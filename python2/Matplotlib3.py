'''
파일명 : Matplotlib3.py

python.exe -m pip install --upgrade pip

https://rigun.tistory.com/m/129
'''

import wordcloud
import matplotlib.pyplot as plt

# 단어와 빈도수 설정
word = {
    'Python': 10,
    'Java': 5,
    'C': 7,
    'C++': 9,
    'JSP':12
}
# WordCloud 객체 생성 및 단어 빈도수 적용
wc = wordcloud.WordCloud()
cloud = wc.generate_from_frequencies(word)

# 그래프 생성
plt.figure()
plt.imshow(cloud)

# 그래프 출력
plt.show()

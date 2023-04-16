'''
파일명 : Matplotlib2.py
'''
import matplotlib.pyplot as plt

# Figure와 Axes 객체 생성
fig, ax = plt.subplots()

#  각 과일의 공급량과 색상 설정
fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange'] # '_'는 비어있는 라벨
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

# 막대 그래프를 생성하여 Axes 객체에 추가
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

# y축 레이블과 그래프 제목 설정
ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')

# 범례 추가
ax.legend(title='Fruit color')

plt.show()



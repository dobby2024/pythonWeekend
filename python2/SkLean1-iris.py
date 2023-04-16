'''
파일명 : SkLean1-iris.py

주피터 노트북 설치
pip install jupyter

명령프롬프트(터미널)
jupyter notebook

pip install scikit-learn
'''
import sklearn

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

print(sklearn.__version__)

import pandas as pd

# 붓꽃 데이터 세트를 로딩합니다.
iris = load_iris()

# 데이터프레임 생성
data = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
target = pd.DataFrame(data=iris['target'], columns=['target'])
df = pd.concat([data, target], axis=1)

# print(df)
# CSV 파일로 저장
df.to_csv('iris.csv', index=False)

# iris 피처
iris_data = iris.data
# iris 레이블(결정값)
iris_label = iris.target
# print(type(iris_data))

# 붓꽃 데이터 DataFrame으로 변환
iris_df = pd.DataFrame(data=iris_data, columns=iris.feature_names)
iris_df['label'] = iris.target
print(iris_df.head(3))

X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_label,
                                                    test_size=0.2, random_state=11)

# DecisionTreeClassifier 객체 생성
dt_clf = DecisionTreeClassifier(random_state=11)

# 학습 수행
dt_clf.fit(X_train, y_train)

# 테스트 예측
pred = dt_clf.predict(X_test)

from sklearn.metrics import accuracy_score
print('예측 정확도: {0:.4f}'.format(accuracy_score(y_test, pred)))

test1 = [[
    4.8,3.2,1.3,0.2
]]
result = dt_clf.predict(test1)
print(result)










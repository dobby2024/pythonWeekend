'''
파일명 : BigO1-O(1).py

빅오 표기법(Big O notation) 
    - 알고리즘의 시간복잡도와 공간복잡도를 분석할 때 사용되는 표기법
    - 입력 크기 n에 대한 함수 f(n)의 실행 시간이나 메모리 사용량을 나타냄
    - 빅오 표기법은 최악의 경우 성능을 표현

빅오 표기법 규칙
    - 상수는 무시:O(2n) -> O(n), O(3n^2) -> O(n^2)
    - 낮은 차수의 항은 무시 :
                O(n^2 + n) -> O(n^2), O(n^3 + 100n^2) -> O(n^3)
'''

# O(1) : 상수 시간 복잡도, 입력 크기와 상관없이 일정한 시간이 걸림
def return_first_value(arr):
    return arr[0]

# 실행코드
arr = [1, 3, 5, 7, 8]
print(return_first_value(arr))






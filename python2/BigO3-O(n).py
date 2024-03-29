'''
파일명 : BigO3-O(n).py
'''

# O(n) : 선형 시간 복잡도, 입력 크기에 비례하여 시간이 걸리는 알고리즘
def linear_search(arr, x):
    # 배열의 크기를 구한다
    size = len(arr)

    # 배열의 모든 원소를 순회하며 찾고자 하는 값을 검색한다.
    for i in range(size):
        # 배열의 i번째 원소가 찾고자 하는 값과 같으면 i를 반환한다.
        if arr[i] == x:
            return i

    # 찾고자 하는 값이 배열에 없는 경우 -1을 반환한다.
    return -1

# 실행코드
arr = [1, 3, 5, 7, 8]
print(linear_search(arr, 5))
'''
파일명 : Search1-LinearSearch.py

선형 검색(Linear Search)
    간단한 검색 알고리즘, 데이터를 처음부터 끝까지
    순차적으로 비교하여 값을 찾는다.
'''

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

# 실행코드
arr = [1, 3, 5, 7, 9]
target = 5
result = linear_search(arr, target)
print(result)














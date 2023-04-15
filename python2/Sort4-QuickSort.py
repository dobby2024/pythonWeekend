'''
파일명 : Sort4-QuickSort.py

4. 퀵 정렬(Quick Sort)
    분할 정복 알고리즘의 일종, 기준점(pivot)을 설정하고
    pivot보다 작은 값을 왼쪽, 큰 값을 오른쪽으로 분할한 후
    각 부분 리스트에 대해 재귀적으로 퀵 정렬을 수행하는 알고리즘.

- 최악의 경우 시간 복잡도: O(n^2)
- 최선의 경우 시간 복잡도: O(n*log n)
- 평균 시간 복잡도: O(n*log n)
'''

# 퀵 정렬 알고리즘을 구현하는 함수
def quick_sort(arr):
    # 리스트 길이가 1이하인 경우 더이상 정렬 필요없다
    if len(arr) <= 1:
        return  arr

    # pivot 값 설정
    pivot = arr[0]

    left, right, equal = [], [], []
    '''
    pivot을 기준으로 left, right, equal 리스트에 나눠 담기
    left: pivot보다 작은 원소들
    right: pivot보다 큰 원소들
    equal: pivot과 같은 원소들
    '''
    for a in arr:
        if a < pivot:
            left.append(a)
        elif a > pivot:
            right.append(a)
        else:
            equal.append(a)

    return quick_sort(left) + equal + quick_sort(right)

# 실행 코드
arr = [4, 2, 7, 1, 3, 6, 8]
print(quick_sort(arr))







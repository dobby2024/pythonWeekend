'''
파일명 : Sort5-MergeSort.py

5. 병합 정렬(Merge Sort)
    분할 정복 알고리즘의 일종으로, 리스트를 절반으로 나눈 후
    각각ㄱ을 재귀적으로 합병 정렬을 하고,
    다시 합치면서 정렬하는 알고리즘

- 최악의 경우 시간 복잡도: O(n*log n)
- 최선의 경우 시간 복잡도: O(n*log n)
- 평균 시간 복잡도: O(n*log n)

'''

# 병합 정렬 알고리즘을 구현하는 함수
def merge_sort(arr):
    # 재귀 종료 조건: 리스트의 길이가 1 이하일 경우, 더 이상 정렬할 필요가 없습니다.
    if len(arr) <= 1:
        return arr

    # 리스트의 중간 인덱스를 계산
    mid = len(arr) // 2

    # 중간을 기준으로 리스트를 두 개로 나누어 각각을 재귀적으로 정렬
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 두 개의 리스트를 병합하여 정렬된 리스트 생성
    return merge(left, right)

# 병합하는 함수
def merge(left, right):
    # 결과를 저장할 리스트를 생성
    result = []

    # 각각의 리스트에 대해 인덱스를 따로 만들어가며 비교하여 작은 값을
    # 결과 리스트에 추가
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 아직 추가하지 못한 나머지 값들을 결과 리스트에 추가
    result += left[i:]
    result += right[j:]

    # 정렬된 리스트 반환
    return result
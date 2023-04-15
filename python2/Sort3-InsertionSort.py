'''
3. 삽입 정렬(Insertion Sort)
    리스트의 모든 요소를 앞에서부터 차례대로
    이미 정렬된 부분과 비교하여 자신의 위치를 찾아 삽입

- 최악의 경우 시간 복잡도: O(n^2)
- 최선의 경우 시간 복잡도: O(n)
- 평균 시간 복잡도: O(n^2)
'''
# 삽입 정렬 알고리즘을 구현하는 함수
def insertion_sort(arr):
    n = len(arr)  # 배열의 길이를 구합니다.

    # 배열의 두 번째 원소부터 마지막 원소까지 반복합니다.
    for i in range(1, n):
        # 현재 원소의 값을 key 변수에 저장합니다.
        key = arr[i]

        # 현재 원소의 이전 원소 인덱스를 j 변수에 저장합니다.
        j = i - 1

        # 이전 원소부터 첫 번째 원소까지 역순으로 반복하면서
        # key 값보다 큰 원소들을 한 칸씩 오른쪽으로 이동시킵니다.
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # 현재 위치의 값을 이전 위치로 이동
            j -= 1  # 이전 위치로 이동

        # key 값을 적절한 위치에 저장합니다.
        arr[j + 1] = key

    # 정렬이 완료된 배열을 반환합니다.
    return arr


# 실행코드
arr = [12, 25, 65, 33, 11, 66]
print(insertion_sort(arr))










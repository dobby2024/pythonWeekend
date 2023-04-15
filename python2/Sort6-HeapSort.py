'''
파일명 : Sort6-HeapSort.py
6. 힙 정렬(Heap Sort)
    최대/최소 힙(heap) 자료구조를 이용하여 배열을 정렬하는 알고리즘

- 최악의 경우 시간 복잡도: O(n*log n)
- 최선의 경우 시간 복잡도: O(n*log n)
- 평균 시간 복잡도: O(n*log n)

'''

import heapq

# 힙 정렬 알고리즘을 구현하는 함수
def heap_sort(arr):
    # 빈 힙을 생성
    h = []

    # 배열의 모든 원소를 힙에 추가
    for value in arr:
        heapq.heappush(h, value)  # 힙에 원소 추가

    # 힙에서 원소를 꺼내 정렬된 리스트 반환
    return [heapq.heappop(h) for i in range(len(h))]


# 실행코드
arr = [4, 10, 3, 5, 1]
print(heap_sort(arr))














'''
파일명 : BigO5-O(n^2).py
'''

# O(n^2) : 제곱 시간 복잡도, 중첩 반복문을 사용하는 알고리즘
def selection_sort(arr):
    # [5, 3, 4, 7, 9, 1]
    # 배열의 길이를 기준으로 외부 반복문을 실행한다.
    for i in range(len(arr)):
        # 최소값의 인덱스를 저장할 변수를 초기화한다.
        min_idx = i

        '''
        i=0 
        
        '''

        # 내부 반복문을 실행하여 i번째부터 배열의 끝까지 탐색
        for j in range(i+1, len(arr)):
            '''
            [5, 3, 4, 7, 9, 1]
            i=0 , min_idx=0
                j=1, arr[1]->3, arr[0]->5, min_idx=1
                j=2, arr[2]->4, arr[1]->3, min_idx=1
                j=3, arr[3]->7, arr[1]->3, min_idx=1
                j=4, arr[4]->9, arr[1]->3, min_idx=1
                j=5, arr[5]->1, arr[1]->3, min_idx=5
            
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            [1, 3, 4, 7, 9, 5]
            i=1 , min_idx=1
                j=2, arr[2]->4, arr[1]->3, min_idx=1
                j=3, arr[3]->7, arr[1]->3, min_idx=1
                j=4, arr[4]->9, arr[1]->3, min_idx=1
                j=5, arr[5]->5, arr[1]->3, min_idx=1
            
            [1, 3, 4, 7, 9, 5]
            i=2 , min_idx=2
                j=3, arr[3]->7, arr[2]->4, min_idx=2
                j=4, arr[4]->9, arr[2]->4, min_idx=2
                j=5, arr[5]->5, arr[2]->4, min_idx=2
            
            [1, 3, 4, 7, 9, 5]
            i=3 , min_idx=3
                j=4, arr[4]->9, arr[3]->7, min_idx=3
                j=5, arr[5]->5, arr[3]->7, min_idx=5
                
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
            [1, 3, 4, 5, 9, 7]
            i=4 , min_idx=4
                j=5, arr[5]->7, arr[4]->9, min_idx=5
                
            [1, 3, 4, 5, 7, 9]
            
            
            
            
            '''


            # 현재 최소값보다 작은 값을 발견하면, 최소값의 인덱스를 업데이트한다.
            if arr[j] < arr[min_idx]:
                min_idx = j

        # 최소값을 찾은 후, i번째 값과 최소값을 교환한다.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    # 정렬이 완료된 배열 반환
    return arr

# 실행코드
arr = [5, 3, 4, 7, 9, 1]
sorted_arr = selection_sort(arr)
print(sorted_arr)











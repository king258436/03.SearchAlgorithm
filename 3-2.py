from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

#생략인 부분 추가로 만들어야함 

arr = [1,2,3,4,5,6] 
print("3의 위치 : ", seq_search(arr,3))

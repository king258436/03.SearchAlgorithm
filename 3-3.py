import copy
from typing import Any, Sequence


def seq_search(seq: Sequence, key: Any) -> int:

    a = copy.deepcopy(seq)
    a.append(key)

    i = 0
    while True:
        if a[i] == key:
            break
        i += 1
    return -1 if i == len(seq) else i

arr = [1,2,3,4,5,6,7,8]
result = seq_search(arr,8)
print(f"8의 위치는 arr[{result}] 입니다.")

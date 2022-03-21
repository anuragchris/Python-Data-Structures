# Link For Problem: https://www.geeksforgeeks.org/sum-elements-k1th-k2th-smallest-elements/

from heapq import heapify, heappop


def sum(arr: list[int], k1: int, k2: int) -> int:

    heapify(arr)

    for _ in range(0, k1):
        heappop(arr)

    sum: int = 0
    for _ in range(k1+1, k2):
        sum += heappop(arr)

    return sum


arr = [20, 8, 22, 4, 12, 10, 14]
k1, k2 = 3, 6
print(sum(arr, k1, k2))

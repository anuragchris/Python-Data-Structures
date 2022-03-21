# https://www.geeksforgeeks.org/find-k-closest-numbers-in-an-unsorted-array/

from queue import PriorityQueue


def k_closest_elements(arr: list[int], k: int, x: int):
    pq = PriorityQueue()

    for i in range(k):
        pq.put((-abs(arr[i]-x), i))

    for i in range(k, len(arr)):
        diff: int = abs(arr[i]-x)
        p, pi = pq.get()
        current: int = -p

        if diff > current:
            pq.put((-current, pi))
            continue
        else:
            pq.put((-diff, i))

    while(not pq.empty()):
        p, q = pq.get()

        print("{} ".format(arr[q]), end="")


arr = [-10, -50, 20, 17, 80]
x: int = 20
k: int = 2
k_closest_elements(arr, k, x)

# Link For Problem: https://www.geeksforgeeks.org/connect-n-ropes-minimum-cost/

from heapq import heapify, heappop, heappush


def min_cost(ropes: list[int]) -> int:

    heapify(ropes)

    cost: int = 0

    while(len(ropes) >= 2):
        first: int = heappop(ropes)
        second: int = heappop(ropes)

        cost += first+second
        heappush(ropes, (first+second))

    return cost


lengths = [4, 3, 2, 6]
print(min_cost(lengths))

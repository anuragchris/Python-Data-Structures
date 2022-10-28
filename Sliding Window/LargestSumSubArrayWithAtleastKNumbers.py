# Link For Problem: https://www.geeksforgeeks.org/largest-sum-subarray-least-k-numbers/

def maxSumWithK(arr: list[int], n: int, k: int) -> int:
    maxSum: list[int] = [0 for i in range(n)]
    maxSum[0] = arr[0]

    curr_max: int = arr[0]

    for i in range(1, n):
        curr_max = max(curr_max, curr_max+arr[i])
        maxSum[i] = curr_max

    sum: int = 0

    for i in range(0, k):
        sum += arr[i]

    result: int = sum

    for i in range(k, n):
        sum = sum+arr[i]-arr[i-k]

        result = max(result, sum, sum+maxSum[i-k])

    return result


a = [1, 2, 3, -10, -3]
k = 4
n = len(a)

print(maxSumWithK(a, n, k))

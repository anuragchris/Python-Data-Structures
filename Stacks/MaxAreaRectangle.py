def largestRectangleArea(heights: list[int]) -> int:
    if len(heights) == 0:
        return 0

    left = [1]*len(heights)
    right = [1]*len(heights)
    # left.append[-1]

    for i in range(1, len(heights)):
        temp = i-1

        while(temp >= 0 and heights[temp] >= heights[i]):
            temp -= left[temp]

        left[i] = i-temp

    for i in range(len(heights)-2, -1, -1):
        temp = i+1

        while(temp < len(heights) and heights[temp] >= heights[i]):
            temp += right[temp]

        right[i] = temp-i

    ans = 0

    for i in range(len(heights)):
        ans = max(ans, heights[i]*(right[i]+left[i]-1))

    return ans


def maxRectangle(arr):
    result = largestRectangleArea(arr[0])

    for i in range(1, len(arr)):

        for j in range(len(arr[i])):

            if arr[i][j]:
                arr[i][j] += arr[i-1][j]
            else:
                arr[i][j] = 0

        result = max(result, largestRectangleArea(arr[i]))

    return result


arr = [[0, 1, 1, 0],
       [1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 0, 0]]
print(maxRectangle(arr))

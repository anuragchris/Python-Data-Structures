def solution(arr):
    stack = list()

    for i in range(len(arr)):
        while(len(stack) > 0 and stack[-1] >= arr[i]):
            stack.pop()
        if(len(stack) == 0):
            print("-1")
        else:
            print(stack[-1])
        stack.append(arr[i])


arr = [1, 3, 0, 2, 5]
solution(arr)

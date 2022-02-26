def solution(arr):
    stack = []
    ans = []
    for i, e in list(enumerate(arr)):
        while(len(stack) != 0 and stack[len(stack)-1] <= arr[i]):
            stack.pop()
        if(len(stack) == 0):
            ans.append(-1)
        else:
            ans.append(stack[(len(stack)-1)])
        stack.append(arr[i])
    for i in range(0, len(arr)):
        print(arr[i], " --> ", ans[i])


arr = [10, 5, 11, 10, 20, 12]
solution(arr)

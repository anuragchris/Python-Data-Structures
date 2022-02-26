def solution(arr):
    stack = []
    ans = []
    for i, e in reversed(list(enumerate(arr))):
        while(len(stack) != 0 and stack[len(stack)-1] <= arr[i]):
            stack.pop()
        if(len(stack) == 0):
            ans.append(-1)
        else:
            ans.append(stack[(len(stack)-1)])
        stack.append(arr[i])
    ans.reverse()
    for i in range(0, len(arr)):
        print(arr[i], " --> ", ans[i])


arr = [11, 13, 21, 3]
solution(arr)

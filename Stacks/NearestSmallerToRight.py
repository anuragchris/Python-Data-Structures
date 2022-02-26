def solution(arr):
    stack = list()
    ans = list()

    for i in reversed(arr):
        while(len(stack) > 0 and stack[-1] >= i):
            stack.pop()
        if(len(stack) == 0):
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(i)
    ans.reverse()

    for i in range(len(arr)):
        print(arr[i], " --> ", ans[i])


arr = [11, 13, 21, 3]
solution(arr)

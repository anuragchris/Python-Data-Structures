def stockSpan(price):
    st = []
    ans = []
    st.append(0)
    ans.append(1)

    for i in range(1, len(price)):
        while len(st) > 0 and price[st[-1]] <= price[i]:
            st.pop()

        ans.append(i+1 if len(st) <= 0 else (i-st[-1]))
        st.append(i)

    for i in ans:
        print(i, end=" ")


price = [10, 4, 5, 90, 120, 80]
stockSpan(price)

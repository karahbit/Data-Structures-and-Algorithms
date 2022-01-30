def fib_tab(n):
    tb = [0, 1]

    for i in range(2, n+1):
        tb.append(tb[i-1] + tb[i-2])

    return tb[n]


print(fib_tab(6))

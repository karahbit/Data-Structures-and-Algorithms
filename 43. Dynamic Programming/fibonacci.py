# Top-down + memo
def fib_memo(n, memo={}):
    if n <= 1:
        return n

    if n not in memo:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)

    return memo[n]


# Bottom-ium + tab
def fib_tab(n):
    tb = [0, 1]

    for i in range(2, n+1):
        tb.append(tb[i-1] + tb[i-2])

    return tb[n]


print(fib_memo(6))
print(fib_tab(6))

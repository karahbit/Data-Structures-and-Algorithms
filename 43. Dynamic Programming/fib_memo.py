from logging.handlers import MemoryHandler


def fib_memo(n, memo={}):
    if n <= 1:
        return n

    if n not in memo:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)

    return memo[n]


print(fib_memo(6))

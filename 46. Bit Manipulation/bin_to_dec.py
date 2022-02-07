def bin_to_dec(x):
    ans = 0
    n = len(x)

    for i in range(n):
        ans += int(x[i]) * 2**(n-i-1)

    return ans


print(bin_to_dec("101"))

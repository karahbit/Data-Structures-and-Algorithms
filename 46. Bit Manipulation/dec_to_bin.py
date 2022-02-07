def dec_to_bin(x):
    ans = ""

    while x >= 1:
        ans = str(x % 2) + ans
        x //= 2

    return ans


print(dec_to_bin(5))

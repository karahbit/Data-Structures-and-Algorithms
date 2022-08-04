def int_to_str(num):
    res = ""

    number = -1*num if num < 0 else num

    while (number > 0):
        digit = number % 10
        number = number // 10
        digit = chr(digit + 48)
        res = digit + res

    res = "-" + res if num < 0 else res

    return res


print(int_to_str(-1234))

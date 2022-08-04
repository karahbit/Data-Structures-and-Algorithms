def str_to_int(s):
    res = 0
    counter = 1

    for c in s[::-1]:
        if c == "-":
            res *= -1
        elif c == " " or c == "+":
            break
        else:
            digit = ord(c) - 48
            res += digit*counter
            counter *= 10

    return res


print(str_to_int("-1234"))

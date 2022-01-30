#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.

# Number Factor Problem  in Python

def f(n):
    if n <= 0:
        return 0
    if n in (1, 2):
        return 1
    elif n == 3:
        return 2
    elif n == 4:
        return 4
    else:
        return f(n-1) + f(n-3) + f(n-4)


# print(f(0))
# print(f(1))
# print(f(2))
# print(f(3))
# print(f(4))
print(f(5))


# Bottom-up
def f(n):

    def f_helper(i, n):
        if i >= n:
            return 0
        if i in (n-1, n-2):
            return 1
        if i == n-3:
            return 2
        if i == n-4:
            return 4
        return f_helper(i+1, n) + f_helper(i+3, n) + f_helper(i+4, n)

    return f_helper(0, n)


print(f(5))


def f(n):
    if n in (0, 1, 2):
        return 1
    if n == 3:
        return 2
    return f(n-1) + f(n-3) + f(n-4)


print(f(5))

# Top-down + memo
def min_steps_memo(s1, s2, i, j, memo={}):
    if i == len(s1):
        return len(s2) - j
    if j == len(s2):
        return len(s1) - i

    if s1[i] == s2[j]:
        return min_steps_memo(s1, s2, i+1, j+1, memo)

    key = (i, j)
    if key not in memo:
        delete = 1 + min_steps_memo(s1, s2, i, j+1, memo)
        insert = 1 + min_steps_memo(s1, s2, i+1, j, memo)
        replace = 1 + min_steps_memo(s1, s2, i+1, j+1, memo)
        memo[key] = min(delete, insert, replace)
    return memo[key]


# Bottom-up + tab
def min_steps_tab(s1, s2):
    m = len(s1)
    n = len(s2)
    tb = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m+1):
        tb[i][0] = i
    for j in range(n+1):
        tb[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                tb[i][j] = tb[i-1][j-1]
            else:
                tb[i][j] = 1 + min(tb[i-1][j], tb[i][j-1], tb[i-1][j-1])

    return tb[-1][-1]


print(min_steps_memo("table", "tbrltt", 0, 0))
print(min_steps_tab("table", "tbrltt"))

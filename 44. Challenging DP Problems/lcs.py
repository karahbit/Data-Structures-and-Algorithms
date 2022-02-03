# Top-down + memo
def lcs_memo(s1, s2, i1, i2, memo={}):
    if i1 == len(s1) or i2 == len(s2):
        return 0

    if s1[i1] == s2[i2]:
        return 1 + lcs_memo(s1, s2, i1+1, i2+1, memo)

    key = (i1, i2)
    if key not in memo:
        op1 = lcs_memo(s1, s2, i1, i2+1, memo)
        op2 = lcs_memo(s1, s2, i1+1, i2, memo)
        memo[key] = max(op1, op2)
    return memo[key]


# Bottom-up + tab
def lcs_tab(s1, s2):
    m = len(s1)
    n = len(s2)
    tb = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for col in range(n-1, -1, -1):
        for row in range(m-1, -1, -1):
            if s1[row] == s2[col]:
                tb[row][col] = 1 + tb[row+1][col+1]
            else:
                tb[row][col] = max(tb[row+1][col], tb[row][col+1])

    return tb[0][0]


# Bottom-up + tab + Space Optimization
def lcs_tab(s1, s2):
    m = len(s1)
    n = len(s2)

    if n < m:
        s1, s2 = s2, s1
        m, n = n, m

    previous = [0] * (m + 1)
    current = [0] * (m + 1)

    for col in range(n-1, -1, -1):
        for row in range(m-1, -1, -1):
            if s2[col] == s1[row]:
                current[row] = 1 + previous[row + 1]
            else:
                current[row] = max(previous[row], current[row + 1])
        previous, current = current, previous

    return previous[0]


print(lcs_memo("elephant", "eretpat", 0, 0))
print(lcs_tab("elephant", "eretpat"))

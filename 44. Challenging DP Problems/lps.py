# Efficient Approach: Top-Down + Memo
# TC = O(n^2)
# SC = O(n^2) recursive
def lps_memo(s, l, r, memo):
    if l > r:
        return 0
    if l == r:
        return 1
    if memo[l][r]:
        return memo[l][r]

    if s[l] == s[r]:
        memo[l][r] = 2 + lps_memo(s, l+1, r-1, memo)
    else:
        op1 = lps_memo(s, l, r-1, memo)
        op2 = lps_memo(s, l+1, r, memo)
        memo[l][r] = max(op1, op2)
    return memo[l][r]


# Optimal Approach: Bottom-up + Tab
# TC = O(n^2)
# SC = O(n^2)
def lps_tab(s):
    n = len(s)
    tb = [[0] * n for _ in range(n)]

    for i in range(n-1, -1, -1):
        tb[i][i] = 1
        for j in range(i+1, n):
            if s[i] == s[j]:
                tb[i][j] = 2 + tb[i+1][j-1]
            else:
                tb[i][j] = max(tb[i+1][j], tb[i][j-1])

    return tb[0][n-1]


# Improved Optimal Approach: Bottom-up + Tab + Space Optimization
# TC = O(n^2)
# SC = O(n)
def lps_tab(s):
    n = len(s)
    prev = [0] * n
    prev[n-1] = 1

    for i in range(n-1, -1, -1):
        curr = prev[:]
        curr[i] = 1
        for j in range(i+1, n):
            if s[i] == s[j]:
                curr[j] = 2 + prev[j-1]
            else:
                curr[j] = max(prev[j], curr[j-1])
        prev = curr

    return prev[n-1]


s = "ELRMENMET"
memo = [[None for _ in s] for _ in s]
print(lps_memo(s, 0, 8, memo))
print(lps_tab(s))

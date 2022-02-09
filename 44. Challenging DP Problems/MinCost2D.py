# Top-down + memo
def min_cost2D_memo(matrix, i, j, memo={}):
    if i == len(matrix) or j == len(matrix[0]):
        return float('inf')

    if i == len(matrix) - 1 and j == len(matrix[0]) - 1:
        return matrix[-1][-1]

    key = (i, j)
    if key not in memo:
        op1 = min_cost2D_memo(matrix, i, j+1)
        op2 = min_cost2D_memo(matrix, i+1, j)
        memo[key] = matrix[i][j] + min(op1, op2)
    return memo[key]


# Bottom-up + tab
def min_cost2D_tab(matrix):
    m = len(matrix)
    n = len(matrix[0])
    tb = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m+1):
        tb[i][n] = float('inf')
    for j in range(n+1):
        tb[m][j] = float('inf')
    tb[m-1][n-1] = matrix[m-1][n-1]

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i != m-1 or j != n-1:
                tb[i][j] = matrix[i][j] + min(tb[i][j+1], tb[i+1][j])

    return tb[0][0]


TwoDList = [[4, 7, 8, 6, 4],
            [6, 7, 3, 9, 2],
            [3, 8, 1, 2, 4],
            [7, 1, 7, 3, 7],
            [2, 9, 8, 9, 3]
            ]

# print(min_cost2D_memo(TwoDList, 0, 0))
# print(min_cost2D_tab(TwoDList))

assert min_cost2D_memo(TwoDList, 0, 0) == 36
assert min_cost2D_memo(TwoDList, 0, 0) == min_cost2D_tab(TwoDList)
print()
print("All tests passed!")
print()

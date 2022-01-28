#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.

# Minimum Cost in 2D array

def findMinCost(twoDArray, row, col):
    if row == -1 or col == -1:
        return float('inf')
    elif row == 0 and col == 0:
        return twoDArray[0][0]
    else:
        op1 = findMinCost(twoDArray, row-1, col)
        op2 = findMinCost(twoDArray, row, col-1)
        return twoDArray[row][col] + min(op1, op2)


def min_cost2D(matrix, i, j):
    if i == len(matrix) or j == len(matrix[0]):
        return float('inf')

    if i == len(matrix) - 1 and j == len(matrix[0]) - 1:
        return matrix[-1][-1]

    op1 = min_cost2D(matrix, i, j+1)
    op2 = min_cost2D(matrix, i+1, j)

    return matrix[i][j] + min(op1, op2)


TwoDList = [[4, 7, 8, 6, 4],
            [6, 7, 3, 9, 2],
            [3, 8, 1, 2, 4],
            [7, 1, 7, 3, 7],
            [2, 9, 8, 9, 3]
            ]

print(findMinCost(TwoDList, 4, 4))
print(min_cost2D(TwoDList, 0, 0))

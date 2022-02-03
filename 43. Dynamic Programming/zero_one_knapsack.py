class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight


# Top-down + memo
def zo_knapsack_memo(items, capacity, index, memo={}):
    if capacity <= 0 or index < 0 or index >= len(items):
        return 0

    key = (capacity, index)
    if key not in memo:
        if items[index].weight <= capacity:
            include = items[index].profit + \
                zo_knapsack_memo(items, capacity -
                                 items[index].weight, index+1, memo)
            exclude = zo_knapsack_memo(items, capacity, index+1, memo)
            memo[key] = max(include, exclude)
        else:
            return 0
    return memo[key]


# bottom-up + tab
def zo_knapsack_tab(profits, weights, capacity):
    rows = len(profits) + 1
    tb = [[0] * (capacity+2) for _ in range(rows)]
    for row in range(rows):
        tb[row][0] = 0
    for col in range(capacity+1):
        tb[rows-1][col] = 0

    for row in range(rows-2, -1, -1):
        for col in range(1, capacity+1):
            inc = exc = 0
            if weights[row] <= col:
                inc = profits[row] + tb[row+1][col-weights[row]]
            exc = tb[row+1][col]
            tb[row][col] = max(inc, exc)
    return tb[0][capacity]


mango = Item(31, 3)
apple = Item(26, 1)
orange = Item(17, 2)
banana = Item(72, 5)
items = [mango, apple, orange, banana]

print(zo_knapsack_memo(items, 7, 0))
print(zo_knapsack_tab([31, 26, 17, 72], [3, 1, 2, 5], 7))

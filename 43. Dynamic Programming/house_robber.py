# Top-down + memo
def house_robber_memo(houses, index, dp={}):
    if index >= len(houses):
        return 0
    if index not in dp:
        rob_first = houses[index] + house_robber_memo(houses, index+2, dp)
        skip_first = house_robber_memo(houses, index+1, dp)
        dp[index] = max(rob_first, skip_first)
    return dp[index]


# Bottom-up + tab
def house_robber_tab(houses, index):
    tb = [0] * (len(houses) + 2)

    for i in range(len(houses)-1, -1, -1):
        tb[i] = max(houses[i] + tb[i+2], tb[i+1])

    return tb[0]


houses = [6, 7, 1, 30, 8, 2, 4]
print(house_robber_memo(houses, 0))
print(house_robber_tab(houses, 0))

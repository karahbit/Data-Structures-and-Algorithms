#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.

# Coin Change Problem  in Python


def coinChange(totalNumber, coins):
    N = totalNumber
    coins.sort()
    index = len(coins) - 1
    while N > 0:
        coinValue = coins[index]
        if N >= coinValue:
            print(coinValue)
            N = N - coinValue
        if N < coinValue:
            index -= 1


coins = [1, 2, 5, 20, 50, 100]
coinChange(201, coins)

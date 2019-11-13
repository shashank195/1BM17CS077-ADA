from collections import defaultdict
amount = 11
coins = [1,2,5]

def computeCoinChange(coins, amount):
    dp = [[0]*(amount+1) for _ in range(len(coins))]

    for i in range(amount+1):
        dp[0][i] = i // coins[0]
    
    for i in range(1, len(coins)):
        for j in range(1, amount+1):
            if j >= coins[i]:
                dp[i][j] = min(dp[i-1][j], 1 + dp[i][j-coins[i]])
            else:
                dp[i][j] = dp[i-1][j]

    return dp

def calculateCoins(dp):
    i, j = len(dp)-1, len(dp[0])-1
    coinList = defaultdict(int)
    print(i,j)
    while i >= 0 and j >= 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] < dp[i-1][j]:
            coinList[coins[i]] += 1
            j -= coins[i]
        if i == 0:
            coinList[coins[i]] += 1
            
    return coinList

dp = computeCoinChange(coins, amount)
print(calculateCoins(dp))
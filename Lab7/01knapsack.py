# values = [60,100,120]
# weights = [1,2,3] # factorize weights list and total weight /10 if trailing zeroes
# w = 5


def solveKnapsack(values, weights, w):
    dp = []
    for i in range(len(weights)):
        dp.append([0]*(w+1))
        
    for i in range(len(weights)):
        for j in range(1,w+1):
            if weights[i] <= j:
                dp[i][j] = max(dp[i-1][j], values[i] + dp[i-1][j-weights[i]])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp)

values = [1,4,4,5,7]
weights = [1,2,3,4,5]
w = 9
solveKnapsack(values, weights, w)

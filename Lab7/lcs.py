# str1 = 'ASDH'
# str2 = 'ADH'
str1 = 'ROUNAK'
str2 = 'ROUAKN'

m = len(str1) + 1
n = len(str2) + 1

dp = [[0]*(m)]*(n)

for i in range(1,m):
    for j in range(1,n):
        if i == 0 or j == 0:
            dp[i][j] = 0
 
        elif str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1

        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[m-1][n-1])
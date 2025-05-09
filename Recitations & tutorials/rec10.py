def denomination(n):
    coins = [1, 5, 10, 20, 50, 100]
    if(1 <= n <= 6):
        return coins[n-1]
    else:
        return 0

def cc(a, n):
    if(a == 0):
        return 1
    elif(a < 0):
        return 0
    elif(n == 0):
        return 0
    else:
        return cc(a - denomination(n), n) + cc(a, n - 1)

memoize_table = {}

def cc_memoized(a, n):
    if(a == 0):
        return 1
    elif(a < 0):
        return 0
    elif(n == 0):
        return 0
    else:
        if((a, n) not in memoize_table):
            result = cc_memoized(a - denomination(n), n) + cc_memoized(a, n-1)
            memoize_table[(a, n)] = result
            return result
        else:
            return memoize_table[(a, n)]

def cc_dp(amount, coins):
    coins_list = [1, 5, 10, 20, 50, 100]
    available_coins = coins_list[:coins]
    dp = [0] * (amount + 1)
    dp[0] = 1  # one way to make 0 cents

    for coin in available_coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]

#print(cc(500, 6))
#print(cc_memoized(500, 6))
#print(cc_dp(500, 6))

prices = {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24, 10:30}

def cut_rod(n, prices):
    if(n <= 0):
        return 0
    
    max_profit = -1

    for i in range(1, n + 1):
        for j in prices:
            if(j > i):
                break
            profit = prices[j] + cut_rod(n - j, prices)
            max_profit = max(max_profit, profit)
    
    return max_profit

def cut_rod_dp(n, prices):
    dp_table = [0] * (n + 1)
    dp_table[1] = 1

    for i in range(1, n + 1):
        max_profit = -1
        for j in range(1, i + 1):
            if(j in prices and j <= i):
                profit = prices[j] + dp_table[i - j]
                max_profit = max(max_profit, profit)
            else:
                continue
        dp_table[i] = max_profit
    
    return dp_table[n]
            

print(cut_rod(4, prices))
print(cut_rod_dp(4, prices))
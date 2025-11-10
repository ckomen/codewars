def count_change(money, coins):
    memo = {}
​
    def helper(amount, index):
        if amount == 0:
            return 1  
        if amount < 0 or index == len(coins):
            return 0  
        if (amount, index) in memo:
            return memo[(amount, index)]
        with_coin = helper(amount - coins[index], index)
        without_coin = helper(amount, index + 1)
​
        memo[(amount, index)] = with_coin + without_coin
        return memo[(amount, index)]
​
    return helper(money, 0)
​
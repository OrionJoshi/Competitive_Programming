# Method-1

def maxProfit(prices):
    if len(prices) == 1:
        return 0
    
    profit = 0
    currentBuy = prices[0]

    for i in range(1, len(prices)):
        if currentBuy > prices[i]:
            currentBuy = prices[i]
        else:
            currentProfit =  prices[i] - currentBuy
            if currentProfit > profit:
                profit = currentProfit
                
    return profit

# Time Complexity : O(n)
# Space Complexity : O(1)
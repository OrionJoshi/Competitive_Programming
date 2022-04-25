# Method-1

def maxProfit(prices):
    if len(prices) == 1:
        return 0
    
    profit = [] 
    for i in range(1, len(prices)):
        profit.append(max(0, prices[i] - prices[i-1])) 

    return sum(profit)

# Time Complexity : O(n)
# Space Complexity : O(n)
# Method-1 Using Stack

def finalPrices(prices):
    result = prices[:]
    stack = []
    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] >= price:
            result[stack.pop()] -= price
        stack.append(i)
        
    return result

# Time Complexity : O(n)
# Space Complexity : O(n)
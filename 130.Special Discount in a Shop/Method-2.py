# Method-2 Iterative

def finalPrices(prices):
    length = len(prices)
    result = []
    
    for i in range(length):
        for j in range(i + 1, length):
            if prices[j] <= prices[i]:
                result.append(prices[i] - prices[j])
                break
        else:
            result.append(prices[i])
                
    return result

# Time Complexity : O(n^2)
# Space Complexity : O(n)
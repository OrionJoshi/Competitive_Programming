# Method-1

def maxIceCream(costs, coins):
    costs.sort()
    totalIcecream = 0
    i = 0
    
    while coins > 0 and i < len(costs):
        if costs[i] > coins:
            break
        else:
            totalIcecream += 1
            coins -= costs[i]
        i += 1
        
    return totalIcecream

# Time Complexity : O(nlogn)
# Space Complexity : O(1)
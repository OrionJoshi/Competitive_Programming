# Method-1 Iterative

def arrangeCoins(n):
    count = 0
    i = 1
    totalCoin = 0
    
    while True:
        print('a')
        totalCoin += i
        count += 1
            
        if n - totalCoin < i + 1:
            return count

        i += 1

# Time Complexity : O(logn)
# Space Complexity : O(1)
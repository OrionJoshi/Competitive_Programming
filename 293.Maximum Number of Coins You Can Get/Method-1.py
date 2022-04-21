# Method-1

def maxCoins(piles):
    piles.sort(reverse=True)
    sum = 0
    for i in range(1,len(piles) - int(len(piles) / 3), 2):
        sum += piles[i]
        print(sum)
    return sum

# Time Complexity : O(nlogn)
# Space Complexity : O(1)
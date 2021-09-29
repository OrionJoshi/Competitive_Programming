# Method-1

def numWaterBottles(numBottles, numExchange):
    return numBottles + int((numBottles - 1) / (numExchange - 1))

# Time Complexity : O(1)
# Space Complexity : O(1)

# Input: numBottles = 9, numExchange = 3
# Output: 13
# Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
# Number of water bottles you can drink: 9 + 3 + 1 = 13.
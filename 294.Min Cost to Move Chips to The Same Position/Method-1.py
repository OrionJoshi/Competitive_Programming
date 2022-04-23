# Method-1

def minCostToMoveChips(position):
    even_cnt = 0
    odd_cnt = 0
    for i in position:
        if i % 2 == 0:
            even_cnt += 1
        else:
            odd_cnt += 1
    return min(even_cnt, odd_cnt)

# Time Complexity : O(n)
# Space Complexity : O(1)
# Method-1

def canThreePartsEqualSum(arr):
    val = sum(arr)
    num = 0
    val_3 = val // 3

    if val % 3 == 0:
        summ= 0
        for i in range(len(arr)):
            summ = summ + arr[i]
            if summ == val_3:
                summ = 0
                num+=1
            if num==2 and i < len(arr) - 1:
                return True      
    return False

# Time Complexity : O(n)
# Space Complexity : O(1)
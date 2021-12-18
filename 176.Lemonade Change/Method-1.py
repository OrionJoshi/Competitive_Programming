# Method-1

def lemonadeChange(bills):
    if not bills[0] == 5:
        return False
    mapping = {
        5 : 0,
        10 : 0,
    }
    for i in range(len(bills)):
        if bills[i] == 5:
            mapping[bills[i]] += 1
        elif bills[i] == 10:
            if mapping[5] >= 1:
                mapping[10] += 1
                mapping[5] -= 1
            else:
                return False
        else:
            if mapping[10] >= 1 and mapping[5] >= 1:
                mapping[10] -= 1
                mapping[5] -= 1
            elif mapping[5] >= 3:
                mapping[5] -= 3
            else:
                return False
    return True

# Time Complexity : O(n)
# Space Complexity : O(1)
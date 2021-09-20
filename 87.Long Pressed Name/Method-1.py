# Method-1 Using pointers

def isLongPressedName(name, typed):
    nameLen = len(name)
    typedLen = len(typed)

    ptr1 = 0
    ptr2 = 0

    while ptr1 <= nameLen and ptr2 < typedLen:
        if ptr1 < nameLen and name[ptr1] == typed[ptr2]:
            ptr1 += 1
            ptr2 += 1
        elif ptr1 != 0 and name[ptr1 - 1] == typed[ptr2]:
            ptr2 += 1
        else:
            return False

    return ptr1 == nameLen and ptr2 == typedLen

# Time Complexity : O(n)
# Space Complexity : O(1)

# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.
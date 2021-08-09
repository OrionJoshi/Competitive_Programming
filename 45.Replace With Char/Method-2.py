# Method-2

def replaceWithChar(s):
        length = len(s)
        lst = list(s)

        for i in range(0, length, 2):
            currentNum = i + 1
            if currentNum < length:
                lst[currentNum] = chr(ord(lst[i]) + int(lst[currentNum]))

        return ''.join([str(elem) for elem in lst])

# Time Complexity : O(n)
# Space Complexity : O(n)
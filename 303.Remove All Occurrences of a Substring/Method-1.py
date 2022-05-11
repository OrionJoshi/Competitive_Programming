# Method-1

def removeOccurrences(s, part):
    string = s.replace(part,"",1)

    while part in string:
        string = string.replace(part,"",1)

    return string

# Time Complexity : O(n)
# Space Complexity : O(n)
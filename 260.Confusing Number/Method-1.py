# Method-1

def confusingNumber(N):
    mapping = {
        '0': '0',
        '1': '1',            
        '6': '9',
        '8': '8',
        '9': '6',            
    }
    
    rotated_str = ""
    n_str = str(N)

    for c in n_str[::-1]:
        if c not in mapping:
            return False
        else:
            rotated_str += mapping[c]
            
    return rotated_str != n_str

# Time Complexity : O(n)
# Space Complexity : O(n)
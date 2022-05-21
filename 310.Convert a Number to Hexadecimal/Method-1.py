# Method-1

def toHex(num):
    if num == 0: 
        return '0'
    map = '0123456789abcdef'
    result = ''
    
    if num<0: 
        num += 2 ** 32
        
    while num > 0:
        digit = num % 16
        num = (num-digit) // 16
        result += str(map[digit])
        
    return result[::-1]

# Time Complexity : O(n)
# Space Complexity : O(n)
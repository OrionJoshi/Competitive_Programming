# Method-1 Bitwise operator

def getSum(self, a: int, b: int) -> int:
    mask = 0xFFFFFFFF # for restricting up to 32 bit
    while b:
        temp = (a & b) << 1
        a = (a ^ b) & mask
        b = temp & mask 
        
    max_int = 0x7FFFFFFF

    return a if a < max_int else ~(a ^ mask)

# Time Complexity : O(n)
# Space Complexity : O(1)
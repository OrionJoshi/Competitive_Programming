# Method-2 Using Iterative method

def mySqrt(num):
    
    init = 0
    
    while 1:
        
        nextInt = init + 1
        currentSqrt = init * init
        nextSqrt = nextInt * nextInt
        
        if currentSqrt == num:
            return init
        elif nextSqrt == num:
            return nextInt
        elif currentSqrt < num < nextSqrt:
            return init
        
        init += 1

# Time Complexity : O(√n)
# Space Complexity : O(1)
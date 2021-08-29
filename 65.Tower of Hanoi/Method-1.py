# Method-1 Using Recursion

def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)

# Time Complexity : O(2^n)
# Space Complexity : O(n)
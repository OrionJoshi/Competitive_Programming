# Method-1 Using pointer

def numRescueBoats(people, limit):
    people.sort()
    noOfBoat = 0
    i = 0
    j = len(people) - 1
    
    while i <= j:
        noOfBoat += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return noOfBoat

# Time Complexity : O(nlogn)
# Space Complexity : O(1)
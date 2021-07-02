# Method-1: iterative Method

def smallestDifference(arrayOne, arrayTwo):

    smallDiff = arrayOne[0] - arrayTwo[0]
    diffArray = [arrayOne[0], arrayTwo[0]]
    for i in range(len(arrayOne) - 1):
        for j in range(len(arrayTwo) - 1):
            if arrayOne[i] > arrayTwo[j]:
                newDiff =   arrayOne[i] - arrayTwo[j]
            else:
                if newDiff <= smallDiff:
                    smallDiff = newDiff
                    diffArray = [arrayOne[i], arrayTwo[j]]
    return diffArray, smallDiff
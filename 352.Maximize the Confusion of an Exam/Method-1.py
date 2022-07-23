# Method-1

def maxConsecutiveAnswers(answerKey, k):
    n = len(answerKey)
    left = ret = numofT = numofF = 0
    
    for right in range(n):
        if answerKey[right] == 'T':
            numofT += 1
        else:
            numofF += 1
        while numofT > k and numofF > k:
            if answerKey[left] == 'T':
                numofT -= 1
            else:
                numofF -= 1
            left += 1
        ret = max(ret, right - left + 1)

    return ret

# Time Complexity : O(n)
# Space Complexity : O(1)
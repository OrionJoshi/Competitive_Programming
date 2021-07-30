#Method-1

def truncateSentence(sentence, k):
    length = len(sentence)
    resultSentence = ''
    pointer = 0
    
    while k != 0 and pointer < length:
        currentChar = sentence[pointer]
        if currentChar == " ":
            k -= 1
            if k == 0:
                break
        resultSentence += currentChar
        pointer += 1
        
    return resultSentence

# Time Complexity : O(n)
# Space Complexity : O(1)
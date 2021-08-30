# Method-1

def sortSentence(string):
    splitedStr = string.split()
    resultedStr = [''] * len(splitedStr)
    
    for word in splitedStr:
        realWord = word[:-1]
        wordPos = int(word[-1]) - 1
        resultedStr[wordPos] = realWord
        
    return ' '.join(resultedStr)

# Time Complexity : O(n)
# Space Complexity : O(n)
# Method-1 Using deque

def deckRevealedIncreasing(deck):
    length = len(deck)
    result = [None] * length
    dequeu = [i for i in range(length)]
    
    for x in sorted(deck):
        idx = dequeu.pop(0)
        result[idx] = x
        
        if len(dequeu) != 0 and dequeu[0]:
            dequeu.append(dequeu.pop(0))
    return result
    
# Time Complexity : O(nlogn)
# Space Complexity : O(n)
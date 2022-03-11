# Method-1

from collections import defaultdict
import string
import re

def mostCommonWord(paragraph, banned):
    my_dict = defaultdict(int)
    par = re.split("[" + string.punctuation + " "+ "]+", paragraph.lower())
    max_count = 0
    max_word = ""
    
    for word in par:
        if word not in banned:
            my_dict[word]+=1
            
            if my_dict[word] > max_count:
                max_count = my_dict[word]
                max_word = word
                
    return max_word
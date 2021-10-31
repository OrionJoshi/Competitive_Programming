# Method-1

def freqAlphabets(s):
        ref = " abcdefghijklmnopqrstuvwxyz"
        i = 0
        out = []
        while i < len(s):
            curr = s[i]
            if i + 2 < len(s) and s[i + 2] == '#':
                curr = s[i:i+2]
                out.append(ref[int(curr)])
                i += 2
            else:
                out.append(ref[int(curr)])
            i += 1
        return "".join(out)

# Time Complexity : O(n)
# Space Complexity : O(n)

# Input: s = "10#11#12"
# Output: "jkab"
# Explanation: "j" -> "10#" ,
# "k" -> "11#" , "a" -> "1" , "b" -> "2".
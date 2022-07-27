# Method-1

def uncommonFromSentences(s1, s2):
        s = s1.split(' ') + s2.split(' ')
        res = []
        d = {}

        for i in s:
          if i in d:
            d[i] += 1
          else:
            d[i] = 1

        for i in d:
          if d[i] == 1:
            res.append(i)

        return res

# Time Complexity : O(n)
# Space Complexity : O(n)
def levenshteinDistance(str1, str2):
   edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
   for i in range(1,len(str2)):
      edits[i][0] = edits[i - 1][0] + 1
   for i in range(1, len(str2) + 1):
      for j in range(1, len(str1) + 1):
         if str2[i - 1] == str1[ j - 1]:
            edits[i][j] = edits[i - 1][j - 1]
         else:
            edits[i][j] = 1 + min(edits[i - 1][j - 1], edits[i][j - 1], edits[i - 1][j])
   return edits[-1][-1]


# Time Complexity:  O(nm)
# Space Complexity: O(nm), Where n = length of first string and m = length of second string

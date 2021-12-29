# Method-1

def mergeLinkedLists(headOne, headTwo):
  p1 = headOne
  p1Prev = None
  p2 = headTwo

  while p1 is not None and p2 is not None:
    if p1.value < p2.value:
      p1Prev = p1
      p1 = p1.next
    else:
      if p1Prev is not None:
        p1Prev.next = p2
      p1Prev = p2
      p2 = p2.next
      p1Prev.next = p1

  if p1 is None:
    p1Prev.next = p2
  
  return headOne if headOne.value < headTwo.value else headTwo


# Time Complexity : O(n + m)
# Space Complexity : O(1)
# Method-1

def countStudents(students, sandwiches):
    while sandwiches:
        if sandwiches[0] in students:
            students.remove(sandwiches[0])
            sandwiches.pop(0)
        else:
            break
    return len(sandwiches)

# Time Complexity : O(n)
# Space Complexity : O(1)
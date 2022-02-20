# Method-1

def capitalizeTitle(title):
    title = title.split(' ')

    for i in range(len(title)):
        if len(title[i]) > 2:
            title[i] = title[i][0].capitalize() + title[i][1:].lower()
        else:
            title[i] = title[i].lower()

    return ' '.join(title)

# Time Complexity : O(n)
# Space Complexity : O(1)
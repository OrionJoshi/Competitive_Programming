# Method-1

def maximumTime(time):
    time = list(time)
    
    for i in range(len(time)):
        if time[i] == '?':
            if i == 0:
                if time[i + 1] in '0123':
                    time[i] = '2'
                else:
                    time[i] = '1'
            elif i == 1:
                if time[i - 1] == '2':
                    time[i] = '3'
                else:
                    time[i] = '9'
            elif i == 3:
                time[i] = '5'
            else:
                time[i] = '9'
                
    return ''.join(time)

# Time Complexity : O(n)
# Space Complexity : O(1)
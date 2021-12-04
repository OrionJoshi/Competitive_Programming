# Method-1

def badSensor(sensor1, sensor2):
    length = len(sensor1)
    i = 0
    defact = -1
    
    while i < length:
        if not sensor1[i] == sensor2[i]:
            if i >= length - 1:
                if sensor1[i -1] == sensor2[i]:
                    defact = 1
                elif sensor2[i -1] == sensor1[i]:
                    defact = 2
                else:
                    defact = -1
            else:
                while i < length - 1 and sensor1[i] == sensor2[i + 1]:
                    i += 1
                if i == length - 1:
                    defact = 1
                else:
                    defact = 2
            break
        else:
            i += 1

    return defact

# Time Complexity : O(n)
# Space Complexity : O(1)
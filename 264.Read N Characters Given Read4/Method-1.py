# Method-1

def read(buf, n):
    index = 0

    while index < n:
        buf4 = [" "] * 4
        count = read4(buf4)

        if count == 0:
            break

        count = min(count, n - index)
        buf[index:] = buf4[:count]
        index += count

    return index

# Time Complexity : O(n)
# Space Complexity : O(1)
# Method-2: recursive method

def getNthFib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)

num = int(input("Enter nth fibonacci you want to find:"))

result = getNthFib(num)

print("The required fibonacci number is:{}".format(result))

# Time Complixity: O(2^n)
# Space Complixity: O(n)


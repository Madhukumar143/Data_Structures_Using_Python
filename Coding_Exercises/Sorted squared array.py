''' Question ->
You are given an array of Integers in which each subsequent value is not less than the previous value.
Write a function that takes this array as an input and returns a new array with the squares of each number
sorted in ascending order.'''


def sorted_squared(array):
    # write code here.make sure to return desired array
    '''op=[0] * len(array)
    for i in range(0,len(array)):
        op[i] = array[i] * array[i]
    op.sort()'''
    # two pionter technique
    i, j = 0, len(array) - 1
    op = [0] * len(array)

    for k in reversed(range(len(array))):
        if array[i] ** 2 > array[j] ** 2:
            op[k] = array[i] ** 2
            i += 1
        else:
            op[k] = array[j] ** 2
            j -= 1

    return op


a = [-4, -4, -3, -1, 0, 1, 3, 3, 4]
b = sorted_squared(a)
print(b)
'''Coding Exercise: Monotonic Array
Question :
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array is monotone increasing if all its elements from left to right are non-decreasing.
An array is monotone decreasing if all  its elements from left to right are non-increasing.
Given an integer array return true if the given array is monotonic, or false otherwise.'''


'''def monotonic_array(array):
    # write code here
    if array[-1] < array[0]:# if array is decreasing convert it to increasing
        array.reverse()
    for k in range(len(array) - 1):# check for the array to be non increasing
        if array[k] > array[k + 1]:
            return False
    return True

b = monotonic_array([12, 11, 9, 7, 6, 5, 6, 5, 4, 4, 3, 3, 2, 2, 0])
print(b)'''

def monotone(arr):
    inc = True #initially assume arrays as monotones
    dec = True #initially assume arrays as monotones

    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            inc = False

        if not(arr[i]>= arr[i+1]): # or (arr[i] < arr[i+1])
            dec = False

    return inc or dec

b = monotone([12, 12, 9, 7, 6, 5, 5, 5, 4, 4, 3, 3, 2, 2, 0])
print(b)
"""We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row,
we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110. Given two integer n and k,
return the kth (1-indexed) symbol in the nth row of a table of n rows."""

def kth_symbol(n, k):
    #write your code here
    if n==1: return 0
    len = 2**(n-1)
    mid = len//2
    if k<=mid:
        return kth_symbol(n-1,k) #if k is in first half we will return directly
    else:
        return 1-(kth_symbol(n-1,k-mid)) #if k is in second half we will return not of value

res = kth_symbol(4,7)
print(res)
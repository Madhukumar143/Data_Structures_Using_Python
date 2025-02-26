"""Coding Exercise: Subsets 2
Given an integer array nums that may contain duplicates, return all possible
subsets
(the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example : 

nums = [1,3,3]
Output =
[ [], [1], [3], [1,3], [3,3], [1,3,3]]"""

def subsetsWithDup(nums):
    #write code here
    res = []
    def helper(i,curr):
        if i == len(nums):
            res.append(curr[:])
            return
        #include
        curr.append(nums[i])
        helper(i+1,curr)
        curr.pop()
        #exclude
        while i<len(nums)-1 and nums[i]==nums[i+1]:
            i+=1 
        helper(i+1,curr)
    helper(0,[])
    return res

print(subsetsWithDup([1,2,2]))
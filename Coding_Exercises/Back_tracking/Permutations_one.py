"""Coding Exercise ( Permutations)
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
Example 1:
nums = [1,4]
Output :[[1,4],[4,1]]
Example 2:
nums = [1,4,5]
Output :[[1,4,5],[1,5,4],[4,1,5],[4,5,1],[5,1,4],[5,4,1]]
"""

def perm(nums):
    n = len(nums)
    res = []
    def helper(ind):
        if ind == n-1 :
            res.append(nums[:])
        
        for j in range(ind,n):
            nums[ind],nums[j] = nums[j],nums[ind]
            helper(ind+1)
            nums[ind],nums[j] = nums[j],nums[ind]
    helper(0)
    return res

print(perm([1,2,3]))
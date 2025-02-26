"""Permutations 2
Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.
Example:
nums = [3,3,2]
Output :
[[3,3,2] , [3,2,3], [2,3,3] ]"""

def permuteUnique(nums):
    #write code here
    res = []
    
    def help(i):
        if i == len(nums)-1:
            res.append(nums[:])
            return
        
        #Recursive case 
        hash = {}
        for j in range(i,len(nums)):
            if nums[j] not in hash:
                hash[nums[j]] = True
                nums[i],nums[j] = nums[j],nums[i]
                help(i+1)
                nums[i],nums[j] = nums[j],nums[i]
        
    help(0)
    return res
        

print(permuteUnique([1,1,3]))
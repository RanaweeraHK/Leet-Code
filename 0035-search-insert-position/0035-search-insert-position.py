class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if (nums[i]>=target):
                    return i 
            return (i+1)    
                    
                    
                    
            
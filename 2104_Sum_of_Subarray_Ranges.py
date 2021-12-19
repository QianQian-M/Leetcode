class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        
        dp= [0]*len(nums)
        s=0
        for idx,num in enumerate(nums):
            
            min_value = nums[idx]
            max_value = float("-inf")
            for i in range(idx,len(nums)):

                if nums[i] > max_value:
                    max_value = nums[i]
                elif nums[i] < min_value:
                    min_value = nums[i]

                dp[i]=max_value-min_value
       
            s+=sum(dp)
        return s
 
 # Follow-up ----> O(n)?
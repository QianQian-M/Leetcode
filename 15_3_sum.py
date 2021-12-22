class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:return []
        res =[]
       
        nums = sorted(nums)
        
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            
            if i >=1 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1
            while l < r:
                s = nums[i]+nums[l]+nums[r]
                
#                 if s==0:
#                     res.append([nums[i],nums[l],nums[r]])
                    
                if l > i+1 and nums[l] ==nums[l-1] or s< 0:
                    l+=1
                elif r < len(nums)-1 and nums[r] == nums[r+1] or s>0:
                    r-=1
                elif s == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    
        return res
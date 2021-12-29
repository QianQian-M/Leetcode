# Solution from discussion

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        # a stack with monotonic decreasing
        monotonic_stack = []
        
        # dictionary:
        # key: number
        # value: next greater number of key
        dict_of_greater_number = {}

        # ----------------------------------------------
        
        # launch linear scan to build dict_of_greater_number
        for cur_number in nums2:
            
            # maintain a monotonic decreasing stack
            while monotonic_stack and cur_number > monotonic_stack[-1]:
                
                pop_out_number = monotonic_stack.pop()
                
                # next greater number of pop_out_number is cur_number
                dict_of_greater_number[pop_out_number] = cur_number
            
            monotonic_stack.append(cur_number)
        # ----------------------------------------------
        
        # solution output
        next_greater_element = []
        
        # get next greater element by dictionary
        for x in nums1:
            
            if x in dict_of_greater_number:
                next_greater_element.append( dict_of_greater_number[x] )
                
            else:
                next_greater_element.append(-1)
                
        return next_greater_element

# solution for O(n) ,n is nums2 array size
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        d = {}
        
        for i in range(len(nums2)):
            while stack and nums2[i] >stack[-1]:
                ele = stack.pop()
                d[ele] = nums2[i]
            
            stack.append(nums2[i])
        
        ans = [-1]*len(nums1)
        
        for i in range(len(nums1)):
            if nums1[i] in d:
                ans[i]=d[nums1[i]]
        
        return ans
        
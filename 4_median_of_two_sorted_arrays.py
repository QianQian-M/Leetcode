class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        total_len = len(nums1)+len(nums2)
        A,B = nums1,nums2
        med = total_len//2
        
        if len(A) > len(B):
            A,B=B,A
        
        # time complexity O(log(min(n)))
        l,r=0,len(A)-1
        while True:
            i = l+(r-l)//2
            j = med-i-2
            
            Aleft=A[i] if i>=0 else float('-infinity')
            Aright= A[i+1] if i < len(A)-1 else float('infinity')
            Bleft=B[j] if j>=0 else float('-infinity')
            Bright=B[j+1] if j < len(B)-1 else float('infinity')
            
            if Aleft <=Bright and Bleft <=Aright:
                if total_len%2:
                    return min(Aright,Bright)
                return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft > Bright:
                r=i-1
            else:
                l=i+1
                
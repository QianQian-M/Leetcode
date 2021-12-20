class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_val = 10**7
        res = []
        arr = sorted(arr)

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if diff < min_val:
                res = []
                res.append([arr[i-1], arr[i]])
                min_val = diff
            elif diff == min_val:
                res.append([arr[i-1], arr[i]])

        return res
                
            
        
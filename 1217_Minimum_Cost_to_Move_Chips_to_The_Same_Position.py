
'''
If moving all position to the even position, which means the cost is 0, so the greedy
method will first check the if the position can be moved during the even number. Odd
position will always have 1 cost if they want to move to same position as the even number.
'''

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even_cnt = 0
        odd_cnt = 0
        for i in position:
            if i % 2 == 0:
                even_cnt += 1
            else:
                odd_cnt += 1
        return min(even_cnt, odd_cnt)
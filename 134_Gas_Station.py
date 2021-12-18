class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        

        if sum(gas) < sum(cost): 
            return -1
        n, start, a = len(gas), 0, 0
        for i in range(n):
            a += gas[i] - cost[i]
            if a < 0:
                start, a = i+1, 0
        return start
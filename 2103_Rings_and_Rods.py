class Solution:
    def countPoints(self, rings: str) -> int:
        
        ans = 0
        import collections
        visited = set()
        d = collections.defaultdict(set)
        for i in range(1,len(rings),2):
            
            d[rings[i]].add(rings[i-1])
            if len(d[rings[i]]) == 3 and rings[i] not in visited:
                ans+=1
                visited.add(rings[i])
        
    
        return ans

# discussion: bit mask???
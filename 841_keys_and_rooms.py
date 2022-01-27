class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # BFS
        key = rooms[0]
        q=deque(key)
      
        visited = set()
    
        while q:
            
            key = q.popleft()
            visited.add(key)
            
            for ele in rooms[key]:
                if ele not in visited:
                    q.append(ele)
                    
                    
        
        for i in range(1,len(rooms)):
            if i not in visited:
                return False
        
        return True
        
            
      
        
  

            
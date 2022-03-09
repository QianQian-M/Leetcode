class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # using dictionary to store edges and list to store indegree
         edges = {i:[] for i in range(numCourses)}
         indegree = [0 for i in range(numCourses)]
         
        
         for i,j in prerequisites:
                edges[j].append(i)
                indegree[i]+=1

         print(edges,indegree)
        
         queue ,count = deque([]),0
         
         res =[]
         # topological sort can always find one input with 0 degree.
         for i in range(numCourses):
                if indegree[i] == 0:
                    # the first element in the final res
                    res.append(i)
                    # put the first element in queue
                    queue.append(i)
         while queue:
            node = queue.popleft()
            count+=1
            
            # check other prerequisite course for the current node            
            for x in edges[node]:
                indegree[x] -=1
                if indegree[x] == 0:
                    queue.append(x)
                    res.append(x)
         # the case with a cycle
         #  3 [[1,0],[1,2],[0,1]]   the len(res) == 1, only has the 2, because the 0 and 1 is a cycle    
         return res if len(res) == numCourses else []
        
        
        
        
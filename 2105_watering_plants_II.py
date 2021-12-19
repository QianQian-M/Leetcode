class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        l = 0 
        r = len(plants)-1
        remain_A = capacityA
        remain_B = capacityB
        s=0
        while r >= l:
            
            if r == l:
                
                if remain_A== remain_B and remain_A <plants[l]:
                    s+=1
                elif max(remain_A,remain_B) < plants[l]:
                    s+=1
                    
                return s
                    
            
            remain_A = remain_A-plants[l]
            remain_B = remain_B-plants[r]
            
            if remain_A < 0:
                s+=1
                remain_A = capacityA-plants[l]
            if remain_B < 0:
                s+=1
                remain_B = capacityB-plants[r]
            
            l+=1
            r-=1
                
           
        return s
     
            
         
            
          
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import collections
        row = collections.defaultdict(list)
        col = collections.defaultdict(list)
        square = collections.defaultdict(list)
      
        
        for i in range(len(board)):
            
            for j in range(len(board[0])):
                
                if board[i][j] != "." and board[i][j] in row[i]:
                    return False
                
                if board[i][j] !="." and board[i][j] in col[j]:
                    return False
                
                col[j].append(board[i][j])
                
                row[i].append(board[i][j])
                
                idx = (i//3)*3+j//3
                if board[i][j] != "." and board[i][j] in square[idx]:
                    return False
                
                square[idx].append(board[i][j])
       
                    
                
                
        return True
        
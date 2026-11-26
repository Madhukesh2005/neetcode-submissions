class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen=set()
            for c in range(9):
                if board[r][c]==".":
                    continue
                else:
                    if board[r][c] in seen:
                        return False
                    else:
                        seen.add(board[r][c])
        
        for c in range(9):
            seen=set()
            for r in range(9):
                if board[r][c]==".":
                    continue
                else:
                    if board[r][c] in seen:
                        return False
                    else:
                        seen.add(board[r][c])
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                seen=set()
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        if board[r][c]==".":
                            continue
                        else:
                            if board[r][c] in seen:
                                return False
                            else:
                                seen.add(board[r][c])
        
        return True


            
        

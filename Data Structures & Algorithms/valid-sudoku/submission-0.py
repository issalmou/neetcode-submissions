class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ligne={}
        colonne={}
        square={} #keys sont l//3,c//3 
        n=len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j] != '.':
                    ligne.setdefault(i,[])
                    colonne.setdefault(j,[])
                    square.setdefault((i//3,j//3),[])
                    if (int(board[i][j])<1 or int(board[i][j])>9 or board[i][j] in ligne[i] 
                        or board[i][j] in colonne[j] or board[i][j] in square[(i//3,j//3)]):
                        return False
                    else:
                        ligne[i].append(board[i][j])
                        colonne[j].append(board[i][j])
                        square[(i//3,j//3)].append(board[i][j])
        return True 


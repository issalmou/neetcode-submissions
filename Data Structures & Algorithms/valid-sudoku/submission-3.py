class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ligne={}
        colonne={}
        square={} #keys sont l//3,c//3 
        for i in range(9):
            for j in range(9):
                val=board[i][j]
                if val != '.':
                    ligne.setdefault(i,[])
                    colonne.setdefault(j,[])
                    square.setdefault((i//3,j//3),[])
                    if (val in ligne[i] or val in colonne[j] or val in square[(i//3,j//3)]):
                        return False
                    else:
                        ligne[i].append(val)
                        colonne[j].append(val)
                        square[(i//3,j//3)].append(val)
        return True 


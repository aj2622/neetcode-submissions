class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def check_squares():
            for i in (0,3,6):
                for j in (0,3,6):
                    l = []
                    s = set()
                    for _i in range(3):
                        for _j in range(3):
                            if board[i + _i][j + _j] != ".":
                                l.append(board[i + _i][j + _j])
                                s.add(board[i + _i][j + _j])
                    if len(s) != len(l):
                        print(len(s), len(l))
                        return False
            return True
            
        if not check_squares():
            return False

        for i in range(9):
            l = []
            s = set()
            for j in range(9):
                if board[i][j] != ".":
                    l.append(board[i][j])
                    s.add(board[i][j])
            if len(s) != len(l):
                return False
            l = []
            s = set()
            for j in range(9):
                if board[j][i] != ".":
                    l.append(board[j][i])
                    s.add(board[j][i])
            if len(s) != len(l):
                return False            

        return True
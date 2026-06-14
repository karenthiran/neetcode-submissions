class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            st=set()
            for j in i:
                if j!='.' and j in st:
                    return False
                st.add(j)
        for j in range(9):
            st=set()
            for i in range(9):
                if board[i][j]!='.' and board[i][j] in st:
                    return False
                st.add(board[i][j])
        
        for n in range(0,9,3):
            for m in range(0,9,3):
                st=set()
                for i in range(n,n+3):
                    for j in range(m,m+3):
                        if board[i][j]!='.' and board[i][j] in st:
                            return False
                        st.add(board[i][j])
        return True
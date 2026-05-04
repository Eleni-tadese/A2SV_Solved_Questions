class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(board), len(board[0])

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols
        
        def dfs(row, col):
            board[row][col] = 'Y'

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if inbound(nr, nc) and board[nr][nc] == 'O':
                    dfs(nr, nc)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O' and (row == 0 or col == 0 or row == rows - 1 or col == cols - 1):
                    dfs(row, col)
        
        print(board)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'Y':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'
                    

        
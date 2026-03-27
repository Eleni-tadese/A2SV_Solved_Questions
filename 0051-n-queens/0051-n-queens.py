class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        cols = set()       # columns already occupied
        posDiag = set()    # positive diagonals (row - col)
        negDiag = set()    # negative diagonals (row + col)

            # to avoid conflict 
                # we need to remember:
                    # Which columns are already used
                    # Which diagonals are already used

                # so
                    # Try all columns
                    # Skip invalid ones that already used
                    # Go deeper if safe 
                    # Undo (backtrack)

                # cols: columns already occupied by a queen
                # posDiag: positive diagonals already occupied (row - col)
                # negDiag: negative diagonals already occupied (row + col)


        solutions = [] # This will store all valid
        def backtrack(row, board):
            if row == n:
                 # if  all rows are filled is our base case
                solutions.append(board[:])
                return
         
            for col in range(n):
                    # Check if this column or diagonals are under attack
                if col in cols or (row - col) in posDiag or (row + col) in negDiag:
                    continue

                    # else we have to  Place queen
                cols.add(col)
                posDiag.add(row - col)
                negDiag.add(row + col)

                    # Update board with queen in this row
                newRow = '.' * col + 'Q' + '.' * (n - col - 1)

                    # Recursive call to place queen in next row
                backtrack(row + 1, board + [newRow])
                    # Backtrack: remove queen   
                cols.remove(col)
                posDiag.remove(row - col)
                negDiag.remove(row + col)
        
        backtrack(0, [])
            
        # Return all valid board
        return solutions
            

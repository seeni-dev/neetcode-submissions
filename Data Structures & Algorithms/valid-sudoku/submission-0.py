class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = {i: {} for i in range(9)}
        column_hash = {i: {} for i in range(9)}
        quadrant_hash = {}
        for i in range(3):
            quadrant_hash[i] = {}
            for j in range(3):
                quadrant_hash[i][j] = {}
        
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == ".":
                    continue
                if cell in row_hash[i]:
                    return False
                if cell in column_hash[j]:
                    return False
                qi = i // 3
                qj = j // 3
                if cell in quadrant_hash[qi][qj]:
                    return False
                row_hash[i][cell] = True
                column_hash[j][cell] = True
                quadrant_hash[qi][qj][cell] = True
        return True
        
class Solution:
    dirs = [
        [0,1],
        [0, -1],
        [1, 0],
        [-1, 0]
    ]
    def solve(self, board: List[List[str]]) -> None:
        for x in [0, len(board)-1]:
            for y in range(0, len(board[0])):
                self.dfs(board, x, y, 'T')
        for x in range(0, len(board)):
            for y in [0, len(board[0])-1]:
                self.dfs(board, x, y, 'T')

        for x  in range(0, len(board)):
            for y in range(0, len(board[x])):
                if board[x][y] == 'T':
                    board[x][y] = 'O'
                elif board[x][y] == 'O':
                    board[x][y] = 'X'
        return
    
    def dfs(self, board: List[List[str]], x: int, y: int, marker: str) -> None:
        if x not in range(0, len(board)):
            return
        if y not in range(0, len(board[x])):
            return
        if board[x][y] != 'O':
            return
        board[x][y] = marker

        for d in self.dirs:
            nx, ny = x +d[0], y+d[1]
            self.dfs(board, nx, ny, marker)
        return
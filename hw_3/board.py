class Board:
    def __init__(self) -> None:
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
    
    def display(self) -> None:
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
    
    def is_full(self) -> bool:
        for row in self.board:
            if ' ' in row:
                return False
        return True
    
    def is_winner(self, player: str) -> bool:
        # Проверка строк
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        
        # Проверка столбцов
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        
        # Проверка диагоналей
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True
        
        return False

    def make_move(self, row: int, col: int, player: str) -> bool:
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False
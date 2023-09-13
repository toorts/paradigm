class Player:
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol
    
    def make_move(self) -> tuple[int, int]:
        row = int(input(f'Введите номер строки (0, 1, 2) для {self.symbol}: '))
        col = int(input(f'Введите номер столбца (0, 1, 2) для {self.symbol}: '))
        return row, col
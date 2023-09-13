from board import Board
from player import Player


def play_game() -> None:
    board = Board()
    player1 = Player('X')
    player2 = Player('O')
    current_player = player1

    while True:
        board.display()
        row, col = current_player.make_move()
        if board.make_move(row, col, current_player.symbol):
            if board.is_winner(current_player.symbol):
                board.display()
                print(f'Игрок {current_player.symbol} выиграл!')
                break
            elif board.is_full():
                board.display()
                print('Ничья!')
                break
            current_player = player2 if current_player == player1 else player1


if __name__ == '__main__':
    play_game()

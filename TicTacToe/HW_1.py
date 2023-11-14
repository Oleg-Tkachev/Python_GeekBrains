
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def print_board(self):
        print(f'''
         {self.board[0]} | {self.board[1]} | {self.board[2]}
        -----------
         {self.board[3]} | {self.board[4]} | {self.board[5]}
        -----------
         {self.board[6]} | {self.board[7]} | {self.board[8]}
        ''')

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.print_board()
            if self.check_winner():
                print(f'{self.current_player} Победа!')
                exit()
            elif all(cell != ' ' for cell in self.board):
                print('Победила дружба!')
                exit()
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print('Неверный ход! Ячейка уже занята.')

    def check_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]  # diagonals
        ]

        for condition in win_conditions:
            a, b, c = condition
            if self.board[a] != ' ' and self.board[a] == self.board[b] == self.board[c]:
                return True
        return False

game = TicTacToe()
game.print_board()
print('Давайте поиграем в крестики-нолики!')

while True:
    try:
        position = int(input('Выберите позицию на доске (0-8): '))
        if position < 0 or position > 8:
            print('Неверный ход! Введите число от 0 до 8.')
            continue
        game.make_move(position)
    except ValueError:
        print('Неверный ход! Введите число от 0 до 8.')
        

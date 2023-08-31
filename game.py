from typing import List

class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = None
        self.winner = None
        self.draw = False

    def start(self):
        self.current_player = Player('X')
        self.play_game()

    def play_game(self):
        while not self.winner and not self.draw:
            self.display_board()
            self.get_move()
            self.make_move()
            if self.check_win():
                self.winner = self.current_player
            elif self.check_draw():
                self.draw = True
            else:
                self.switch_players()

        self.display_board()
        if self.winner:
            print(f"Player {self.winner.mark} wins!")
        else:
            print("It's a draw!")

    def display_board(self):
        print("---------")
        for row in self.board:
            print('|', end='')
            for cell in row:
                print(f' {cell} |', end='')
            print("\n---------")

    def get_move(self):
        valid_move = False
        while not valid_move:
            try:
                row = int(input("Enter the row number (0-2): "))
                col = int(input("Enter the column number (0-2): "))
                if 0 <= row <= 2 and 0 <= col <= 2 and self.board[row][col] == ' ':
                    valid_move = True
                else:
                    print("Invalid move. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        self.current_player.move = (row, col)

    def make_move(self):
        row, col = self.current_player.move
        self.board[row][col] = self.current_player.mark

    def check_win(self):
        mark = self.current_player.mark
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == mark:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == mark:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == mark:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == mark:
            return True
        return False

    def check_draw(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def switch_players(self):
        self.current_player = Player('O') if self.current_player.mark == 'X' else Player('X')


class Player:
    def __init__(self, mark):
        self.mark = mark
        self.move = None

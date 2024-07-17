import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.buttons = []

        self.create_board()

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.window, text=" ", font='normal 20 bold', height=3, width=6,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def on_button_click(self, index):
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            winning_combination = self.check_win(self.current_player)
            if winning_combination:
                for i in winning_combination:
                    self.buttons[i].config(fg="red")
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.window.destroy()
            elif self.check_tie():
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                self.window.destroy()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return condition
        return None

    def check_tie(self):
        return all(cell != " " for cell in self.board)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()

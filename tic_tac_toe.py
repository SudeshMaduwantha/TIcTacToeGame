import tkinter as tk
from tkinter import messagebox
import os

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.geometry("400x450+500+200")  # Increased window size and centered
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.load_scores()
        self.buttons = []
        self.create_widgets()
        self.show_loading_screen()

    def load_scores(self):
        if os.path.exists("scores.txt"):
            with open("scores.txt", "r") as file:
                scores = file.read().split(",")
                self.player1_score = int(scores[0])
                self.player2_score = int(scores[1])
        else:
            self.player1_score = 0
            self.player2_score = 0

    def save_scores(self):
        with open("scores.txt", "w") as file:
            file.write(f"{self.player1_score},{self.player2_score}")

    def clear_scores(self):
        self.player1_score = 0
        self.player2_score = 0
        self.save_scores()
        self.score_label.config(text=f"Player 1: {self.player1_score} | Player 2: {self.player2_score}")

    def show_loading_screen(self):
        self.loading_label = tk.Label(self.window, text="Loading Tic-Tac-Toe...", font='normal 20 bold')
        self.loading_label.pack(expand=True)
        self.window.after(2000, self.start_game)  # Show loading screen for 2 seconds

    def start_game(self):
        self.loading_label.destroy()
        self.create_board()

    def create_widgets(self):
        self.footer = tk.Label(self.window, text="Game By Sudesh Maduwantha", font='normal 10')
        self.footer.pack(side="bottom")
        
        button_frame = tk.Frame(self.window)
        button_frame.pack(side="bottom")
        
        self.new_game_button = tk.Button(button_frame, text="New Game",bg="blue",foreground="white", command=self.new_game)
        self.new_game_button.pack(side="left", padx=5)
        
        self.clear_score_button = tk.Button(button_frame, text="Clear Scores",bg="orange",foreground="black", command=self.clear_scores)
        self.clear_score_button.pack(side="left", padx=5)
        
        self.score_label = tk.Label(self.window, text=f"Player 1: {self.player1_score} | Player 2: {self.player2_score}", font='normal 10')
        self.score_label.pack(side="bottom")

    def create_board(self):
        frame = tk.Frame(self.window)
        frame.pack()
        for i in range(9):
            button = tk.Button(frame, text=" ", font='normal 20 bold', height=3, width=6,
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
                self.update_score()
                self.save_scores()
                self.reset_board()
            elif self.check_tie():
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def update_score(self):
        if self.current_player == "X":
            self.player1_score += 1
        else:
            self.player2_score += 1
        self.score_label.config(text=f"Player 1: {self.player1_score} | Player 2: {self.player2_score}")

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

    def reset_board(self):
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ", fg="black")

    def new_game(self):
        self.window.destroy()
        self.__init__()
        self.run()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()

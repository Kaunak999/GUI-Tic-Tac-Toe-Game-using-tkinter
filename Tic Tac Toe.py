import tkinter as tk
from tkinter import messagebox

# Create the main game class
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        
        # Initialize a 3x3 grid of buttons
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    # Function to create the board
    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=('Arial', 20), width=5, height=2,
                                   command=lambda row=row, col=col: self.on_click(row, col))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    # Function to handle button clicks
    def on_click(self, row, col):
        if self.buttons[row][col]["text"] == "":
            self.buttons[row][col]["text"] = self.current_player
            if self.check_winner(self.current_player):
                self.show_winner(self.current_player)
            elif self.check_tie():
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_board()
            else:
                self.switch_player()

    # Function to switch players
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    # Function to check for a win
    def check_winner(self, player):
        # Check rows, columns, and diagonals
        for row in self.buttons:
            if all(button["text"] == player for button in row):
                return True
        for col in range(3):
            if all(self.buttons[row][col]["text"] == player for row in range(3)):
                return True
        if all(self.buttons[i][i]["text"] == player for i in range(3)) or all(self.buttons[i][2 - i]["text"] == player for i in range(3)):
            return True
        return False

    # Function to check for a tie
    def check_tie(self):
        return all(button["text"] != "" for row in self.buttons for button in row)

    # Function to display the winner and reset the game
    def show_winner(self, player):
        messagebox.showinfo("Tic Tac Toe", f"Player {player} wins!")
        self.reset_board()

    # Function to reset the board for a new game
    def reset_board(self):
        for row in self.buttons:
            for button in row:
                button["text"] = ""
        self.current_player = "X"

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

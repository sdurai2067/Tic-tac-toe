import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Game XO")
        self.master.resizable(False, False)
        self.master.configure(bg="light blue")  # Set background color to light blue

        # Initialize player scores
        self.playerX_score = 0
        self.playerO_score = 0

        # Title Label
        self.title_label = tk.Label(self.master, text="Game XO", font=("Helvetica", 16), bg="light blue")
        self.title_label.pack(pady=10)

        # Logo Image (Circle/Oval with black border)
        self.logo_image = Image.open(r"C:\Users\Admin\Documents\tic-tac-toe\xo logo.png")
        self.logo_image = self.logo_image.resize((60, 40), Image.BILINEAR)
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(self.master, image=self.logo_photo, bg="light blue", borderwidth=2, relief="solid")
        self.logo_label.pack()

        # Canvas for game board
        self.canvas = tk.Canvas(self.master, width=300, height=300, bg="white")
        self.canvas.pack(pady=10)

        # Player scores
        self.player_scores_label = tk.Label(self.master, text="PLAYER X SCORE: 0   PLAYER O SCORE: 0", font=("Helvetica", 12), bg="light blue")
        self.player_scores_label.pack()

        # Frame for option buttons
        self.options_frame = tk.Frame(self.master, bg="light blue")
        self.options_frame.pack(pady=5)

        # Restart button
        self.restart_button = tk.Button(self.options_frame, text="RESTART", command=self.restart)
        self.restart_button.pack(side=tk.LEFT, padx=5)

        # Continue button
        self.continue_button = tk.Button(self.options_frame, text="CONTINUE", command=self.try_next)
        self.continue_button.pack(side=tk.LEFT, padx=5)

        # Draw the Tic Tac Toe board
        self.draw_board()

        # Initialize the game
        self.initialize_game()

    def draw_board(self):
        self.canvas.create_line(100, 0, 100, 300, fill="black", width=3)
        self.canvas.create_line(200, 0, 200, 300, fill="black", width=3)
        self.canvas.create_line(0, 100, 300, 100, fill="black", width=3)
        self.canvas.create_line(0, 200, 300, 200, fill="black", width=3)

    def initialize_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.canvas.bind("<Button-1>", self.click_handler)

    def click_handler(self, event):
        if self.check_winner() is None:
            x = event.x // 100
            y = event.y // 100

            if self.board[y][x] == "":
                self.board[y][x] = self.current_player
                self.draw_move(x, y, self.current_player)
                winner = self.check_winner()
                if winner:
                    if winner == "X":
                        self.playerX_score += 1
                    else:
                        self.playerO_score += 1
                    self.update_scores()
                    self.initialize_game()
                elif self.check_draw():
                    self.initialize_game()
                else:
                    self.current_player = "O" if self.current_player == "X" else "X"

    def draw_move(self, x, y, player):
        color = "orange" if player == "X" else "black"
        self.canvas.create_text(x * 100 + 50, y * 100 + 50, text=player, font=("Helvetica", 40), fill=color, tags=f"{x}_{y}")

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return self.board[0][2]
        return None

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def update_scores(self):
        self.player_scores_label.config(text=f"PLAYER X SCORE: {self.playerX_score}   PLAYER O SCORE: {self.playerO_score}")

    def restart(self):
        self.playerX_score = 0
        self.playerO_score = 0
        self.update_scores()
        self.reset_board()

    def try_next(self):
        self.reset_board()

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""
                self.canvas.delete(f"{i}_{j}")
        self.current_player = "X"

def main():
    root = tk.Tk()
    root.configure(bg="light blue")  # Set background color to light blue
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()

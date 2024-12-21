import tkinter as tk
from tkinter import messagebox

def reset_game():
    global current_player, game_over, moves, score_x, score_o
    current_player = "X"
    moves = 0
    game_over = False
    for row in buttons:
        for btn in row:
            btn.config(text="")

    if score_x >= 3 or score_o >= 3:
        if score_x > score_o:
            messagebox.showinfo("Игра окончена", "Игрок X победил в серии!")
        else:
            messagebox.showinfo("Игра окончена", "Игрок O победил в серии!")
        score_x = 0
        score_o = 0
        update_score()

def update_score():
    score_label.config(text=f"X: {score_x} | O: {score_o}")

def check_draw():
    global game_over
    if moves == 9 and not game_over:
        messagebox.showinfo("Ничья", "Игра завершилась ничьей!")
        game_over = True
        reset_game()

def check_winner():
    global game_over, score_x, score_o
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False

def on_click(row, col):
    global current_player, moves, game_over, score_x, score_o

    if buttons[row][col]['text'] != "" or game_over:
        return

    buttons[row][col]['text'] = current_player
    moves += 1

    if check_winner():
        game_over = True
        if current_player == "X":
            score_x += 1
        else:
            score_o += 1
        update_score()
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
        if score_x < 3 and score_o < 3:
            reset_game()
        return

    check_draw()

    current_player = "O" if current_player == "X" else "X"

def set_player(choice):
    global current_player
    current_player = choice
    for btn in player_choice_buttons:
        btn.config(state=tk.DISABLED)

# Настройки окна
window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x400")

current_player = "X"
game_over = False
moves = 0
score_x = 0
score_o = 0

buttons = []

# Поле для игры
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2, command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

# Кнопка сброса
reset_button = tk.Button(window, text="Сброс", font=("Arial", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

# Счетчик побед
score_label = tk.Label(window, text=f"X: {score_x} | O: {score_o}", font=("Arial", 14))
score_label.grid(row=4, column=0, columnspan=3)

# Выбор игрока
player_choice_buttons = []
player_label = tk.Label(window, text="Выберите игрока: X или O", font=("Arial", 12))
player_label.grid(row=5, column=0, columnspan=3)

for choice in ["X", "O"]:
    btn = tk.Button(window, text=choice, font=("Arial", 14), command=lambda c=choice: set_player(c))
    btn.grid(row=6, column=["X", "O"].index(choice))
    player_choice_buttons.append(btn)

window.mainloop()

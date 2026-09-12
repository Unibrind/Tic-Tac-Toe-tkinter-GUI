import tkinter as tk

window = tk.Tk()

window.title("Tic-Tac-Toe")
window.geometry("600x650")
window.configure(bg="#1e1e2e")

current_player = "X"
game_over = False

title_label = tk.Label(
    window,
    text="Tic-Tac-Toe",
    font=("Arial", 28, "bold"),
    fg="white",
    bg="#1e1e2e"
)

title_label.grid(row=0, column=0, columnspan=3, pady=5)


turn_label = tk.Label(
    window,
    text="X's turn",
    font=("Arial", 16, "bold"),
    fg="#89b4fa",
    bg="#1e1e2e"
)

turn_label.grid(row=1, column=0, columnspan=3)


winner_label = tk.Label(
    window,
    text="",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#1e1e2e",
    padx=10,
    pady=5
)

winner_label.grid(row=5, column=0, columnspan=3)


def check_winner():
    # Vérifier les lignes
    for row in range(3):
        if (
            buttons[row * 3]["text"] != ""
            and buttons[row * 3]["text"]
            == buttons[row * 3 + 1]["text"]
            == buttons[row * 3 + 2]["text"]
        ):
            return [row * 3, row * 3 + 1, row * 3 + 2]

    # Vérifier les colonnes
    for column in range(3):
        if (
            buttons[column]["text"] != ""
            and buttons[column]["text"]
            == buttons[column + 3]["text"]
            == buttons[column + 6]["text"]
        ):
            return [column, column + 3, column + 6]

    # Vérifier la première diagonale
    if (
        buttons[0]["text"] != ""
        and buttons[0]["text"]
        == buttons[4]["text"]
        == buttons[8]["text"]
    ):
        return [0, 4, 8]

    # Vérifier la deuxième diagonale
    if (
        buttons[2]["text"] != ""
        and buttons[2]["text"]
        == buttons[4]["text"]
        == buttons[6]["text"]
    ):
        return [2, 4, 6]

    return None


def check_draw():
    for button in buttons:
        if button["text"] == "":
            return False

    return True


def restart_game():
    global current_player, game_over

    current_player = "X"
    game_over = False

    for button in buttons:
        button["text"] = ""
        button["fg"] = "black"
        button["bg"] = original_button_color

    winner_label["text"] = ""
    turn_label["text"] = "X's turn"


def button_click(button):
    global current_player, game_over

    if game_over:
        return

    if button["text"] == "":
        button["text"] = current_player

        if current_player == "X":
            button["fg"] = "#89b4fa"
        else:
            button["fg"] = "#f38ba8"

        winning_buttons = check_winner()

        if winning_buttons:
            winner_label["text"] = f"{current_player} wins!"

            if current_player == "X":
                winner_label["fg"] = "#89b4fa"
                winning_color = "#45475a"
            else:
                winner_label["fg"] = "#f38ba8"
                winning_color = "#45475a"

            for index in winning_buttons:
                buttons[index]["bg"] = winning_color

            turn_label["text"] = ""
            game_over = True
            return

        if check_draw():
            winner_label["text"] = "Draw!"
            winner_label["fg"] = "white"
            turn_label["text"] = ""
            game_over = True
            return

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

        turn_label["text"] = f"{current_player}'s turn"


for row in range(7):
    window.grid_rowconfigure(row, weight=1)

for column in range(3):
    window.grid_columnconfigure(column, weight=1)


buttons = []
original_button_color = None


for row in range(3):
    for column in range(3):
        button = tk.Button(
            window,
            text="",
            font=("Arial", 40, "bold"),
            relief="flat",
            borderwidth=0,
            bg="#313244",
            fg="white",
            activebackground="#45475a"
        )

        if original_button_color is None:
            original_button_color = button["bg"]

        buttons.append(button)

        button.config(command=lambda b=button: button_click(b))

        button.grid(row=row + 2, column=column, sticky="nsew")


restart_button = tk.Button(
    window,
    text="Play Again",
    font=("Arial", 16, "bold"),
    relief="raised",
    borderwidth=3,
    padx=20,
    pady=5,
    command=restart_game
)

restart_button.grid(row=6, column=0, columnspan=3)


window.mainloop()
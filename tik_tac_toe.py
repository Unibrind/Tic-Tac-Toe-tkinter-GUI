import os

def display_game(game_list):#affiche le jeux
    print(game_list["1"], "|", game_list["2"], "|", game_list["3"])
    print("—————————————")
    print(game_list["4"], "|", game_list["5"], "|", game_list["6"])
    print("—————————————")
    print(game_list["7"], "|", game_list["8"], "|", game_list["9"])
    print(" ")

def caracter_choice():  # choose character X or O
    player1 = ""
    player2 = ""
    
    x = "✖️ "
    o = "⭕"
    
    while True:
        choice = input("Pick a character you want to play between (X or O): ").upper()
        print(" ")

        if choice not in ["X", "O"]:
            print("Please answer only with (X or O).")
            print(" ")
            continue

        if choice == "X":
            player1 = x
            player2 = o
        else:
            player1 = o
            player2 = x

        print("Player 1 =", player1, " and Player 2 =", player2)
        print(" ")

        return player1, player2

def position_choice(game_list):#index
    while True:
        choice = input("Choose a position where you want to place your character: ")
        if not choice.isdigit():
            print("Please answer with a number.")
            continue
        
        if choice not in game_list.keys():
            print("")
            print("Out of range! Please enter a number between 1 and 9.")
            continue
        
        if not game_list[choice].isdigit():
            print("")
            print("You can't do that! This position is already taken.")
            continue
        
        return choice

def update_game(game_list, position, caracter):#update dic
    game_list.update({position: caracter})
    return game_list

def winner(game_list, player):#define winner :gagnat = True or ya pas de gagant = False
    list_win = [("7", "8", "9"),#Top   horizental
                ("4", "5", "6"),#mid   horizental
                ("1", "2", "3"),#bot   horizental
                ("1", "4", "7"),#right vertical
                ("2", "5", "8"),#mid   vertical
                ("3", "6", "9"),#left  vertical
                ("1", "5", "9"),#diagonal
                ("7", "5", "3")]#diagonal
    
    for x in list_win:
        if game_list[x[0]] == game_list[x[1]] == game_list[x[2]] == player:
            return True
    return False

def game_on_choice():#asking if wana play again True or False
    choice = 'wrong'
    while choice not in ['Y','N']:
        choice = input("Would you like to keep playing? Y or N: ").upper()
        if choice not in ['Y','N']:
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")
            
    if choice == "Y":
        return True
    else:
        return False

def digit_check(game_list, position):
    return game_list[position].isdigit()

def tie(game_list):
    for x in game_list:
        if digit_check(game_list, x):
            return False
        
    return True

print("""
        ✖️ ⭕ --Welcome to TIC TAC TOE game--✖️ ⭕
                
✖️ ⭕ The first player to line up 3 identical characters wins the game!✖️ ⭕

There is the grind that you'll be playing on:
""")

game_on = True
while game_on:
    game_list = {"1":"1", "2":"2", "3":"3", "4":"4" ,"5":"5", "6":"6", "7":"7" ,"8":"8", "9":"9"}
    display_game(game_list)
    player1 , player2 = caracter_choice()
    
    while True:
        if not winner(game_list, player1) and not winner(game_list, player2) and not tie(game_list):
            who_play = "Player 1"
            
            while True:
                if who_play == "Player 1":
                    print("Player 1")
                    position = position_choice(game_list)
                    update_game(game_list, position, player1)
                    display_game(game_list)
                    if winner(game_list, player1):
                        print(f"{player1}  Player 1: Win 👏🎉!")
                        break
                    if tie(game_list):
                        print("Draw")
                        break
                    else:
                        who_play = "Player 2"
            
                else:
                    print("Player 2")
                    position = position_choice(game_list)
                    update_game(game_list, position, player2)
                    display_game(game_list)
                    if winner(game_list, player2):
                        print(f"{player2}  Player2: Win 👏🎉!")
                        break
                    if tie(game_list):
                        print("Draw")
                        break
                    else:
                        who_play = "Player 1"
        
        else:
            game_on = game_on_choice()
            if game_on:
                os.system("cls")
                break
            else:
                break
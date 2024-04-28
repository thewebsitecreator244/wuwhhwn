import os


#board color
CYAN = "\033[1;36m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
# winning lines
LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, -1),
    (0, 3, 6), (1, 4, 7), (2, 5, -1),
    (6, 4, 2), (0, 4, -1)

)
#cells_list
cells = list(range(1, 10))
#names
player_name1 = CYAN + input("player 1 what is your name?:\n") + GREEN
player_name2 = RED + input("player 2 what is your name?:\n")  + GREEN
os.system("cls")
# board:
print(GREEN)
print(f"[{cells[0]}] [{cells[1]}] [{cells[2]}]")
print(f"[{cells[3]}] [{cells[4]}] [{cells[5]}]")
print(f"[{cells[6]}] [{cells[7]}] [{cells[-1]}]")
player_win = False
player2_win = False
tie = False
move_count = 0
while not player_win and not player2_win and not tie:
    if move_count % 2 == 0:
        number_choice = int(input(f"{player_name1} enter a number from 1 to 9:\n"))
        case_occupied = f"{CYAN}O{GREEN}"
        os.system("cls")
    else:
        number_choice = int(input(f"{player_name2} enter a number from 1 to 9:\n"))
        case_occupied = f"{RED}X{GREEN}"
        os.system("cls")
    if number_choice in cells:
        cells[number_choice-1] = case_occupied
        move_count += 1
        #tie
        if move_count == 9:
            tie = True
        print(f"[{cells[0]}] [{cells[1]}] [{cells[2]}]")
        print(f"[{cells[3]}] [{cells[4]}] [{cells[5]}]")
        print(f"[{cells[6]}] [{cells[7]}] [{cells[-1]}]")
        print("")
        #check if player wins
        for line in LINES:
            if cells[line[0]] == cells[line[1]] == cells[line[2]]:
                if case_occupied == f"{RED}X{GREEN}":
                    player2_win = True
                else:
                    player_win = True
                break
    else:
        print("impossible move this square is occcupied by another player or does not exist")
        print("")
        print(f"[{cells[0]}] [{cells[1]}] [{cells[2]}]")
        print(f"[{cells[3]}] [{cells[4]}] [{cells[5]}]")
        print(f"[{cells[6]}] [{cells[7]}] [{cells[-1]}]")
        print("")
if player_win:
    print(f"{player_name1} wins")
elif player2_win:
    print(f"{player_name2} wins")
else:
    print(f"{YELLOW}it is a tie")
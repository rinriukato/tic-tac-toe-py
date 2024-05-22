import os
import art

PLAYER_1 = 1
PLAYER_2 = 2

valid_positions = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
player_1_positions = []
player_2_positions = []


def is_valid_grid_position(pos: str, player: int) -> bool:
    if pos.lower() in valid_positions:
        remove_grid_position(pos, player)
        return True
    else:
        return False


def remove_grid_position(pos: str, player: int):
    removed_pos = valid_positions.pop(valid_positions.index(pos))
    add_to_player_positions(removed_pos, player)


def add_to_player_positions(pos: str, player: int):
    if player == PLAYER_1:
        player_1_positions.append(pos)
    else:
        player_2_positions.append(pos)


def did_player_win(player_pos: list[str]) -> bool:
    winning_combinations = [
        ['a1', 'a2', 'a3'],
        ['b1', 'b2', 'b3'],
        ['c1', 'c2', 'c3'],
        ['a1', 'b1', 'c1'],
        ['a2', 'b2', 'c2'],
        ['a3', 'b3', 'c3'],
        ['a1', 'b2', 'c3'],
        ['c1', 'b2', 'a3'],
    ]

    for combo_list in winning_combinations:
        if all(i in player_pos for i in combo_list):
            return True

    return False


def can_keep_playing() -> bool:
    # Check if Player 1 has won
    if did_player_win(player_1_positions):
        print("Player 1 Won!")
        return False

    # Check if Player 2 has won
    elif did_player_win(player_2_positions):
        print("Player 2 Won!")
        return False

    # Check if there are any open spaces left
    elif len(valid_positions) <= 0:
        print("No more spaces left! Its a draw...")
        return False

    else:
        return True


def update_board_row(row_graphic: str, row_num: int) -> str:
    a_col = "a" + str(row_num)
    b_col = "b" + str(row_num)
    c_col = "c" + str(row_num)
    target_columns = [a_col, b_col, c_col]
    row_graphic = f"{row_num}"

    for col in target_columns:
        if col in player_1_positions:
            row_graphic += "  X  |"
        elif col in player_2_positions:
            row_graphic += "  O  |"
        else:
            row_graphic += "  -  |"

    return row_graphic[:-1]


def print_board():
    print(art.row_1)
    print(art.row_2)
    print(update_board_row(art.row_3, 1))
    print(art.row_4)
    print(art.row_2)
    print(update_board_row(art.row_6, 2))
    print(art.row_4)
    print(art.row_2)
    print(update_board_row(art.row_9, 3))
    print(art.row_2)


def player_move(player: int):
    player_move = input(f"Player {player}, your move. Place marker by typing grid position: ")
    while not is_valid_grid_position(player_move, player):
        player_move = input("Space not valid or is occupied. Input different grid position: ")
    print_board()


print_board()
while True:
    player_move(1)
    if not can_keep_playing():
        break
    player_move(2)
    if not can_keep_playing():
        break


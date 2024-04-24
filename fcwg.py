
names = {"F": "Farmer",
         "W": "Wolf",
         "C": "Cabbage",
         "G": "Goat",}
forbidden_states = [{"W", "G"}, {"G", "C"}, {"G", "C", "W"}]
def print_story():
    print("*" * 50)
    print("\n#### WOLF, GOAT, and CABBAGE PROBLEM ####\n")
    print("Once upon a time, a farmer went to a market and purchased a wolf, a goat, and a cabbage.")
    print("On his way home, the farmer came to the bank of a river and rented a boat.")
    print("But crossing the river by boat, the farmer could carry only himself and a single one of his purchases:")
    print("the wolf, the goat, or the cabbage.")
    print("If left unattended together, the wolf would eat the goat, or the goat would eat the cabbage.")
    print("The farmer's challenge was to carry himself and his purchases to the far bank of the river, leaving each purchase intact.")
    print("How did he do it?\n")
    input("Press enter to continue.")



def print_state(state, direction=None):
    left_bank, right_bank = state
    print("\n#### CURRENT STATE OF PUZZLE ####")
    left_bank_display = [names[item] for item in left_bank]
    right_bank_display = [names[item] for item in right_bank]
    if direction:
        print(f"Move: {direction}")
    print("Left Bank: ", left_bank_display, "| Right Bank: ", right_bank_display if right_bank else "[]")
    print("=" * 50 )

def get_move():
    print("\nWhich item do you wish to take across the river? - First left to right then right to left respectively ")
    answer = ""
    while answer.upper() not in ["F", "W", "G", "C"]:
        answer = input("Just type the letter only! Farmer (f), Wolf (w), Goat (g) or Cabbage (c)?. \nYou can return back by farmer:>>  ")

    return answer.upper()


def process_move(move, state):
    # Determine the direction of the move
    direction = "Left to Right" if move in state[0] else "Right to Left"

    # Create a temporary state to simulate the move
    temp_state = [state[0].copy(), state[1].copy()]
    containing_set = 0 if move in state[0] else 1
    # Check if the farmer is accompanying the move
    if "F" not in state[containing_set]:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!  Not allowed - the farmer must accompany the item.  !!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return state, None
    # Simulate the move
    if containing_set == 0:
        temp_state[0].difference_update({move, "F"})
        temp_state[1].update([move, "F"])
    elif containing_set == 1:
        temp_state[1].difference_update({move, "F"})
        temp_state[0].update([move, "F"])
    # Check if the new state is allowed
    if temp_state[0] not in forbidden_states and temp_state[1] not in forbidden_states:
        state = [temp_state[0].copy(), temp_state[1].copy()]
    else:
     # If the new state is forbidden, determine which item would be eaten
        if temp_state[0] in forbidden_states:
            forbidden_state = temp_state[0]
        else:
            forbidden_state = temp_state[1]
        for item in forbidden_state:
            if item != "F":
                forbidden_item = names[item]
                break
        # farmer_bank = "Left" if containing_set == 1 else "Right"
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        # print(f"!!  Not allowed - if left alone on the {farmer_bank} bank, the {forbidden_item} would eat the other item.  !!")
        print(f"!! WRONG: one of your items would be eaten!  !!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        direction = None
    return state, direction


def is_win(state):
    return state[1] == {"F", "W", "G", "C"}

def main():
    left_bank = {"F", "W", "G", "C"}
    right_bank = set()
    state = [left_bank, right_bank]
    print_story()
    while not is_win(state):
        move = get_move()
        state, direction = process_move(move, state)
        print_state(state, direction)

    print("\n##########################################")
    print("##                                      ##")
    print("##  WELL DONE - YOU SOLVED THE PUZZLE!  ##")
    print("##                                      ##")
    print("##########################################")

if __name__ == "__main__":
    main()
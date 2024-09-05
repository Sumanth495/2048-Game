from logic import *

def main():
    mat = start_game()
    while True:
        x = input("Press the command : ")
        if x in ['W', 'w']:
            mat, changed = move_up(mat)
        elif x in ['S', 's']:
            mat, changed = move_down(mat)
        elif x in ['A', 'a']:
            mat, changed = move_left(mat)
        elif x in ['D', 'd']:
            mat, changed = move_right(mat)
        else:
            print("Invalid Key Pressed")
            continue
        if changed:
            add_new_2(mat)
        else:
            print("No Change in the Grid")

        for row in mat:
            print(row)

        state = get_current_state(mat)
        print(state)
        if state == 'WON' or state == 'LOST':
            break

if __name__ == "__main__":
    main()

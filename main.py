from WordGamesSolvers import Anagrams, WordHunt, WordBites

select = int(input("Anagrams [1] or WordHunt [2] or WordBites [3]: "))
if  select == 1:
    board = input("Enter board: ")
    cur = Anagrams(board)
    try: cur.print_words()
    except Exception as e: print("Error:", str(e))

elif select == 2:
    board = input("Enter board: ")
    cur = WordHunt(board)
    try: cur.print_words()
    except Exception as e: print("Error:", str(e))

elif select == 3:
    singles = input("Enter single tiles (differentiate tiles using a space): ").split()
    vert = input("Enter vertical tiles: ").split()
    hor = input("Enter horizontal tiles: ").split()
    cur = WordBites(singles, vert, hor)
    cur.print_words()
    
else:
    print("Input not recognized.")
from WordGamesSolvers import Anagrams, WordHunt

select = int(input("Anagrams [1] or WordHunt [2]: "))
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
else:
    print("Input not recognized.")
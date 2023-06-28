from WordFinder import WordFinder

board = input("Enter board: ")
cur = WordFinder(board)

try:
    cur.valid_words()
except Exception as e:
    print("Error:", str(e))


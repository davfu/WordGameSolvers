class WordFinder:
    def __init__(self, board) -> None:
        self.board = [char for char in board]
        self.found_words = set()
        self.filename = 'words.txt'
        if not len(self.board) == 16:
            raise Exception("Board must be 16 characters.")
    
    def fine_all_combos(self):
        seen = []
        for node in range(len(self.board)):
            seen.append(node)
            # recursive DFS


    
    def valid_neighbors(self, node, seen):
        row, col = node // 4, node % 4
        # list of positions with their corresponding list of operators
        config = [["TLC", "TE", "TE", "TRC"],
                  ["LE", "IP", "IP", "RE"],
                  ["LE", "IP", "IP", "RE"],
                  ["BLC", "BE", "BE", "BRC"]]
        positions = {"TLC": [+1, +5, +4], 
                     "TRC": [-1, +3, +4], 
                     "BLC": [-4, -3, +1], 
                     "BRC": [-1, -5, -4], 
                     "TE": [-1, +3, +4, +5, +1], 
                     "RE": [-4, -5, -1, +3, +4], 
                     "BE": [-1, -5, -4, -3, +1], 
                     "LE": [-4, -3, +1, +5, +4], 
                     "IP": [-5, -1, +3, +4, +5, +1, -3, -4]}
        # find the neighbors based on operator and if in seen
        operator = positions[config[row][col]]
        valid_neighbors = [node + val for val in operator if node + val not in seen]
        return valid_neighbors

    def valid_words(self, list_combos): # sorted from longest to shortest
        with open(self.filename, 'r') as file: dictionary_words = [word.strip() for word in file.readlines()]
        valid_words = []
        # check every word if valid and add to list
        for word in list_combos:
            if word in dictionary_words: valid_words.append(word)
        # sort list from longest word to shortest
        valid_words.sort(key=len, reverse=True)
        return valid_words

    def return_board(self):
        return self.board

    



        
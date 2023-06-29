from Trie import Trie, TrieNode

class WordFinder:
    def __init__(self, board) -> None:
        self.board = [char for char in board]
        self.words_set = set()
        self.words_list = []
        self.filename = 'dictionary.txt'
        self.trie = Trie()
        if not len(self.board) == 16: raise Exception("Board must be 16 characters.")
    
    # set up the trie to reflect self.filename
    def make_trie(self):
        with open(self.filename, 'r') as file: dictionary_words = [word.strip() for word in file.readlines()]
        for word in dictionary_words:
            self.trie.insert(word)
    
    # returns nodes that can be neighbors
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
    
    # finds words in all nodes calling DFS method
    def find_words(self):
        seen = []
        for node in range(16):
            self.dfs_words(node, seen)

    # finds words in a given node using DFS
    def dfs_words(self, node, seen):
        # compute dfs if node has not been visited
        if node not in seen:
            new_seen = [i for i in seen] + [node]
            neighbors = self.valid_neighbors(node, new_seen)
            cur_word = ''.join([self.board[i] for i in new_seen])

            # add word to set of words if valid word
            if len(new_seen) >= 3 and self.trie.valid_word(cur_word):
                self.words_set.add(cur_word)

            # recurse if a word possible exists w/ current prefix
            if self.trie.valid_prefix(cur_word):
                for node in neighbors: self.dfs_words(node, new_seen)
    
    # returns board
    def return_board(self):
        return self.board
    
    # sorts and prints valid wordsp
    def print_words(self):
        self.make_trie()
        self.find_words()
        self.words_list = list(self.words_set)
        self.words_list.sort(key=len)
        for i in range(len(self.words_list)):
            print(self.words_list[i])
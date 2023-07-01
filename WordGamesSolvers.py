import copy
from Trie import Trie

class WordGameSolver:
    def __init__(self) -> None:
        self.words_set = set()
        self.words_map = {}
        self.filename = 'dictionary.txt'
        self.trie = Trie()
    
    def make_trie(self):
        with open(self.filename, 'r') as file: dictionary_words = [word.strip() for word in file.readlines()]
        for word in dictionary_words:
            self.trie.insert(word)
            
    # finds words in all nodes calling DFS method
    def find_words(self):
        seen = []
        for node in range(len(self.board)):
            self.dfs_words(node, seen)

    # classify the words on basis of word length
    def classify_words(self):
        for word in self.words_set:
            if len(word) not in self.words_map:
                self.words_map[len(word)] = []
            self.words_map[len(word)].append(word)
    
    # sorts and prints valid words
    def print_words(self):
        self.make_trie()
        self.find_words()
        self.classify_words()
        for key in sorted(self.words_map.keys()):
            print("\n" + str(key) + " letter words (" + str(len(self.words_map[key])) + "): \n" + "-------------------")
            for word in self.words_map[key]:
                print(word, end='   ')
            print()

class Anagrams(WordGameSolver):
    def __init__(self, board) -> None:
        super().__init__()
        self.board = [char for char in board]
        if not len(self.board) == 6: raise Exception("Board must be 6 characters.")
        
    def dfs_words(self, node, seen):
        if node not in seen:
            new_seen = [i for i in seen] + [node]
            cur_word = ''.join([self.board[i] for i in new_seen])
            if len(new_seen) >= 3 and self.trie.valid_word(cur_word):
                self.words_set.add(cur_word)
            if self.trie.valid_prefix(cur_word):
                for node in list(set([i for i in range(len(self.board))]) - set(new_seen)): self.dfs_words(node, new_seen)

class WordHunt(WordGameSolver):
    def __init__(self, board) -> None:
        super().__init__()
        self.board = [char for char in board]
        if not len(self.board) == 16: raise Exception("Board must be 16 characters.")

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

class WordBites(WordGameSolver):
    def __init__(self, singles, vert, hor) -> None:
        super().__init__()
        self.board = {'s': singles, 'v': vert, 'h': hor}
    
    def find_words(self):
        remaining = {'s': copy.deepcopy(self.board['s']), 
                     'v': copy.deepcopy(self.board['v']), 
                     'h': copy.deepcopy(self.board['h'])}
        for key in self.board:
            for val in self.board[key]:
                self.vert_words((key, val), remaining, '')

    def vert_words(self, node, remaining, prev_word): 
        if node[1] in remaining[node[0]]:
            # remove node from remaining
            new_remaining = {key: [value[i] for i in range(len(value)) if value[i] != node[1] or (value[i] == node[1] and i != value.index(node[1]))] if key == node[0] else value for key, value in remaining.items()}
            if node[0] == 'h': iters = 2 # two possible words:
            else: iters = 1
            for i in range(iters):
                if iters == 2: cur_word = prev_word + node[1][i]
                else: cur_word = prev_word + node[1]
                if len(cur_word) >= 3 and self.trie.valid_word(cur_word): self.words_set.add(cur_word)
                if self.trie.valid_prefix(cur_word): 
                    for key in new_remaining:
                        for val in new_remaining[key]:
                            self.vert_words((key, val), new_remaining, cur_word)

            # if node[0] == 'h':
            #     cur_word1, cur_word2 = prev_word + node[1][0], prev_word + node[1][1]
            #     if len(cur_word1) >= 3 and self.trie.valid_word(cur_word1): self.words_set.add(cur_word1)
            #     if len(cur_word2) >= 3 and self.trie.valid_word(cur_word2): self.words_set.add(cur_word2)
            #     if self.trie.valid_prefix(cur_word1): 
            #         for key in new_remaining:
            #             for val in new_remaining[key]:
            #                 self.vert_words((key, val), new_remaining, cur_word1)
            #     if self.trie.valid_prefix(cur_word2):
            #         for key in new_remaining:
            #             for val in new_remaining[key]:
            #                 self.vert_words((key, val), new_remaining, cur_word2)
            # else:
            #     cur_word = prev_word + node[1]
            #     if len(cur_word) >= 3 and self.trie.valid_word(cur_word): self.words_set.add(cur_word)
            #     if self.trie.valid_prefix(cur_word):
            #         for key in new_remaining:
            #             for val in new_remaining[key]:
            #                 self.vert_words((key, val), new_remaining, cur_word)

    def hor_words(self):
        hor_starters = [char for string in self.board['v'] for char in string] + self.board['h'] + self.board['s']
        print("horizontal starters" + str(hor_starters))
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False
    
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children: node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True
    
    def valid_word(self, word):
        node = self.root
        for char in word: 
            if char not in node.children: return False
            node = node.children[char]
        return node.end_of_word
    
    def valid_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children: return False
            node = node.children[char]
        return True

    

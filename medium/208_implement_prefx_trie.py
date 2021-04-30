class Node:
    def __init__(self, children, is_word):
        self.children = children
        self.is_word = is_word


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Node({}, False)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.trie
        for char in word:
            if char not in current.children:
                current.children[char] = Node({}, False)
            current = current.children[char]
        current.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.trie
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given
        prefix.
        """
        current = self.trie
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

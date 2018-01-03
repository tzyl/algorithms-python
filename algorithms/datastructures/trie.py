class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for c in word:
            if c not in current.links:
                current.links[c] = TrieNode()
            current = current.links[c]
            current.size += 1
        current.is_word = True

    def search(self, word):
        current = self.root
        for c in word:
            if c not in current.links:
                return False
            current = current.links[c]
        return current.is_word

    def starts_with_count(self, prefix):
        current = self.root
        for c in prefix:
            if c not in current.links:
                return 0
            current = current.links[c]
        return current.size

    def starts_with(self, prefix):
        current = self.root
        for c in prefix:
            if c not in current.links:
                return False
            current = current.links[c]
        return True


class TrieNode:
    def __init__(self):
        self.links = {}
        self.is_word = False
        self.size = 0


# if __name__ == '__main__':
#     trie = Trie()
#     trie.insert("abc")
#     trie.insert("abcdef")
#     print(trie.search("abc"))
#     print(trie.starts_with("abc"))
#     print(trie.search("abcd"))
#     print(trie.starts_with("abcd"))

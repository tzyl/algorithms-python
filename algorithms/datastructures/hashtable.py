from .linkedlist import LinkedList


class Map:
    """Hash table with collision resolution by chaining in linked lists.
    Contains 701 slots and uses division method for hash function.
    Accepts key, value inserts and returns the value for a given key.
    """
    def __init__(self):
        self.m = 701
        self.data = [LinkedList()] * self.m

    def hash(self, k):
        return k % self.m

    def insert(self, k, v):
        self.data[self.hash(k)].insert(Node(k, v))

    def search(self, k):
        node = self.data[self.hash(k)].search(k)
        return node.value if node is not None else None

    def delete(self, k):
        node = self.data[self.hash(k).search(k)]
        if node is not None:
            self.data[self.hash(k)].delete(node)


class HashTable:
    """Hash table with collision resolution by chaining in linked lists.
    Contains 701 slots and uses division method for hash function.
    """
    def __init__(self):
        self.m = 701
        self.data = [LinkedList()] * self.m

    def hash(self, k):
        return k % self.m

    def insert(self, x):
        self.data[self.hash(x.key)].insert(x)

    def search(self, k):
        return self.data[self.hash(k)].search(k)

    def delete(self, x):
        self.data[self.hash(x.key)].delete(x)


class HashTableOpenAddressing:
    """Hash table using open addressing with linear probing for
    collision resolution. Replaces elements if table gets full.
    """
    def __init__(self):
        self.m = 701
        self.data = [None] * self.m

    def hash(self, k, i):
        return (k + i) % 701

    def insert(self, x):
        i = 0
        while self.data[self.hash(x.key, i)] is not None and i < self.m:
            i += 1
        self.data[self.hash(x.key, i)] = x

    def search(self, k):
        i = 0
        while self.data[self.hash(k, i)] is not None and i < self.m:
            if self.data[self.hash(k, i)].key == k:
                break
            i += 1
        return self.data[self.hash(k, i)] if i != self.m else None

    def delete(self, x):
        # Deletion complicated with open addressing.
        pass


class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


# if __name__ == "__main__":
#     hash_table = HashTable()
#     for i in range(697, 706):
#         node = Node(i)
#         print(hash_table.hash(node.key))
#         hash_table.insert(node)
#     for i in range(697, 707):
#         print(hash_table.search(i))
#     for i in range(697, 706):
#         hash_table.delete(hash_table.search(i))
#     for i in range(697, 707):
#         print(hash_table.search(i))

#     hash_table2 = HashTableOpenAddressing()
#     for i in range(701):
#         hash_table2.insert(Node(i))
#     for i in range(100):
#         hash_table2.insert(Node(i + 701))
#     print([node_.key for node_ in hash_table2.data])

#     my_dict = Map()
#     my_dict.insert(1, "Hello")
#     my_dict.insert(25, " world!")
#     print(my_dict.search(1) + my_dict.search(25))

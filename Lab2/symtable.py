
class hashTable:
    def __init__(self, size):
        """
        Initialize the hashtable by creating a list of a given size that on every position contains an empty list
        :param size: size of the hashtable
        """
        self.size = size
        self.items = []
        for i in range(0, size):
            self.items.append([])
        self.counter = 1

    def getSize(self):
        """
        :return: size of hashtable
        """
        return self.size

    def hash(self, key):
        """
        hash a string to a number lower than the size of the hash table
        :param key: the string to be hashed
        :return: the value of the hashed string
        """
        s = 0
        for i in range(len(key)):
            s += ord(key[i])
        return s % self.size

    def add(self, key):
        """
        add an element to the hashtable
        :param key: element
        :return: True if the element does not already exist in the table, False otherwise
        """
        hashVal = self.hash(key)
        if not self.contains(key):
            self.items[hashVal].append((self.counter, key))
            self.counter += 1
            return True
        return False

    def contains(self, key):
        """
        checks if the hashtable contains the given element
        :param key: the element to be checked if it is contained in the hashtable
        :return: True if it is contained in the hashtable, False otherwise
        """
        hashVal = self.hash(key)
        for tpl in self.items[hashVal]:
            if key in tpl:
                return True
        if key in self.items[hashVal]:
            return True
        return False

    def getPosition(self, key):
        """
        searches and returns the position of the element in the hashtable
        :param key: the element that is looked for in the hashtable
        :return: a tuple containing the position in the list and the index in the inner list if it exist,
                 a tuple (-1, -1) if the key does not exist in the hashtable
        """
        if self.contains(key):
            listPosition = self.hash(key)
            listIndex = 0
            for e in self.items[listPosition]:
                if e[1] != key:
                    listIndex += 1
                else:
                    break
            return listPosition, listIndex
        return -1, -1

    def remove(self, key):
        """
        removes an element from the hashtable if it exists
        :param key: the element to be removed
        :return: True if the element exists in the hashtable and it is removed, False otherwise
        """
        hashVal = self.hash(key)
        if key in self.items[hashVal]:
            self.items[hashVal].remove(key)
            return True
        return False

    def toString(self):
        """
        prints a string that illustrates the hashtable
        :return:
        """
        for i in range(self.size):
            print(i, " : ", end='')
            if len(self.items[i]) == 0:
                print("empty")
            else:
                print(*self.items[i], sep="; ")

    def getItems(self):
        return self.items


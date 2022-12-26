class HashTable:

    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None] * table_size  # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value = None):
        ''' Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1).'''
        i = 0
        hash_val = self.horner_hash(key)
        while self.hash_table[hash_val + i ** 2] and self.hash_table[hash_val + i ** 2][0] != key:
            i += 1
            if hash_val ** 2 + i >= self.table_size:
                hash_val -= self.table_size
        if self.hash_table[hash_val + i ** 2] == None and type(value) is not list:
            self.hash_table[hash_val + i ** 2] = (key, [value])
            self.num_items += 1
        elif self.hash_table[hash_val+i**2] == None and type(value) is list:
            self.hash_table[hash_val + i ** 2] = (key, value)
            self.num_items += 1
        elif self.hash_table[hash_val + i ** 2][0] == key:
            self.hash_table[hash_val + i ** 2][1][0] = value
        if self.get_load_factor() > 0.5:
            self.rehash()

    def horner_hash(self, key):
        ''' Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification.'''
        num = min(len(key), 8)
        val = 0
        for i in range(num):
            val += ord(key[i]) * 31 ** (num - 1 - i)
        return val % self.table_size

    def in_table(self, key):
        ''' Returns True if key is in an entry of the hash table, False otherwise.'''
        i = self.quad_probe_i(key)
        if self.hash_table[i] != None:
            if self.hash_table[i][0] == key:
                return True
        return False

    def get_index(self, key):
        ''' Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None.'''
        if not self.in_table(key):
            return None
        else:
            i = self.quad_probe_i(key)
            if self.hash_table[i] != None:
                if self.hash_table[i][0] == key:
                    return i

    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        keys = []
        for item in self.hash_table:
            if item != None:
                keys.append(item[0])
        return keys

    def get_value(self, key):
        ''' Returns the value associated with the key. 
        If key is not in hash table, returns None.'''
        if not self.in_table(key):
            return None
        i = self.quad_probe_i(key)
        if self.hash_table[i] != None:
            if self.hash_table[i][0] == key:
                return self.hash_table[i][1][0]

    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.num_items

    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return self.table_size

    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        return self.num_items/self.table_size

    def quad_probe_i(self, key):
        i = 0
        hash_val = self.horner_hash(key)
        while self.hash_table[hash_val + i ** 2] and self.hash_table[hash_val + i ** 2][0] != key:
            i += 1
            if hash_val + i ** 2 >= self.table_size:
                hash_val -= self.table_size
        return hash_val + i ** 2


    def rehash(self):
        old_table = self.hash_table
        new_table_size = self.table_size * 2 + 1
        self.hash_table = [None] * new_table_size
        self.table_size = new_table_size
        self.num_items = 0
        for item in old_table:
            if item == None:
                continue
            else:
                self.insert(item[0], item[1])
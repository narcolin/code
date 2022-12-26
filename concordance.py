from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = HashTable(191)          # hash table for stop words
        self.concordance_table = HashTable(191)   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            file = open(filename, 'r')
        except:
            raise FileNotFoundError
        words = file.readlines()
        for line in range(len(words)):
            self.stop_table.insert(words[line].strip(), 0)
        file.close()

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            file = open(filename, 'r')
        except:
            raise FileNotFoundError
        words = file.readlines()

        for line in range(len(words)):
            words[line] = words[line].strip()
            new_line = self.remove_helper(words[line])
            for only_words in new_line.split():
                if self.is_a_number(only_words):
                    continue
                else:
                    self.concordance_table.insert(only_words, line + 1)

        for i in range(len(self.concordance_table.hash_table)):
            if self.concordance_table.hash_table[i] != None:
                temp = set(self.concordance_table.hash_table[i][1])
                sort_temp = list(temp)
                sort_temp.sort()
                key = self.concordance_table.hash_table[i][0]
                self.concordance_table.hash_table[i] = (key, sort_temp)
        file.close()

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        outfile = open(filename, 'w')
        tuple_list = []
        output = ''
        for item in self.concordance_table.hash_table:
            if item != None:
                temp = (item[0].lower(), [0])
                if temp in self.stop_table.hash_table:
                    item = 0
                tuple_list.append(item)

        tuple_list = list(filter(lambda a: a != 0, tuple_list))
        tuple_list.sort()
        for pairs in tuple_list:
            temp = ''
            for nums in pairs[1]:
                temp += str(nums) + ' '
            nums = temp.strip()
            output += pairs[0].lower() + ": " + nums + '\n'
        final = output.strip()
        outfile.write(final)
        outfile.close()

    def remove_helper(self, line):
        new = line
        for char in line:
            if char == '-':
                new = new.replace(char, ' ')
            if char in string.punctuation:
                new = new.replace(char, '')
        return new.lower()

    def is_a_number(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False
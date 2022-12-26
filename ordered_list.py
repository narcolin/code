class Node:
    # node for use with doubly-linked list
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class OrderedList:
    # A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)

    def __init__(self):
        # Use ONE dummy node as described in class, No other attributes
        # DO NOT have an attribute to keep track of size
        self.head = Node(None)
        self.head.next = self.head
        self.head.prev = self.head

    def __lt__(self, other):
        if not (isinstance(other, OrderedList)):
            return False
        cur = self.head.next
        cur2 = other.head.next
        while cur != self.head and cur2 != self.head:
            if cur.item >= cur2.item:
                return False
            cur = cur.next
            cur2 = cur2.next
        return True

    def __eq__(self, other):
        if not (isinstance(other, OrderedList)):
            return False
        cur = self.head.next
        cur2 = other.head.next
        while cur != self.head and cur2 != self.head:
            if cur.item != cur2.item:
                return False
            cur = cur.next
            cur2 = cur2.next
        return True

    def is_empty(self):
        # Returns True if OrderedList is empty. MUST have O(1) performance
        return self.head.next == self.head

    def add(self, item):
        # Adds an item to OrderedList, in the proper location based on ordering of items
        # from lowest (at head of list) to highest (at tail of list) and returns True.
        # If the item is already in the list, do not add it again and return False.
        # MUST have O(n) average-case performance'''
        new = Node(item)
        current = self.head.next
        count = 0
        duplicate = 0
        while current != self.head and count == 0 and duplicate == 0:
            if current.item >= item:
                if current.item == item:
                    duplicate = 1
                else:
                    count = 1
            else:
                current = current.next
        if duplicate == 1:
            pass

        else:
            new.next = current
            new.prev = current.prev
            current.prev.next = new
            current.prev = new

    def remove(self, item):
        # Removes the first occurrence of an item from OrderedList. If item is removed (was in the list)
        # returns True.  If item was not removed (was not in the list) returns False
        # MUST have O(n) average-case performance
        current = self.head.next
        if current.next == self.head:
            if current.item == item:
                self.head.next = self.head
                self.head.prev = self.head
                return True
            else:
                return False
        while current != self.head and current.item != item:
            current = current.next
        if current == self.head:
            return False
        current.prev.next = current.next
        current.next.prev = current.prev
        current.next = None
        current.prev = None
        return True

    def index(self, item):
        # Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
        # If item is not in list, return None
        # MUST have O(n) average-case performance
        current = self.head.next
        count = 0
        while item != current.item:
            count += 1
            if current == self.head:
                return None
            current = current.next
        return count

    def pop(self, index):
        # Removes and returns item at index (assuming head of list is index 0).
        # If index is negative or >= size of list, raises IndexError
        # MUST have O(n) average-case performance
        current = self.head.next
        if current == self.head or index < 0:
            raise IndexError
        count = 0
        while count < index:
            count += 1
            current = current.next
            if current == self.head:
                raise IndexError
        current.prev.next = current.next
        current.next.prev = current.prev
        return current.item

    def search(self, item):
        # Searches OrderedList for item, returns True if item is in list, False otherwise"
        # To practice recursion, this method must call a RECURSIVE method that
        # will search the list. MUST have O(n) average-case performance
        current = self.head.next
        if current.item == None or self.head == current:
            return False
        else:
            return self.search_helper(current, item)  # Question

    def search_helper(self, node, item):
        if node.item == item:
            return True
        elif node.item == None or self.head == node:
            return False
        elif node.item > item:
            return False
        else:
            return self.search_helper(node.next, item)

    def python_list(self):
        # Return a Python list representation of OrderedList, from head to tail
        # For example, list with integers 1, 2, and 3 would return [1, 2, 3]
        # MUST have O(n) performance
        current = self.head.next
        python_list = []
        while current != self.head:
            python_list.append(current.item)
            current = current.next
        return python_list

    def python_list_reversed(self):
        # Return a Python list representation of OrderedList, from tail to head, using recursion
        # For example, list with integers 1, 2, and 3 would return [3, 2, 1]
        # To practice recursion, this method must call a RECURSIVE method that
        # will return a reversed list. MUST have O(n) performance
        current = self.head.next
        return self.python_list_reversed_helper(current)

    def python_list_reversed_helper(self, node):
        if node == self.head:
            return []
        return self.python_list_reversed_helper(node.next) + [node.item]

    def size(self):
        # returns number of items in the OrderedList
        # To practice recursion, this method must call a RECURSIVE method that
        # will count and return the number of items in the list
        # MUST have O(n) performance
        current = self.head.next
        return self.size_helper(current, 0)

    def size_helper(self, node, count):
        if node == self.head:
            return count
        else:
            return self.size_helper(node.next, count + 1)


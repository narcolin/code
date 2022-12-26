class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.front = 0
        self.back = 0
        self.items = [None] * (capacity + 1)
        self.num_items = 0

    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''
        if self.num_items == 0:
            return True
        else:
            return False


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''
        if self.capacity == self.num_items and self.num_items > 0:
            return True
        else:
            return False


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance'''
        if not self.is_full():
            self.items[self.back % self.capacity] = item
            self.num_items += 1
            self.back += 1
        else:
            raise IndexError


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():  # If empty, raise error
            raise IndexError
        else:
            self.num_items -= 1
            item = self.items[self.front % self.capacity]
            self.front += 1
            return item


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.num_items
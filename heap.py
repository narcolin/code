#Nicole Arcolino 202 Lab 07
class MaxHeap:

    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created.'''
        self.cap = capacity
        self.items = [None] * capacity
        self.size = 0

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other 
           items using the < operator'''
        if self.is_full():
            return False
        self.size += 1
        self.items.append(item)
        self.perc_up(self.size)
        return True

    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        if self.is_empty():
            return None
        return self.items[1]

    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty'''
        if self.is_empty():
            return None
        max = self.peek()
        self.items[1] = self.items[self.size]
        self.items.pop()
        self.size -= 1
        self.perc_down(1)
        return max

    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        return self.items[1:]

    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from 
        the items in alist using the bottom-up construction method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate the items in alist'''
        if self.cap < len(alist):
            self.cap = len(alist)
        index = len(alist)//2
        self.size = len(alist)
        self.items = [None] + alist
        while index > 0:
            self.perc_down(index)
            index -= 1

    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        if self.size == 0:
            return True
        return False

    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        if self.get_capacity() == self.cap:
            return True
        return False
        
    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        return (len(self.items) - 1)
    
    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.size
        
    def perc_down(self, i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        while i * 2 <= self.size:
            max_item = self.max_helper(i)
            # check to see if child is larger than current item at index i.
            if self.items[max_item] > self.items[i]:
                # swaps with the largest child
                temp = self.items[i]
                self.items[i] = self.items[max_item]
                self.items[max_item] = temp
            i = max_item
        
    def perc_up(self, i):
        '''where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        while self.items[i//2]:
            if self.items[i] > self.items[i//2]:
                temp = self.items[i]
                self.items[i] = self.items[i//2]
                self.items[i//2] = temp
            i = i//2

    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''
        new_heap = MaxHeap(len(alist))
        new_heap.build_heap(alist)
        while new_heap.size > 0:
            max = new_heap.dequeue()
            alist.remove(max)
            alist.insert(0, max)

    def max_helper(self, i):
        # finds which child is bigger and returns its index
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.items[i * 2] > self.items[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
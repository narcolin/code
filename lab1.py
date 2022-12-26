# Nicole Arcolino
# CSC 202-07

def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list is None:
      raise(ValueError('Empty Case'))
   elif (len(int_list)) == 0:
      return None
   max = int_list[0]
   for x in int_list:
      if x > max:
            max = x
   return max

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError
   return helper(int_list)

def helper(int_list):
   if len(int_list) == 0 or len(int_list) == 1:
      return int_list
   return (helper(int_list[1:]) + [int_list[0]])

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list is None:
      raise (ValueError('Empty Case'))
   elif high <= low:
      return None
   else:
      mid = ((high + low) // 2)
      if mid == high == low and int_list[mid] != target:
         return None
      if target == int_list[mid]:
         return mid
      elif target < int_list[mid]:
         return bin_search(target, low, mid - 1, int_list)
      elif target > int_list[mid]:
         return bin_search(target, mid + 1, high, int_list)

# Signature: Maybe_List -> None
# Purpose: Reverse the original input list 
def reverse_list_mutate(int_list):
   '''Reverses a list, modifies the input list, returns None
   If list is None, raises ValueError'''
   if int_list is None:
      raise(ValueError('Empty Case'))
   k = 0
   j = len(int_list) - 1
   while (k < j):
      int_list[k], int_list[j] = int_list[j], int_list[k]
      k += 1
      j -= 1
   return int_list


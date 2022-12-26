# CPE 202 Lab 1
# Nicole Arcolino

def max_list_iter(int_list):  # must use iteration not recursion
   if int_list is None:
      raise(ValueError)
   elif (len(int_list)) == 0:
      return None
   largest_number = int_list[0]
   for number in int_list:
      if number > largest_number:
            largest_number = number
   return largest_number


def reverse_rec(int_list):  # must use recursion
    if int_list is None:
        raise ValueError
    return helper(int_list)

def helper(int_list):
    if len(int_list) == 0 or len(int_list) == 1:
        return int_list
    return (helper(int_list[1:]) + [int_list[0]])


def bin_search(target, low, high, int_list):  # must use recursion
    if int_list is None:
        raise ValueError
    elif high<=low:
        return None
    else:
        midpoint = ((high + low) // 2)
        if midpoint == high == low and int_list[midpoint] != target:
            return None
        if target == int_list[midpoint]:
            return midpoint
        elif target < int_list[midpoint]:
            return bin_search(target, low, midpoint - 1, int_list)
        elif target > int_list[midpoint]:
            return bin_search(target, midpoint + 1, high, int_list)

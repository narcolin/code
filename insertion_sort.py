import random

def insertion_sort(alist):
	count = 0
	for i in range(1, len(alist)):
		temp = alist[i]
		j = i - 1
		if temp < alist[j]:
			while temp < alist[j] and j >= 0:
				alist[j+1] = alist[j]
				j -= 1
				count +=1
			alist[j+1] = temp
		else:
			count += 1
	return count




# Test Cases:
#
# alist = [54,26,93,17,77,31,44,55,20]
# insertion_sort(alist)
# print(alist)
#
# n = 100
# my_randoms = random.sample(range(10000), n)
# count = insertion_sort(my_randoms)
# print(my_randoms)
# print ("Random, n =", n, "comp comparison count =", count)
#
# n = 200
# my_randoms = random.sample(range(10000), n)
# count = insertion_sort(my_randoms)
# print ("Random, n =", n, "comp comparison count =", count)
#
# # The reversed list is the worst case because insertion_sort has to reorder every single element by
# # traversing it all the way down to the beginning of the list.
# n = 100
# reverse = list(range(n,0,-1))
# count = insertion_sort(reverse)
# print(reverse)
# print ("Reversed, n =", n, "comp comparison count =", count)
#
# n = 200
# reverse = list(range(n,0,-1))
# count = insertion_sort(reverse)
# print ("Reversed, n =", n, "comp comparison count =", count)

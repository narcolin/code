# Nicole Arcolino
# CSC 202 Lab 6

import random
import time

def selection_sort(list):
    count = 0
    for fillslot in range(len(list) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            count += 1
            if list[location] > list[positionOfMax]:
                positionOfMax = location
        temp = list[fillslot]
        list[fillslot] = list[positionOfMax]
        list[positionOfMax] = temp
    return count
    
def insertion_sort(list):
    count = 0
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        if temp < list[j]:
            while temp < list[j] and j >= 0:
                list[j + 1] = list[j]
                j -= 1
                count += 1
            list[j + 1] = temp
        else:
            count += 1
    return count

def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 5000)
    start_time = time.time() 
    comps = selection_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()


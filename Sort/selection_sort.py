# from operator import index


# In-place comparision sorting.

# 1. Find the min number in the list
# 2. Swap the smallest value in the 0th index

import time


def selection_sort_asc(l):
    
    length = len(l)
    
    for i in range(length):
        min_index = i
        #finding the index of minimum value
        for j in range(i+1, length):
            if l[min_index] > l[j]:
                min_index = j
        #swapping
        l[i], l[min_index] = l[min_index], l[i]
    return l

def selection_sort_desc(l):
    
    length = len(l)
    
    for i in range(0,length):
        max_index = i
        #finding the max value
        for j in range(i+1, length):
            if l[j] > l[max_index]:
                max_index = j
        #swapping
        l[i], l[max_index] = l[max_index], l[i]
    return l


if __name__ == "__main__":
    test_arr = [x for x in range(0,1000)]
    start = time.time()
    print(selection_sort_desc(test_arr))
    end = time.time()
    ms = end-start
    print("Your code's performance: {} ms".format(str(ms)))
    

# Time Complexity
# Best: n^2
# Average: n^2
# Worst: n^2

# prefer to use selection sort incase of small lists (<1000)
# it took about 6 secs to sort a list of size 10000
# it took more than 2 mins to sort a list of size 1000000
# 0.07928609848022461 to sort an input of size 1000
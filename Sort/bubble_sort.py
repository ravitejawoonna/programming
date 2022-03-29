# Sorts the array by comparing the adjacent elements and swapping them until no swaps are
import time

def bubble_sort_asc(l):
    length = len(l)
    
    if length ==  0 or length == 1:
        return l
        
    for i in range(0, length):
        swapped = False
        
        for j in range(0, length-1-i):
            if l[j] > l[j+1]:
                swapped = True
                l[j], l[j+1] = l[j+1], l[j] 
                
        if swapped == False:
            break 
        
    return l 

def bubble_sort_desc(l):
    length = len(l)
    
    if length == 0 or length == 1:
        return l
    
    for i in range(0, length-1):
        swapped = False
        
        for j in range(0, length-i-1):
            if l[j] < l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                
                swapped = True 
                
        if swapped == False:
            # didn't swap in this iteration
            break
        
    return l

if __name__ == "__main__":
    test_arr = [x for x in range(0,1000)]
    start = time.time()
    print(bubble_sort_desc(test_arr))
    end = time.time()
    ms = end-start
    print("Your code's performance: {} ms".format(str(ms)))


#input size 1000 -> 0.23288702964782715
#input size 10000 -> more than 25 secs
# best for small input sizes
#Time complexity
# BEST - O(n) - when no swaps required
# Average - n^2
# Worst - n^2


 
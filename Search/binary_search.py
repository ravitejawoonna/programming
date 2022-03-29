import time

def binary_search(arr, low, high, element):
    if high >= low:
        #floor division
        mid = (low+high)//2
        
        if arr[mid] == element:
            return mid
        
        #search in the element before the 'mid' index
        elif arr[mid] > element:
            return binary_search(arr, low, mid-1, element)
        
        #search in elements after the 'mid' index
        else:
            return binary_search(arr, mid+1, high, element)
    else:
        return -1

def naive_search(arr, element):
    for i in range(0, len(arr)):
        if arr[i] == element:
            return i
        
    return -1

if __name__ == "__main__":
    test_arr = [x for x in range(0,1000000)]
    start = time.time()
    res  = binary_search(test_arr, 0, len(test_arr), 43367)
    #res =  naive_search(test_arr, 43367)
    print(res)
    end = time.time()
    ms = end-start
    print("Your code's performance: {} ms".format(str(ms)))

##############################################################
#  Binary Search's performance - 0.0009982585906982422 ms
#   - Time Complexity O(log(n))
#
#   Naive Search's performance - 0.003000020980834961 ms 
#   - Time complexity - O(n)
##############################################################
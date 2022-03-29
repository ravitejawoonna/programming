#Given an unsorted array of size n. Array elements are in the range from 1 to n. One number from set {1, 2, …n} is missing and one number occurs twice in the array. Find these two numbers.

import time

def naive_method(arr, n):
    missing_element = None
    repeated_element = None

    counter = {}

    i = 1
    while (missing_element == None and repeated_element == None) and i<=n:
        if missing_element == None:
            if i not in arr:
                missing_element = i
                i = i+1
        
        if str(i) not in counter:
            counter[str(i)] = 1
        
        if str(i) in counter and counter[str(i)] == 1:
            repeated_element = i

        i=i+1

    return {
        "missing_element": missing_element,
        "repeated_element": repeated_element
    }

if __name__ == "__main__":
    test_arr = [1,2,3,4,5,6,7,8,8]

    start = time.time()
    print(naive_method(test_arr, 9))
    end = time.time()
    ms = end-start
    print("Your code's performance: {} ms".format(str(ms)))
# Link: https://practice.geeksforgeeks.org/problems/wave-array-1587115621/1/?page=1&curated[]=2&sortBy=accuracy

# Input 1 2 3 4 5
# Iutput 2 1 3 5 4

def return_wave_array(arr, N):
    
    if N == 0:
        return []
    
    for i in range(0, N-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

if __name__ == "__main__":
    test_arr = [1,2,3,4,5,6,7,8,9,10]
    test_arr = return_wave_array(test_arr, len(test_arr))
    test_arr = [str(i) for i in test_arr]
    print(",".join(test_arr))
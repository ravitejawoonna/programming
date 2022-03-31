# link: https://practice.geeksforgeeks.org/problems/find-the-frequency/1/?page=1&curated[]=2&sortBy=accuracy


def findFrequency (arr, n, x):
    # Your Code Here
    f = 0
    for i in range(0, int(n/2)):
        if arr[i] == x:
            f += 1
        
        if arr[n-i-1] == x:
            f += 1
            
    if n % 2 != 0:
        idx = int(n/2)
        if arr[idx+1] == x:
            f +=1
            
    return f

if __name__ == "__main__":
    test_arr = [2 for i in range(0,1000)]
    print(findFrequency(test_arr, len(test_arr), 2))
#link: https://practice.geeksforgeeks.org/problems/minimum-element-in-a-sorted-and-rotated-array3611/1/?page=1&curated[]=2&sortBy=accuracy#

def findMin(arr, n):
    #complete the function here
    l = int(n/2)
    
    for i in range(0, l):
        if arr[i] > arr[i+1]:
            return arr[i+1]
            
        j = n-i-1
        
        if arr[j] < arr[j-1]:
            return arr[j]
    # if no such condition exists, it should be sorted.
    return arr[0]

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50, 5, 7]
    print(findMin(arr, len(arrr)))
# link: https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1/?page=1&curated[]=2&sortBy=accuracy#

def findMinDiff( A,N,M):
    #sorting
    A.sort()        
    # for i in range(0, N):
    #     swapped = False
        
    #     for j in range(0, N-i-1):
    #         if A[j]> A[j+1]:
    #             A[j+1], A[j] = A[j], A[j+1]
    #             swapped = True
                
    #     if swapped == False:
    #         break
    min_dif = A[N-1]
    left = 0
    right = M-1
    
    while right < N:
        diff = A[right] - A[left]
        if min_dif > diff:
            min_dif = diff
            
        right += 1
        left += 1
    return min_dif

    
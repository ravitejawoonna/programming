# Sort border elements of a square matrix and place them from top left 

def sort_matrix(matrix):
    l = len(matrix)
    #finding edge elements
    eles = []
    
    for i in range(0, l):
        if i == 0 or i == l-1:
            eles = eles + matrix[i]
            continue
            
        eles = eles + [matrix[i][0]]
        eles = eles + [matrix[i][l-1]]

    eles.sort()
    print(eles)
    #adding elements from top left
    
    # top row
    for i in range(0, l):
        matrix[0][i] = eles.pop(0)
        
    # right most
    for i in range(1,l-1):
        matrix[i][l-1] = eles.pop(0)
        
    #bottom row
    for i in range(l-1,-1,-1):
        matrix[l-1][i] = eles.pop(0)
        
    #left most
    for i in range(l-2,0,-1):
        matrix[i][0] = eles.pop(0)
        
    return matrix

if __name__ == "__main__":
    matrix = [
    [99,98,97,96,101],
    [95,94,93,92,102],
    [91,90,89,88,103],
    [87,86,85,84,104],
    [1,2,3,4,5]
    ]
    
    print(sort_matrix(matrix))
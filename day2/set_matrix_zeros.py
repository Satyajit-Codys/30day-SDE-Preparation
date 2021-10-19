

#ask the interiewer if all the values will be zero and ones only or something else

#1st Approach: Brute Force
#first find out the indexes with zero values and add the indexes in two dummy matrix
#then making all the positions zeros

#O(n*m) + O(n*m) Time complexity
#almost O(m) + O(n) space required
     
        rows = len(matrix[0])
        cols = len(matrix)
        i0=[]
        j0 = []
        
        for i in range(cols):
            for j in range(rows):
                if matrix[i][j]==0:
                    if i not in i0:
                        i0.append(i)
                    if j not in j0:
                        j0.append(j)
        
        for i in i0:
            matrix[i] = [0]*rows
        for j in j0:
            for i in range(cols):
                matrix[i][j] = 0
        print(matrix)

#2nd Approach:
#we can improve the time complexity of this approach
# by making 1st row and 1st column as dummy matrix 

m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for a in range(m):
                        if matrix[a][j] != 0:
                            matrix[a][j] = float('inf')
                    for b in range(n):
                        if matrix[i][b] != 0:
                            matrix[i][b] = float('inf')
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0 
        return matrix
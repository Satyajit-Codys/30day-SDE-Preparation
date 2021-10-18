#List Slicing Method

def merge(self,arr1,arr2,m,n):
        arr1.extend(arr2)
        arr1.sort()
        del arr2[:]
        arr2=arr1[n:]
        arr1=arr1[:n]

#2nd Approach : m*n time complexity
'''The idea is simple. Consider each array element X[] and ignore it if it is already in the correct order (i.e., the element smallest among all remaining elements); otherwise, swap it with the smallest element, which happens to be the first element of Y[]. After swapping, move the element (now present at Y[0]) to its correct position in Y[] to maintain the sorted order.'''

def merge(X, Y):
 
    m = len(X)
    n = len(Y)
 
    # Consider each element `X[i]` of list `X[]` and ignore the element if it is
    # already in the correct order; otherwise, swap it with the next smaller
    # element, which happens to be the first element of `Y[]`.
    for i in range(m):
 
        # compare the current element of `X[]` with the first element of `Y[]`
        if X[i] > Y[0]:
 
            # swap `X[i] with `Y[0]`
            temp = X[i]
            X[i] = Y[0]
            Y[0] = temp
 
            first = Y[0]
 
            # move `Y[0]` to its correct position to maintain the sorted
            # order of `Y[]`. Note: `Y[1…n-1]` is already sorted
            k = 1
            while k < n and Y[k] < first:
                Y[k - 1] = Y[k]
                k = k + 1
 
            Y[k - 1] = first
            
 
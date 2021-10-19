#1st Approach

def inversionCount(self, arr, n):
        count = 0
        for i in range(n):
            for j in range(n):
                if arr[i] > arr[j] and i<j:
                    count += 1
        return count

#2nd Approach
#Merge Sort Technique - nlogn time complexity and 1 space complexity

    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
class Solution:
    def merge(self,arr,tmp,l,m,r):
        i = l
        j = m+1
        k = l
        count = 0
        
        while i<=m and j<=r:
            if arr[i]<=arr[j]:
                tmp[k] = arr[i]
                k+=1
                i+=1
            else:
                tmp[k] = arr[j]
                count += (m-i+1)
                k += 1
                j += 1
        
        while i<= m:
            tmp[k] = arr[i]
            k += 1
            i += 1
        
        while j<=r:
            tmp[k] = arr[j]
            k += 1
            j += 1
        
        for v in range(l,r+1):
            arr[v] = tmp[v]
        return count
    
    def merge_sort(self,arr,tmp,l,r):
        count = 0
        if l < r:
            m = (l+r)//2
            
            count += self.merge_sort(arr,tmp,l,m)
            count += self.merge_sort(arr,tmp,m+1,r)
            
            count += self.merge(arr,tmp,l,m,r)
        return count
    
    def inversionCount(self, arr, n):
        tmp = [0]*n
        return self.merge_sort(arr,tmp,0,n-1)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))

#}Driver Code Ends
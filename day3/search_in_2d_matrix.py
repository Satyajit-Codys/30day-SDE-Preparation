#1st Method
#It iterates through the whole list of lists to find out the target value 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return target in sum(matrix, [])


#2nd method
#binary search reduce the time complexity

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search on the matrix rows - not expected to find an exact match
        a = 0
        b = len(matrix)
        while b > a + 1:
	        mid = (b + a) // 2
	        if matrix[mid][0] == target:
		        return True
	        if matrix[mid][0] < target:
		        a = mid
	        elif matrix[mid][0] > target:
		        b = mid

# binary search on the found row
        rel_row = matrix[a]
        a = 0
        b = len(rel_row)
        while b > a:
	        mid = (b + a) // 2
	        if rel_row[mid] == target:
		        return True
	        if rel_row[mid] < target:
		        a = mid + 1
	        elif rel_row[mid] > target:
		        b = mid

        return rel_row[mid] == target
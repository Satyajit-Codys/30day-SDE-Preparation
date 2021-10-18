#1st Approach:
    # nlogn + n +n time complexity
    # 1 space complexity
def findTwoElement( self,arr, n): 
        arr.sort()
        res= []
        index_sum = 0
        for i in range(1,n):
            if arr[i] == arr[i-1]:
                res.append(arr[i])
        for j in range(1,n+1):
            index_sum += j
        print(index_sum, sum(arr), res[0])
        res.append(index_sum - (sum(arr)-res[0]))
        return res

		
#2nd Approach
    # n time complexity &  n space complexity
def findTwoElement( self,arr, n): 
        set_arr = list(set(arr))
        res = []
        res.append(sum(arr) - sum(set_arr))
        res.append(n*(n+1)//2 - sum(set_arr))
        return res


# 3rd Approach
def printTwoElements( arr, size):
	for i in range(size):
		if arr[abs(arr[i])-1] > 0:
			arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
		else:
			print("The repeating element is", abs(arr[i]))
			
	for i in range(size):
		if arr[i]>0:
			print("and the missing element is", i + 1)



# 4th Approach : Uisng XOR
def getTwoElements(arr, n):
	
	global x, y
	x = 0
	y = 0
	
	# Will hold xor of all elements
	# and numbers from 1 to n
	xor1 = arr[0]
	
	# Get the xor of all array elements
	for i in range(1, n):
		xor1 = xor1 ^ arr[i]
		
	# XOR the previous result with numbers
	# from 1 to n
	for i in range(1, n + 1):
		xor1 = xor1 ^ i
	
	# Will have only single set bit of xor1
	set_bit_no = xor1 & ~(xor1 - 1)
	
	# Now divide elements into two
	# sets by comparing a rightmost set
	# bit of xor1 with the bit at the same
	# position in each element. Also,
	# get XORs of two sets. The two
	# XORs are the output elements.
	# The following two for loops
	# serve the purpose
	for i in range(n):
		if (arr[i] & set_bit_no) != 0:
			
			# arr[i] belongs to first set
			x = x ^ arr[i]
		else:
			
			# arr[i] belongs to second set
			y = y ^ arr[i]
			
	for i in range(1, n + 1):
		if (i & set_bit_no) != 0:
			
			# i belongs to first set
			x = x ^ i
		else:
			
			# i belongs to second set
			y = y ^ i
		
	# x and y hold the desired
	# output elements

# 5th Approach: using Maps
def main():
	
	arr = [ 4, 3, 6, 2, 1, 1 ]
	
	numberMap = {}
	
	max = len(arr)
	for i in arr:
		if not i in numberMap:
			numberMap[i] = True
			
		else:
			print("Repeating =", i)
	
	for i in range(1, max + 1):
		if not i in numberMap:
			print("Missing =", i)
main()

# This code is contributed by stutipathak31jan


nums = list(map(int, input().split()))
n = len(nums)


# 1st Approach - n3 time complexity
'''
suma = 0
maximum = 0
for i in range(n):
    for j in range(i,n,1):
        for k in range(i,j+1,1): #this loop will run from i to j
            suma += nums[k]
            print("k", i,j, nums[k])
        print("sum",suma)
        maximum = max(suma,maximum)
        suma = 0

print("res",maximum)
'''

# Optimized Approach - n2 time complexity 

# what I did is, remove the for loop for k and in that place
#uses sum addition and check.
'''
suma = 0
maximum = 0
for i in range(n):
    suma = 0
    for j in range(i,n,1):
        suma += nums[j]
        maximum = max(suma,maximum)
print("res",maximum)
'''

#Kadane's Algorithm - Linear time complexity & O(1) space complexity
#we're initializing the maximum with the first element of the nums array
#then we're iterating the array 
#and checking if after the sum the sum of subarray is greater than the current maximum or not
#if the sum is negative then make it zero
#and if the sum is positive thencarry forward
#this is the main essence of the kadane algorithm
suma = 0
maxi = nums[0]
for i in range(n):
    suma += nums[i]
    maxi = max(suma,maxi)
    if suma<0: suma =0
print(maxi)




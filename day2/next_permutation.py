#1st Approach: 
# iterate the array in reverse order and set breakpoint when array[index-1] becomes greater than array[index]
# now replace the value 
#and return the other part of the array in reversed order 

 def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        index, next = -1, 0
        for i in reversed(range(1,n)):
            if nums[i-1] < nums[i]:
                index = i-1
                break
        
        if index == -1:
            nums.reverse()
        else:
            for i in reversed(range(n)):
                if nums[i] > nums[index]:
                    next = i
                    break
            nums[index], nums[next] = nums[next], nums[index]
            self.reverse(nums,index+1)
    
	#function to reverse the list from given index
    def reverse(self, arr, start):
        end = len(arr)-1
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
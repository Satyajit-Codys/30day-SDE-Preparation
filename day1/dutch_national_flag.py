class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 1st Solution : simple nlogn sort
        # nums.sort()
        
        #2nd solution: count the occurances
        # zeros = 0
        # ones = 0
        # twos = 0
        # for num in nums:
        #     if num ==0:
        #         zeros += 1
        #     elif num == 1:
        #         ones += 1
        #     else:
        #         twos +=1
        # for i in range(len(nums)):
        #     if zeros != 0:
        #         nums[i] = 0
        #         zeros-=1
        #     elif ones !=0:
        #         nums[i]= 1
        #         ones-=1
        #     else:
        #         nums[i] = 2
        
        #3rd approach using pointer (n time complexity- o(1) space)
        low,mid =0,0
        high = len(nums)-1
        while(mid <= high):
            if nums[mid] ==0:
                nums[low] , nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] ==1:
                mid += 1 
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        
            
# Problem Statement Link : https://leetcode.com/problems/sort-colors/
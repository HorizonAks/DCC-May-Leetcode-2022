#Day 2.
#905. Sort Array By Parity

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left,right = 0,len(nums)-1
        while(left < right):
            if nums[left]%2!=0:
                while(left < right and nums[right]%2!=0):
                    right-=1
                nums[right],nums[left] = nums[left],nums[right]
            else:
                left+=1
        return nums

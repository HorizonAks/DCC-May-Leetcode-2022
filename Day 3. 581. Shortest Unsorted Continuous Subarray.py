#Day 3.
#581. Shortest Unsorted Continuous Subarray

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        chk = sorted(nums)
        if chk == nums:
            return 0
        else:
            low = 0
            while(chk[low] == nums[low]):
                low+=1
            high = len(nums)-1
            while(chk[high] == nums[high]):
                high-=1
            return (high-low) + 1

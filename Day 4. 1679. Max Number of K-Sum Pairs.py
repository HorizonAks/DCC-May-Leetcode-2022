#Day 4.
#1679. Max Number of K-Sum Pairs

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        low, high = 0, len(nums)-1
        count= 0
        while low < high:
            curr = (nums[low]+nums[high])
            if curr == k:
                count+=1
                low+=1
                high-=1
            elif (curr < k):
                low+=1
            else:
                high-=1
        return count

                

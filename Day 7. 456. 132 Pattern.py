#Day 7.
#456. 132 Pattern

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        #create an array with minimum element till ith index
        minarr = []
        mink = float('inf')
        for i in nums:
            mink = min(mink,i)
            minarr.append(mink)
        #create a stack
        stack = []
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > minarr[i]:
                while stack and stack[-1] <= minarr[i]:
                    stack.pop()
                    #pop until element greater than minimum is on top of the stack
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        return False

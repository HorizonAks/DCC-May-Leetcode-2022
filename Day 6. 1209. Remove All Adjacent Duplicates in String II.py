#Day 6.
#1209. Remove All Adjacent Duplicates in String II

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        #create a stack
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append([s[i],1])
                continue
            #peek stack and check character and count
            if stack[-1][0] == s[i]:
                if stack[-1][1] == k-1:
                    #remove if count == k
                    stack.pop()
                else:
                    #increment count
                    stack[-1][1]+=1
                continue
            #not same append new pair
            stack.append([s[i],1])
            
        #loop to convert stack pair into og string
        res = ""
        
        for ch,val in stack:
            res += ch*val
        
        return res

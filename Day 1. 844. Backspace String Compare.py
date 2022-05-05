#Day1.
#844. Backspace String Compare

#simple stack implemetation
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        diff = min(len(s),len(t))
        for i in range(diff):
            if s[i] == '#':
                if len(stack_s) > 0:
                    stack_s.pop()
            else:
                stack_s.append(s[i])
            if t[i]== '#':
                if len(stack_t) > 0:
                    stack_t.pop()
            else:
                stack_t.append(t[i])
        for i in range(diff,len(s)):
            if s[i] == '#':
                if len(stack_s) > 0:
                    stack_s.pop()
            else:
                stack_s.append(s[i])
        for i in range(diff,len(t)):
            if t[i] == '#':
                if len(stack_t) > 0:
                    stack_t.pop()
            else:
                stack_t.append(t[i])
        #rint(stack_s,stack_t)
        return stack_s == stack_t
            

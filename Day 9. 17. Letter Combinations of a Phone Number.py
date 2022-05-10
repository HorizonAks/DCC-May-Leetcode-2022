#Day 9
#17. Letter Combinations of a Phone Number


from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numpad = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        n = i = len(digits)
        crS = []
        while(i):
            if not crS:
                crS = list(numpad[digits[n-i]])
            else:
                ncrS = [x+y for x,y in product(crS,list(numpad[digits[n-i]]))]
                crS = ncrS
            i-=1
        return crS
                

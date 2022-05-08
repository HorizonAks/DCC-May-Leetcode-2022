#Day 8.
#341. Flatten Nested List Iterator


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.itr = []
        self.ptr = -1
        self.recurse(nestedList)
    
    def recurse(self,nL):
        if type(nL) == type(1):
            self.itr.append(nL)
        elif type(nL) == type([2]):
            for i in nL:
                self.recurse(i)
        else:
            if nL.isInteger():
                self.itr.append(nL.getInteger())
            else:
                self.recurse(nL.getList())
            
    
    def next(self) -> int:
        self.ptr += 1
        return self.itr[self.ptr]
    
    def hasNext(self) -> bool:
        if self.ptr < len(self.itr)-1:
            return True
        return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

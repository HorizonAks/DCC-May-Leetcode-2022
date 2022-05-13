#Day 11
#1641. Count Sorted Vowel Strings

class Solution:
    def countVowelStrings(self, n: int) -> int:
        @cache
        def dp(n,k):
            if n == 1 or k == 1:
                return k
            return sum(dp(n - 1, k) for k in range(1, k + 1))
        return dp(n,5)

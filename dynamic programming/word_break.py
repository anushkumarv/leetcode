from typing import List

class SolutionBruteForce:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def recursive(sub, s, wordDict):
            if len(sub) > len(s):
                return False

            if sub == s:
                return True

            val = False
            if sub == s[:len(sub)]:
                for word in wordDict:
                    val = val or recursive(sub + word, s, wordDict)
            else:
                return False

            return val

        return recursive("", s, wordDict)


sol = SolutionBruteForce()
## time complexity - O(n^n)
## space complexity - O(n)
print(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)

        word_set = set(wordDict)

        dp[0] = (s[0] in word_set)

        for i in range(1, len(s)):
            for j in range(i-1, -1, -1):
                if dp[j]:
                    dp[i] = (s[:j+1] + s[j+1:i+1] in word_set) or (s[j+1:i+1] in word_set)
                else:
                    dp[i] = (s[:i+1] in word_set)

                if dp[i]:
                    break

        return dp[-1]


sol = SolutionBruteForce()
## time complexity - O(n^3)
## space complexity - O(n)
print(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
## Brute Force ##
class SolutionBruteForce:
    def groupAnagrams(self, strs):
        anagram_dict = dict()
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
        
        op = []
        for key in anagram_dict:
            op.append(anagram_dict[key])
            
        return op
        

## Slightly Optimised ##
class Solution:
    def groupAnagrams(self, strs):
        anagram_dict = dict()
        for word in strs:
            char_arr = [0] * 26
            for char in word:
                char_arr[ord(char) - ord('a')] += 1
            key = tuple(char_arr)
            if key in anagram_dict:
                anagram_dict[key].append(word)
            else:
                anagram_dict[key] = [word]

        return anagram_dict.values()

## Brute Force ##
sol_bf = SolutionBruteForce()
## time complexity - O(n * klogk)
## space complexity - O(n)
print('## Brute Force ##')
print(sol_bf.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

## Slightly Optimised ##
sol = Solution()
## time complexity - O(n * k)
## space complexity - O(n)
print('## Slightly optimised ##')
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

## Outputs ##
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

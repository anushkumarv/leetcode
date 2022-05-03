class Solution:
    def isAnagram(self, s, t):
        
        if len(s) != len(t):
            return False 
        
        char_count_s = self.get_char_count_word(s)
        char_count_t = self.get_char_count_word(t)
        
        if len(char_count_s.keys()) != len(char_count_t.keys()):
            return False 
        
        for key in char_count_s:
            if key not in char_count_t or char_count_s[key] != char_count_t[key]:
                return False
            
        return True
        
        
    def get_char_count_word(self, word):
        
        char_count = dict()
        for char in word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
                
        return char_count
        

sol = Solution()
print(sol.isAnagram("rat","car"))
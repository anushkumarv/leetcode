class Solution:
    def containsDuplicate(self, nums):
        
        item_set = set()
        
        for item in nums:
            if item in item_set:
                return True
            else:
                item_set.add(item)
            
        return False 


# Example test cases
sol = Solution()
## time complexity - O(n)
## space complexity - O(n)
print(sol.containsDuplicate([1,2,3,1]))
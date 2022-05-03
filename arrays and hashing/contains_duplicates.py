class Solution:
    def containsDuplicate(self, nums):
        
        item_counts = dict()
        
        for item in nums:
            if item in item_counts:
                item_counts[item] += 1
            else:
                item_counts[item] = 1
                
        for key in item_counts:
            if item_counts[key] > 1:
                return True 
            
        return False 


# Example test cases
sol = Solution()
## time complexity - O(n)
## space complexity - O(n)
print(sol.containsDuplicate([1,2,3,1]))
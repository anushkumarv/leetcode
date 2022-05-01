### Brute Force Approach ###
class SolutionBruteForce:
    def maxArea(self, height):

        max_area = float("-inf")
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                length = height[i] if height[i] < height[j] else height[j]
                breadth = j - i 
                area = length * breadth
                max_area = area if area > max_area else max_area
                
        return max_area
        


### Two pointer approach ###
class Solution:
    def maxArea(self, height):
        ### two pointer approach ###
        left = 0
        right  = len(height) - 1
        max_area = float("-inf")
        while(left < right or left != right):
            # Compute area 
            length  = right - left 
            breadth  = min(height[left], height[right])
            # breadth = height[left] if height[left] < height[right] else height[right]
            area = length * breadth
            max_area = max(area, max_area)
            # Update pointers
            if height[left] < height [right]:
                left += 1 
            else:   
                right -=1 
                
        return max_area


# Example test cases
## Brute Force ##
sol_bf = SolutionBruteForce()
## time complexity - O(n^2)
## space complexity - O(n)
print(sol_bf.maxArea([1,8,6,2,5,4,8,3,7]))
print(sol_bf.maxArea[1,1])

## Two Pointer 
sol = Solution()
## time complexity - O(n)
## space complexity - O(n)
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
print(sol.maxArea([1,1]))
        
# Output 
# 49
# 1
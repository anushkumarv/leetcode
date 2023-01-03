from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def choose_row(l, r):
            while l <= r:
                mid = (l + r) // 2
                print(l,r,mid)
                if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                    return mid
                elif target >= matrix[mid][-1]:
                    l = mid + 1
                elif target <= matrix[mid][0]:
                    r = mid - 1
            
            return -1

        def binary_search(l, r, row):
            while l <= r:
                mid = (l + r) // 2
                if target == row[mid]:
                    return True
                elif target > row[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return False

        row = choose_row(0, len(matrix)-1)
        if row != -1:
            return binary_search(0, len(matrix[row])-1, matrix[row])
        else:
            return False


sol = Solution()
## time complexity - O(log m * n)
## space complexity - O(1)
print(sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
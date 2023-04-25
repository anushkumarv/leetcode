from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = list()
        def pascals_triangle(row, max_row, prev_row):
            if row > max_row:
                return res
            next_row = [1]
            for i in range(1,len(prev_row)):
                next_row.append(prev_row[i-1] + prev_row[i])
            next_row.append(1)

            res.append(next_row)
            return pascals_triangle(row+1, max_row, next_row)

        res.append([1])
        return pascals_triangle(2, numRows, [1])
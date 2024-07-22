from collections import Counter, deque
from heapq import heappush, heappop
from typing import List, Optional

# #####
# https://leetcode.com/problems/intersection-of-two-arrays-ii
# #####

class Solution1Jul:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1c = Counter(nums1)
        n2c = Counter(nums2)
        res = []
        for n, count in n1c.items():
            if n in n2c:
                temp = [n] * min(count, n2c[n])
                res.extend(temp)
        return res
    

# #####
# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves
# #####

class Solution2Jul:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        small_4 = list()
        big_4 = list()
        for _, num in enumerate(nums):
            heappush(small_4, -num)
            if len(small_4) > 4:
                heappop(small_4)

            heappush(big_4, num)
            if len(big_4) > 4:
                heappop(big_4)

        res = float("inf")
        small_4 = [-1*num for num in small_4]
        small_4.sort()
        big_4.sort()
        for i in range(4):
            res = min(res, big_4[i] - small_4[i])

        return res
    

# #####
# https://leetcode.com/problems/merge-nodes-in-between-zeros
# #####

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution3Jul:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        cur = head.next
        prev = dummy
        s = 0
        while cur:
            if cur.val == 0:
                prev.next = ListNode(s)
                prev = prev.next
                s = 0
            else:
                s += cur.val
            cur = cur.next
        return dummy.next
    
# #####
# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/
# #####

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution4Jul:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        i = 0
        cur = head
        prev_node, cur = None, head
        first, last, prev = None, None, None
        min_dist = float("inf")
        
        while cur:
            if prev_node \
               and cur.next \
               and (prev_node.val < cur.val > cur.next.val \
                    or prev_node.val > cur.val < cur.next.val):
                first = i if not first else first
                last = i
                min_dist = min(min_dist, i - prev) if prev else min_dist
                prev = i

            prev_node = cur
            cur = cur.next
            i += 1

        return [min_dist, last - first] if min_dist != float("inf") else [-1, -1] 

# #####
# https://leetcode.com/problems/pass-the-pillow
# #####

class Solution5Jul:
    def passThePillow(self, n: int, time: int) -> int:
        cycle_time = n - 1
        cycles = time // cycle_time
        position = time % cycle_time
        if cycles & 1:
            return n - position
        return 1 + position
    
# #####
# https://leetcode.com/problems/water-bottles
# #####

class Solution6Jul:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        full_b, emp_b = numBottles, 0
        count = 0
        while full_b > 0:
            count += full_b
            emp_b += full_b
            full_b = emp_b // numExchange
            emp_b = emp_b % numExchange
        return count

# #####
# https://leetcode.com/problems/find-the-winner-of-the-circular-game
# #####

class Solution7Jul:
    def findTheWinner(self, n: int, k: int) -> int:
        prev = 0
        for i in range(2, n+1):
            prev = (prev + k) % i
        return prev + 1

# #####
# https://leetcode.com/problems/average-waiting-time
# #####    

class Solution8Jul:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        prev_stime, prev_etime = customers[0][0], customers[0][0] + customers[0][1]
        wt = prev_etime - prev_stime
        
        for i in range(1, len(customers)):
            prev_etime = max(prev_etime, customers[i][0])
            etime = prev_etime + customers[i][1]
            wt += etime - customers[i][0] 
            prev_etime = etime

        return wt / len(customers)

# #####
# https://leetcode.com/problems/crawler-log-folder
# #####

class Solution9Jul:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for op in logs:
            if op == "../":
                depth -= 1
            elif op == "./":
                continue
            else:
                depth += 1
            depth = max(depth, 0)
        return depth

# #####
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses
# ####


class Solution10Jul:
    def reverseParentheses(self, s: str) -> str:
        d = {}
        stk = []
        for i, c in enumerate(s):
            if c == ')':
                start = stk.pop()
                d[start] = i
                d[i] = start
            elif c == '(':
                stk.append(i)

        res = []
        dir_ = 1
        i = 0
        while i < len(s):
            if s[i] == '(' or s[i] == ')':
                i = d[i]
                dir_ = -dir_
            else:
                res.append(s[i])
            i += dir_
        return ''.join(res)
    
# #####
# https://leetcode.com/problems/maximum-score-from-removing-substrings
# ####    

class Solution11Jul:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            s, res1 = self.patternPoints(s, "ab", x)
            _, res2 = self.patternPoints(s, "ba", y)
        else:
            s, res1 = self.patternPoints(s, "ba", y)
            _, res2 = self.patternPoints(s, "ab", x)
        return res1 + res2
    
    def patternPoints(self, s, pattern, points):
        count = 0
        stk = []
        for c in s:
            stk.append(c)
            if len(stk) >= 2 and stk[-1] == pattern[-1] and stk[-2] == pattern[-2]:
                stk.pop()
                stk.pop()
                count += points
        return ''.join(stk), count

# #####
# https://leetcode.com/problems/robot-collisions
# ####    

class Robot:
    def __init__(self, position, health, direction, weight):
        self.position = position
        self.health = health
        self.direction = direction
        self.weight = weight

    def __lt__(self, robot):
        return self.position < robot.position
    
    def __repr__(self):
        return f"(pos: {self.position}, health: {self.health}, dir: {self.direction})"

class Solution12Jul:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = [Robot(positions[i], healths[i], directions[i], i) for i in range(n)]
        robots.sort()
        stk = []
        for robot in robots:
            while stk and stk[-1].direction == "R" and robot.direction == "L":
                prev_robot = stk.pop()
                if prev_robot.health == robot.health:
                    robot = None
                    break
                new_dir = "R" if prev_robot.health > robot.health else "L"
                new_health = prev_robot.health - 1 if prev_robot.health > robot.health else robot.health - 1
                new_weight = prev_robot.weight if prev_robot.health > robot.health else robot.weight
                robot.direction = new_dir
                robot.health = new_health
                robot.weight = new_weight
            if robot:
                stk.append(robot)
        stk.sort(key=lambda robot: robot.weight)
        return [robot.health for robot in stk]
    
# #####
# https://leetcode.com/problems/number-of-atoms
# ####    

class Solution13Jul:
    def countOfAtoms(self, formula: str) -> str:
        f_arr = []
        i = 0
        for i in range(len(formula)):
            ch = formula[i]
            if ch.islower() and f_arr:
                f_arr[-1] = f_arr[-1] + ch
                continue
            elif ch.isdigit() and f_arr and f_arr[-1].isdigit():
                f_arr[-1] = f_arr[-1] + ch
                continue

            if ch.isupper() and f_arr and not f_arr[-1].isdigit():
                if f_arr[-1] != "(":
                    f_arr.append(str(1))
            elif ch == ")" and f_arr and not f_arr[-1].isdigit() and f_arr[-1] != "(" and f_arr[-1] != ")":
                f_arr.append(str(1))
            elif ch == "(" and f_arr and not f_arr[-1].isdigit() and not f_arr[-1] == "(" and f_arr[-1] != ")":
                f_arr.append(str(1))
            f_arr.append(ch)
            
        if f_arr[-1].isupper():
            f_arr.append(str(1))

        stk = []
        bstk = []
        for i, ch in enumerate(f_arr):
            if ch.isdigit() and stk and stk[-1] == ")":
                for i in range(len(stk)-1,bstk[-1],-1):
                    if stk[i].isdigit():
                        stk[i] = str(int(stk[i]) * int(ch))
                bstk.pop()  
                stk.append("@")   
            else:
                if ch == "(":
                    bstk.append(i)
                stk.append(ch)

        d = {}
        for i, item in enumerate(stk):
            if item == "(" or item == ")" or item == "@":
                continue
            if not item.isdigit():
                d[item] = d.get(item, 0)
            else:
                key = stk[i-1]
                d[key] += int(item)
        
        keys = list(d.keys())
        keys.sort()
        res = []
        for key in keys:
            if d[key] == 1:
                res.append(key)
            else:
                res.append(key + str(d[key]))
        return "".join(res)

# #####
# https://leetcode.com/problems/create-binary-tree-from-descriptions
# ####    

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution14Jul:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d = {}
        non_roots = set()
        for parent, child, isleft in descriptions:
            if parent not in d:
                d[parent] = TreeNode(parent)
            if child not in d:
                d[child] = TreeNode(child)
            pnode, cnode = d[parent], d[child]
            if isleft:
                pnode.left = cnode
            else:
                pnode.right = cnode
            non_roots.add(child)

        for key in d:
            if key not in non_roots:
                return d[key]

        return

# #####
# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another
# ####    

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution15Jul:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node, target, path):
            if not node:
                return False
            if node.val == target:
                path.append((node.val, "C"))
                return True

            path.append((node.val, "L"))
            if dfs(node.left, target, path):
                return True
            path.pop()

            path.append((node.val, "R"))
            if dfs(node.right, target, path):
                return True
            path.pop()

            return False

        startpath = []
        dfs(root, startValue, startpath)
        
        endpath = []
        dfs(root, destValue, endpath)
        
        i = 0
        while i < len(startpath) and i < len(endpath) and startpath[i][0] == endpath[i][0]:
            i += 1
        i -= 1

        res = ["U"] * (len(startpath) - i - 1)
        while i < len(endpath) - 1:
            res.append(endpath[i][1])
            i += 1
        return "".join(res)
    
# #####
# https://leetcode.com/problems/delete-nodes-and-return-forest
# ####    

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution16Jul:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        to_delete = set(to_delete)
        def dfs(node, prev_node):
            if node == None:
                return
            
            if prev_node == None and node.val not in to_delete:
                res.append(node)
                    
            prev_node = node if node.val not in to_delete else None
            dfs(node.left, prev_node)
            if node.left and node.left.val in to_delete:
                node.left = None
            dfs(node.right, prev_node)
            if node.right and node.right.val in to_delete:
                node.right = None

        dfs(root, None)
        return res
    
# #####
# https://leetcode.com/problems/lucky-numbers-in-a-matrix
# ####    

class Solution17Jul:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mins, maxs = [], []
        for row in matrix:
            mins.append(min(row))

        for j in range(len(matrix[0])):
            temp = matrix[0][j]
            for i in range(len(matrix)):
                temp = max(temp, matrix[i][j])
            maxs.append(temp)

        res = []
        for i in range(len(mins)):
            for j in range(len(maxs)):
                if mins[i] == maxs[j]:
                    res.append(mins[i])

        return res
    
# #####
# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums
# ####  

class Solution18Jul:
    def restoreMatrix(self, rowSum, colSum):
        N = len(rowSum)
        M = len(colSum)

        orig_matrix = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                orig_matrix[i][j] = min(rowSum[i], colSum[j])

                rowSum[i] -= orig_matrix[i][j]
                colSum[j] -= orig_matrix[i][j]

        return orig_matrix

# #####
# https://leetcode.com/problems/build-a-matrix-with-conditions
# ####  

class Node:
    def __init__(self, val):
        self.val = val
        self.inedge = set()
        self.outedge = set()


class Solution19Jul:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_order = self.get_order_preference(k, rowConditions)
        col_order = self.get_order_preference(k, colConditions)
        if len(row_order) != k or len(col_order) != k:
            return []

        d = {i+1:[] for i in range(k)}
        for i, val in enumerate(row_order):
            d[val].append(i)
        for i, val in enumerate(col_order):
            d[val].append(i)

        res = [[0]*k for i in range(k)]
        for k in d:
            i, j = d[k][0], d[k][1]
            res[i][j] = k

        return res

    def get_order_preference(self, k, conditions):
        nodes = [Node(i+1) for i in range(k)]
        for before, after in conditions:
            src = nodes[before-1]
            tgt = nodes[after-1]
            src.outedge.add(tgt)
            tgt.inedge.add(src)
            
        q = deque()
        for node in nodes:
            if len(node.inedge) == 0:
                q.append(node)
        
        res = []
        while q:
            node = q.pop()
            res.append(node.val)
            for out_node in node.outedge:
                out_node.inedge.remove(node)
                if len(out_node.inedge) == 0:
                    q.append(out_node)

        return res
    
# #####
# https://leetcode.com/problems/sort-the-people
# ####  

class Solution20Jul:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hn = [(heights[i], names[i]) for i in range(len(heights))]
        hn.sort(reverse=True)
        return [item[1] for item in hn]
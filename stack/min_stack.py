## The below solution is based on updating the min value each time a push and pop operation are made
class MinStack:

    def __init__(self):
        self.stk = list()
        self.min_idx = None
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.stk) == 1:
            self.min_idx = 0
        else: 
            self.min_idx = len(self.stk) - 1 if val < self.stk[self.min_idx] else self.min_idx

    def pop(self) -> None:
        if self.min_idx != len(self.stk) - 1:
            self.stk.pop()
        else:
            self.stk.pop()
            self.update_min_idx()

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.stk[self.min_idx]
    
    def update_min_idx(self):
        if len(self.stk) == 0:
            self.min_idx = None
        else:
            self.min_idx = 0
            for i in range(len(self.stk)):
                self.min_idx = i if self.stk[i] < self.stk[self.min_idx] else self.min_idx
            

## The below solution is based out of a hint from leetcode where we maintain the latest min value each time we add an item to the stack                
class MinStack:

    def __init__(self):
        self.stk = list()

    def push(self, val: int) -> None:
        if len(self.stk) == 0:
            self.stk.append((val, val))
        else:
            cur_min_val = self.stk[-1][1]
            new_min_val = cur_min_val if cur_min_val < val else val
            self.stk.append((val, new_min_val))

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]
        

## Time complexity - O(1) for push, pop, getMin
## Space complexity - O(n) 
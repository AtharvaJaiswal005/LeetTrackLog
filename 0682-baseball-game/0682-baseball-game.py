class Solution:
    def calPoints(self, ops: List[str]) -> int:
        from collections import deque
        stack=deque()
        for i in ops:
            try:
                stack.append(int(i))
            except:
                if i=="C":
                    stack.pop()
                elif i=="D":
                    stack.append(stack[-1]*2)
                elif i=="+":
                    stack.append(stack[-1]+stack[-2])
        return sum(stack)
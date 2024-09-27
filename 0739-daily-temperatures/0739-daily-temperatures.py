class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        from collections import deque
        stack=deque()
        res=[0]*len(temperatures)
        v=temperatures[0]
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                p=stack.pop()
                res[p]=(i-p)
            stack.append(i)
        return res
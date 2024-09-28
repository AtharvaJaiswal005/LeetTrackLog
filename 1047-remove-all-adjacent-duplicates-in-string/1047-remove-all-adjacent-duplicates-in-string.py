class Solution:
    def removeDuplicates(self, s: str) -> str:
        from collections import deque
        stack=deque()
        for i in s:
            if stack and stack[-1]==i:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(list(stack))
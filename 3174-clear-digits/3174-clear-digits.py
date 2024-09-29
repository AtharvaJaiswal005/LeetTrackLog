class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i].isdigit() and stack and stack[-1].isalpha():
                stack.pop()
            else:
                stack.append(s[i])
        return ''.join(stack)
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import deque
        
        q = deque(students)
        s = sandwiches
        i = 0
        cnt = 0
        
        while q and cnt < len(q):
            if q[0] == s[i]:
                q.popleft()
                i += 1
                cnt = 0
            else:
                q.append(q.popleft())
                cnt += 1
        
        return len(q)

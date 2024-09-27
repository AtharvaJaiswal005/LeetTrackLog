class MinStack:

    def __init__(self):
        self.main_stack = [] 
        self.tracker = []     

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        
        if  not self.tracker or val <= self.tracker[-1]:
            self.tracker.append(val)

    def pop(self) -> None:
        if self.main_stack[-1] == self.tracker[-1]:
            self.tracker.pop()
        self.main_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.tracker[-1]

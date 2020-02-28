class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
        else:
            return 0

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return 0

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return min(self.stack)
        else:
            return 0


if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(3)
    obj.push(2)
    obj.push(1)
    obj.pop()
    assert obj.top() != None
    assert obj.getMin() == 2

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stck = []

    def push(self, x: int) -> None:
        self.stck.append(x)

    def pop(self) -> None:
        if self.stck is not None:
            self.stck.pop(-1)

    def top(self) -> int:
        if self.stck is not None:
            return self.stck[-1]

    def getMin(self) -> int:
        if self.stck is not None:
            return min(self.stck)

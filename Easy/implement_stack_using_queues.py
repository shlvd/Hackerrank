class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._queue=[]
    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self._queue.append(x)
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        for i in range(len(self._queue)-1):
            self._queue.append(self._queue.pop(0))
        return self._queue.pop(0)
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        top=None
        for i in range(len(self._queue)):
            top=self._queue.pop(0)
            self._queue.append(top)
        return top
    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self._queue==[] 

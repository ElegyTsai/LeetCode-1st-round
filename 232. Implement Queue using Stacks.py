class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack=[[],[]]
        self.ps=0
        self.pp=1


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack[self.ps].append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.stack[self.pp]:
            return self.stack[self.pp].pop()
        else:
            while self.stack[self.ps]:
                self.stack[self.pp].append(self.stack[self.ps].pop())
            return self.stack[self.pp].pop()


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stack[self.pp]:
            return self.stack[self.pp][-1]
        else:
            while self.stack[self.ps]:
                self.stack[self.pp].append(self.stack[self.ps].pop())
            return self.stack[self.pp][-1]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.stack[1]) == 0 and len(self.stack[0]) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
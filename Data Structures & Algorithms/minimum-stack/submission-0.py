class MinStack:

    def __init__(self):
        self.values = []
        self.mins = []

    def push(self, val: int) -> None:
        """
        pushed val onto stack
        """
        self.values.append(val)

        # if mins is empty or value is less than current min
        if not self.mins or val <= self.mins[-1]:
            self.mins.append(val) # add to mins as new min

        else:
            self.mins.append(self.mins[-1])


    def pop(self) -> None:
        """
        removes the element at the top of the stack
        - always called on non empty stacks
        """
        item = self.values.pop()

        self.mins.pop()

    def top(self) -> int:
        """
        returns top element of the stack
        - always called on non empty stacks
        """
        return self.values[len(self.values) - 1]
        
    def getMin(self) -> int:
        """
        returns minimum element in the stack
        - always called on non empty stacks
        """
        return self.mins[-1]
        

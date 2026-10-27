class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        constraints state: no unexpected characters, valid arithmetic expression
        RPN: operators follow their operands
        - typical 3 + 4 becomes in RPN 3 4 +
        - each operator has two operands

        for nested operations
        ((1+2)*3)-4 becomes 1 2 + 3 * 4 -
        - the last added element/first popped is an operator, 
            - considering recursion

        (3 + 4) × (5 + 6) becomes 3 4 + 5 6 + ×

        - token given as list of strings

        pseudocode:
        dictionary mapping 'operation' to ...? (how to convert '+' to action)
        while tokens:
            op = tokens.pop() # first pop returns first operator
            x = tokens.pop() # next pop: if operator, recurse, if operand, perform

        **new approach**
        go from front of list (idk why i forgot i could do that)
        """
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a/b)
        }

        store = []
        for t in tokens:
            if t in ops: # if t is an operator
                b = store.pop() # last item added to store is the second operand
                a = store.pop()
                store.append(ops[t](a, b))
            else: # if t is an operand
                store.append(int(t))

        return store[0]

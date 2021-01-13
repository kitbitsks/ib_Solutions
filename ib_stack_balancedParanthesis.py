class Solution:
    # @param A : string
    # @return an integer
    def push(self, stack, elem):
        stack.append(elem)
    
    def pop(self, stack):
        return stack.pop()

    def solve(self, A):
        if A == '))':
            return 0
        stack = []
        x = range(0,len(A))
        for elem in x:
            if A[elem] == '(':
                self.push(stack, A[elem])
            else:
                if stack != []:
                    self.pop(stack)
                else:
                    self.push(stack,A[elem])
        if stack == []:
            return 1
        else:
            return 0
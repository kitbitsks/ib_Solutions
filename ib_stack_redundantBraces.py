class Solution:
    # @param A : string
    # @return an integer
    def push(self, stack, elem):
        stack.append(elem)

    def pop(self, stack):
        return stack.pop()

    def expressionBool(self,exp):
        switcher = {
            '+' : True,
            '-' : True,
            '*' : True,
            '/' : True
        }
        return switcher.get(exp, False)

    def braces(self, A):
        stack = []
        openBrac = False
        for elem in A:
            if elem == ')':
                expression = False
                while(True):
                    poppedElem = self.pop(stack)
                    if(self.expressionBool(poppedElem) == True):
                        expression = True
                    if poppedElem == '(' and expression == True:
                        self.push(stack,'X')
                        break
                    if poppedElem == '(' and expression == False:
                        return 1
            else:
                if elem == '(':
                    openBrac = True
                self.push(stack,elem)
        if openBrac == False:
            return 0
        if stack[0] == 'X':
            return 0
        else:
            return 1
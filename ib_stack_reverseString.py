class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        stackForStr = []
        reverseStr = ""
        for elem in A:
            self.push(elem, stackForStr)
        for index in range(len(stackForStr)):
            poppedElem = self.pop(stackForStr)
            reverseStr += poppedElem
        return reverseStr
        
    def push(self,elem, stack):
        stack.append(elem)
    
    def pop(self,stack):
        return stack.pop()
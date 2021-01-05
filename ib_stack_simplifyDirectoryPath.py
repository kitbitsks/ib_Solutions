class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        stackForPath = []
        listOfPath = A.split("/")
        for elem in listOfPath:
            if elem is not '.':
                if elem == '..':
                    self.pop(stackForPath)
                else:
                    self.push(elem, stackForPath)
        absolutePath = ""
        for index in range(len(stackForPath)):
            poppedElem = stackForPath.pop()
            if poppedElem != "":
                absolutePath = "/" + poppedElem + absolutePath
        if absolutePath == "":
            return "/"
        return absolutePath
    
    def push(self, elem, stack):
        stack.append(elem)

    def pop(self, stack):
        if stack != []:
            stack.pop()
class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        if A == 1:
            return 1
        else:
            loopNumber = A-1
            result = 1
            for elem in range(loopNumber):
                result = self.increaseTheCount(result)
            return result
    
    def increaseTheCount(self,A):
        A = str(A) + " "
        stringToSendToFunc = ""
        resultingString = ""
        presentChar = A[0]
        for index in range(1,len(A)):
            nextChar = A[index]
            stringToSendToFunc += presentChar
            if presentChar != nextChar or nextChar==" ":
                resultingString += self.countOfContagiousNum(stringToSendToFunc) + presentChar
                stringToSendToFunc =""
                presentChar = nextChar
        return int(resultingString)
        
    def countOfContagiousNum(self,x):
        return str(len(x))    
        
        
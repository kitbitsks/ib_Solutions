class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        A = A.strip()
        A = " " + A
        count = 0 
        calculatedString = ""
        resultingString = ""
        for index in range(len(A)):
            if A[len(A)-1-index] == " ":
                resultFromFunc = self.reverseString(calculatedString)
                resultingString += resultFromFunc + " "
                calculatedString = ""
            else:
                calculatedString += A[len(A)-1-index]
        
        return resultingString.strip()

    def reverseString(self,stringToBeReversed):
        result = ""
        for index in range(len(stringToBeReversed)):
            result += stringToBeReversed[len(stringToBeReversed)-1-index]
        return result

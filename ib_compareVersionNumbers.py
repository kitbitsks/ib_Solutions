class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        tempB = B
        tempA = A
        A = A.split(".")
        B = B.split(".")
        if len(A) > len(B):
            tempB += ".0"* (len(A) - len(B))
        else:
            tempA += ".0"* (len(B) - len(A))
        A = tempA.split(".")
        B = tempB.split(".")
        for index in range(len(A)):
            if int(A[index]) > int(B[index]):
                return 1
            if int(A[index]) < int(B[index]):
                return -1
            if int(A[index]) == int(B[index]) and index == len(A)-1:
                return 0
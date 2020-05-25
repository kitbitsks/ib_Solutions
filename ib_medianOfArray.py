class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        C = sorted(A + B)
        # C.sort()
        if len(C) %2 ==0:
            result = C[(len(C)//2)-1] + C[(len(C)//2)]
            return float(result)/float(2)
        else:
            return C[len(C)/2]
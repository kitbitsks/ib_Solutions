class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        count = 0
        for elem in bin(A)[2:]:
            if elem =="1":
                count += 1
        return count

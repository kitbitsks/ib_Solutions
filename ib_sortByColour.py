class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        countOfOne = 0
        countOfTwo = 0
        countOfZero = 0
        for elem in A:
            if elem == 0:
                countOfZero += 1
            elif elem == 1:
                countOfOne += 1
            else:
                countOfTwo += 1
        A.clear()
        for i in range(countOfZero):
            A.append(0)
        
        for i in range(countOfOne):
            A.append(1)
            
        for i in range(countOfTwo):
            A.append(2)
            
        return A
        
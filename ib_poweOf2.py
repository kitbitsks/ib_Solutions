import math
class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        valueToBeChecked = int(A)
        if valueToBeChecked <=1:
            return 0
        resultAfterComputation = str(math.log(valueToBeChecked,2))
        for index in range(len(resultAfterComputation)):
            if resultAfterComputation[index] == ".":
                if resultAfterComputation[index + 1] == "0":
                    return 1
                else:
                    return 0
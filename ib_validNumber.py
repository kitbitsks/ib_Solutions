import re
class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, A):
        A = A.strip()
        if bool(re.match("^\-?[0-9]*\.[0-9]+$",A)) == True or bool(re.match("^\-?[0-9]+\.[0-9]+\e\-?[0-9]+$", A)) == True or bool(re.match("^\-?[0-9]+\e\-?[0-9]+$", A)) == True or bool(re.match("^\-?[0-9]+$", A)) == True: 
            return 1
        else:
            return 0
            
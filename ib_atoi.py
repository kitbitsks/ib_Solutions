class Solution:
    def asciiToNumber(self,number):
        switcher = {
            "0": 48,
            "1": 49,
            "2": 50,
            "3": 51,
            "4": 52,
            "5": 53,
            "6": 54,
            "7": 55,
            "8": 56,
            "9": 57,
            " ": 32,
            "+": 1,
            "-": -1
        }
        return switcher.get(number, 0)

    # @param A : string
    # @return an integer
    def atoi(self, A):
        stringToNumber = A
        res = 0
        index = 0
        while True:
            if self.asciiToNumber(stringToNumber[index]) != 32:
                mul = 1
                if self.asciiToNumber(stringToNumber[index]) == 0:
                    return 0
                if self.asciiToNumber(stringToNumber[index]) == -1:
                    mul = -1
                    index = index + 1
                if self.asciiToNumber(stringToNumber[index]) == 1:
                    mul =1
                    index = index + 1
                for newIndex in range(index, len(stringToNumber)):
                    if self.asciiToNumber(stringToNumber[newIndex]) == 32 or self.asciiToNumber(stringToNumber[newIndex]) == 0:
                        return res*mul
                    res = res * 10 + self.asciiToNumber(stringToNumber[newIndex]) - self.asciiToNumber("0")
                    if res >2147483647:
                        if res*mul < 0:
                            return -2147483647
                        else:
                            return 2147483647
                return mul*res
            else:
                index += 1
                
result =Solution()
print(result.atoi("-54332872018247709407 4 54"))
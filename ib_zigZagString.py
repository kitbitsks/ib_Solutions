class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        if B <=1:
            return A
        sentence = A
        n=B
        counterForSentence=0
        listToHoldValues = []
        for index in range(n):
            listToHoldValues.append("")
        countForRow = 0
        counterForRow = 1
        result = ""
        for counterForSentence in range(len(sentence)):
            if counterForRow == n:
                operator = "-"
                counterForRow = 1
            if countForRow == 0:
                operator = "+"
            if operator == "+":
                listToHoldValues[countForRow] = listToHoldValues[countForRow] + sentence[counterForSentence]
                countForRow+=1
            if operator == "-":
                listToHoldValues[countForRow] = listToHoldValues[countForRow] + sentence[counterForSentence]
                countForRow-=1
            counterForRow+=1
        # print(listToHoldValues)
        result = result.join(listToHoldValues[0:])
        return result


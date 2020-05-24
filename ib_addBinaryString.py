        firstBin = 0
        secondBin = 0
        if len(B) > len(A):
            stringToOperate = B
        else:
            stringToOperate = A
        for index in range(len(stringToOperate)):
            if index < len(A):
                firstBin+=2**index * int(A[len(A)-1-index])
            if index < len(B):
                secondBin+=2**index * int(B[len(B)-1-index])
        finalDecimalValue = firstBin + secondBin
        binaryValueOfGivenDecimal = ""
        decimalValueToBeConvertedToBinary = finalDecimalValue
        while True:
            if decimalValueToBeConvertedToBinary < 1:
                break
            binaryValueOfGivenDecimal += str(decimalValueToBeConvertedToBinary % 2)
            decimalValueToBeConvertedToBinary//=2
        convertedToBinary = binaryValueOfGivenDecimal[::-1]
        return convertedToBinary
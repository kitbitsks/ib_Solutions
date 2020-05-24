A = [ "abcd", "efgh", "adcdg" ]
A.sort(key = len)
# print(A)
longestPrefixFound = False
finalPrefix = ""
longestPrefix = ""
for characterInString in range(len(A[0])):
    extractedChar = A[0][characterInString]
    for index in range(1,len(A)):
        if extractedChar == A[index][characterInString]:
            longestPrefixFound = True
        else:
            longestPrefixFound = False
            longestPrefix = ""
            break
    if longestPrefixFound == True:
        longestPrefix+=extractedChar
        finalPrefix = longestPrefix
        # print(longestPrefix)
    
if not finalPrefix:
    print("sks")
else:
    print(finalPrefix)

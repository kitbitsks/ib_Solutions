countOfChar = 0
countOfSpace = 0
newLengthOfString = len(A)-1
if newLengthOfString == -1:
    return 0
while True:
    if newLengthOfString == -1:
        break
    elif A[newLengthOfString] != " ":
        break
    else:
        newLengthOfString-=1
        countOfSpace+=1
if countOfSpace == len(A):
    return 0
newLengthOfString = (len(A)- countOfSpace)
for i in range(newLengthOfString):
    if A[newLengthOfString-1-i] == " ":
        break
    else:
        countOfChar+=1
return countOfChar

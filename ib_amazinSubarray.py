A = "ABEC"
A = A.upper()
totalCount = 0
for index in range(len(A)):
    if A[index] == "A" or A[index] == "E" or A[index] == "I" or A[index] == "O" or A[index] == "U":
        totalCount+= len(A) - index

print(totalCount % 10003)
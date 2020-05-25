A= [ 0,23 ]
B= []
C = sorted(A + B)
print(C)
C.sort()
if len(C) %2 ==0:
    result = C[(len(C)//2)-1] + C[(len(C)//2)]
    print(result/2)
else:
    print(C[len(C)/2])
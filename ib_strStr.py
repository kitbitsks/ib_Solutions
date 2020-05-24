
mainStr = "aaaaaabbaaaaaabaabbbaaababbaabaabbbbbbaabaabbabbabaababbabababbababaabbbabaababb"
subStr = "baabb"
foundStr = -1
matchCount = 0
if mainStr == "" or subStr == "":
    print(foundStr)
for indexForMain in range(len(mainStr)):
    foundStr = indexForMain
    matchCount = 0
    for indexForSubStr in range(len(subStr)):
        if mainStr[indexForMain] != subStr[indexForSubStr]:
            foundStr = -1
            break
        if indexForMain != len(mainStr)-1:
            indexForMain+=1
            matchCount+=1
    if foundStr != -1 and matchCount == len(subStr):
        break
print(foundStr)

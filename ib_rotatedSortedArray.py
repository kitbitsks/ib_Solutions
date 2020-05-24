class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):

        inputArray = A
        firstArr = []
        secondArr = []
        for index in range(len(inputArray)-1):
            if inputArray[index+1] < inputArray[index]:
                firstArr.append(inputArray[index])
                secondArr = inputArray[index+1:]
                break
            else:
                firstArr.append(inputArray[index])

        firstResult = self.binarySearch(firstArr, B)
        secondResult = self.binarySearch(secondArr, B)
        if firstResult != -1:
            return firstResult
        elif secondResult != -1:
            return secondResult + (len(firstArr))
        else:
            return -1

    def binarySearch(self, arr, key):
        start = 0
        end = len(arr)-1
        while start<=end:
            mid = (start + end) // 2
            if key == arr[mid]:
                return mid
            elif key > arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return -1
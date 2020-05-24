class Solution:
    
    def binarySearch(self,arr, key):
        start = 0
        end = len(arr)
        while start <= end:
            mid = (start + end) //2
            if arr[mid] == key:
                return 1
            elif key > arr[mid]:
                start = mid+1
            else:
                end = mid -1
        return 0
                
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        combinedArr = []
        for arr in A:
            combinedArr.extend(arr)
        print(combinedArr)
        return self.binarySearch(Solution, combinedArr, B)
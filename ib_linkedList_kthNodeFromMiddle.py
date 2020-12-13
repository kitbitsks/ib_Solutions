# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        temp = A
        listLength = 0
        while temp is not None:
            listLength += 1
            temp = temp.next
        
        midPoint = listLength//2
        returningPoint = midPoint - B
        if returningPoint < 0:
            return -1
        countOfElem = 0
        temp = A
        while temp is not None:
            if returningPoint == countOfElem:
                return temp.val
            countOfElem += 1
            temp = temp.next
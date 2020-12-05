# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        listHavingZerosAndOnes = A
        n0 = n1 = 0
        while(listHavingZerosAndOnes is not None):
            if listHavingZerosAndOnes.val == 0:
                n0+=1
            else:
                n1+=1
            listHavingZerosAndOnes = listHavingZerosAndOnes.next
        listHavingZerosAndOnes = A
        for i in range(n0):
            listHavingZerosAndOnes.val = 0
            listHavingZerosAndOnes = listHavingZerosAndOnes.next
        
        for i in range(n1):
            listHavingZerosAndOnes.val = 1
            listHavingZerosAndOnes = listHavingZerosAndOnes.next
        return A      
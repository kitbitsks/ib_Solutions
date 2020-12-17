# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(self, A, B):
        count = 0
        temp = A
        noft = 1
        arrToOper = []
        newList = ListNode(None)
        finalList = newList
        while temp is not None:
            count += 1
            arrToOper.append(temp.val)
            if count == B:
                if noft % 2 != 0:
                    arrToOper = arrToOper[::-1]
                for elem in arrToOper:
                    newList.next = ListNode(elem)
                    newList = newList.next
                arrToOper = []
                count = 0
                noft += 1
            temp = temp.next
        newList.next = None
        return finalList.next

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        newList = ListNode(None)
        returningList = newList
        headNode = A
        sizeOfList = 0 
        temp = A
        while temp is not None:
            sizeOfList += 1
            temp = temp.next
        frontPointOfList = (sizeOfList - B) % (sizeOfList)
        temp = A
        countForFront = 0
        valForFront = -1
        while temp is not None:
            countForFront += 1
            if countForFront > frontPointOfList:
                newList.next = ListNode(temp.val)
                if countForFront-1 == frontPointOfList:
                    valForFront = temp.val
                newList = newList.next
            temp = temp.next
        if B % sizeOfList != 0:
            while headNode is not None:
                if headNode.val == valForFront:
                    break
                newList.next = ListNode(headNode.val)
                newList = newList.next
                headNode = headNode.next
        newList.next = None
        return returningList.next

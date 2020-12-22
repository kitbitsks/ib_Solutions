# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        if A.next is None:
            return A
        if (A.next).next is None:
            if A.val == (A.next).val:
                return 
            else:
                return A
        prevElem = A
        currentElem = (A.next)
        countOfElem = 1
        listToBeUpdated = ListNode(None)
        returningList = listToBeUpdated
        while currentElem is not None and prevElem is not None:
            if prevElem.val == currentElem.val:
                countOfElem += 1
            else:
                if countOfElem == 1:
                    listToBeUpdated.next = ListNode(prevElem.val)
                    listToBeUpdated = listToBeUpdated.next
                countOfElem = 1
            prevElem = currentElem
            currentElem = currentElem.next
            if currentElem is None:
                if countOfElem == 1:
                    listToBeUpdated.next = ListNode(prevElem.val)
                    listToBeUpdated = listToBeUpdated.next
                    break
        return returningList.next

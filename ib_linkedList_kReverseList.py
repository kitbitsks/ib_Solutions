# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        headPointer = ListNode(None)
        returnList = headPointer
        countForReverse = 0
        temp = A
        arrForReverse = []
        while temp is not None:
            countForReverse += 1
            arrForReverse.append(temp.val)
            if countForReverse == B:
                arrForReverse = arrForReverse[::-1]
                for elem in arrForReverse:
                    headPointer.next = ListNode(elem)
                    headPointer = headPointer.next
                countForReverse = 0
                arrForReverse = []
            temp = temp.next
        return returnList.next

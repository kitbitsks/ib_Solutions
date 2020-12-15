# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        temp = A
        smallerList = ListNode(None)
        biggerList = ListNode(None)
        newlyFormSmallList = smallerList
        newlyFormBiggerList = biggerList
        while temp is not None:
            if temp.val < B:
                smallerList.next = ListNode(temp.val)
                smallerList = smallerList.next
            else:
                biggerList.next = ListNode(temp.val)
                biggerList = biggerList.next
            temp = temp.next
        smallerList.next = newlyFormBiggerList.next
        newlyFormSmallList = newlyFormSmallList.next
        return newlyFormSmallList

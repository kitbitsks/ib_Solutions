# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        head = A
        current = A
        next = current.next
        while current:
            while next and next.val == current.val:
                next = next.next
            current.next = next
            current = current.next
        return head
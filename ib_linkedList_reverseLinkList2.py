# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        middleList = ListNode(None)
        firstList = ListNode(None)
        lastList = ListNode(None)
        headOfAllList = ListNode(None)
        headOfAllList.next = firstList
        headOfLastList = ListNode(None)
        headOfLastList.next = lastList
        count = 0
        temp = A
        while temp is not None:
            count += 1
            if count >= B and count <= C :
                new_node = ListNode(temp.val)
                new_node.next = middleList.next
                middleList.next = new_node
            if count < B:
                firstList.next = ListNode(temp.val)
                firstList = firstList.next
            if count > C:
                lastList.next = ListNode(temp.val)
                lastList = lastList.next
            temp = temp.next
        if count == 1:
            return ListNode(1)
        firstList.next = middleList.next
        while middleList.next is not None:
            middleList = middleList.next
        middleList.next = (headOfLastList.next).next
        headOfAllList = headOfAllList.next
        return headOfAllList.next
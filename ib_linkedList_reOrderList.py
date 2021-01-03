# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        temp = A
        reverseList = ListNode(None)
        freshList = ListNode(None)
        pointerToFresh = freshList
        displayingList = reverseList
        while temp is not None:
            new_node = ListNode(temp.val)
            new_node.next = reverseList.next
            reverseList.next = new_node
            freshList.next = ListNode(temp.val)
            freshList = freshList.next
            temp = temp.next
        temp = A
        displayingList = displayingList.next
        pointerToFresh = pointerToFresh.next
        roundOffList = ListNode(pointerToFresh.val)
        pointerToFresh = pointerToFresh.next
        returningList = ListNode(None)
        returningList.next = roundOffList
        temp = temp.next
        count  = 0
        while temp is not None:
            count += 1
            if count % 2 == 0:
                roundOffList.next = ListNode(pointerToFresh.val)
                pointerToFresh = pointerToFresh.next
                roundOffList = roundOffList.next
            else:
                roundOffList.next = ListNode(displayingList.val)
                displayingList = displayingList.next
                roundOffList = roundOffList.next
            temp = temp.next
        return returningList.next
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
    def __init__(self):
        self.head = None

    def add_element_LL(self,new_data):
        new_node = ListNode(new_data)
        if self.head is None:
            self.head = new_node
            return self.head
        last = self.head
        while(last.next is not None):
            last = last.next
        last.next = new_node
        return self.head
        
	def mergeTwoLists(self, A, B):
        mergedList = Solution()
        while (A is not None and B is not None):
            if A.val < B.val:
                finalList = mergedList.add_element_LL(A.val)
                A = A.next
            else:
                finalList = mergedList.add_element_LL(B.val)
                B = B.next
        
        while (A is not None):
            finalList = mergedList.add_element_LL(A.val)
            A = A.next
        while (B is not None):
            finalList = mergedList.add_element_LL(B.val)
            B = B.next
        return finalList

# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def listSize(self, listWhoseSizeToBeEvaluated):
        count = 0
        while listWhoseSizeToBeEvaluated is not None:
            count+=1
            listWhoseSizeToBeEvaluated = listWhoseSizeToBeEvaluated.next
        return count

    def removeNthFromEnd(self, A, B):
        sizeOfList = Solution.listSize(self,A)
        if ((sizeOfList-B)+1) <= 1:
            A = A.next
            return A 
        count = 1
        head = A
        prev = A
        while count != ((sizeOfList-B)+1):
            prev = A
            A = A.next
            count += 1
        prev.next = A.next
        return head


# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
        
    def solve(self, A):
        oddArr = []
        evenArr = []
        temp = A
        while temp is not None:
            if (temp.val %2) == 0:
                evenArr.append(temp.val)
            else:
                oddArr.append(temp.val)
            temp = temp.next
        evenArr = evenArr[::-1]
        i = 0
        j = 0
        k = 1
        totalLength = len(oddArr) + len(evenArr)
        head_node = A
        returnList = head_node
        while k <= totalLength:
            if k%2 == 0:
                head_node.val = (ListNode(evenArr[j])).val
                j+=1
            else:
                head_node.val = (ListNode(oddArr[i])).val
                i+=1
            head_node = head_node.next
            k+=1
        return returnList
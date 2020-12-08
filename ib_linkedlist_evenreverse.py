# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def __init__(self):
        self.head = None

    def addElement(self,valueToBeAdded):
        new_node = ListNode(valueToBeAdded)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        
    def solve(self, A):
        oddArr = []
        evenArr = []
        temp = self.head

        while temp is not None:
            if (temp.val %2) == 0:
                evenArr.append(temp.val)
            else:
                oddArr.append(temp.val)
            temp = temp.next
        evenArr = evenArr[::-1]
        i = j = 0
        k = 1
        totalLength = len(oddArr) + len(evenArr)
        # finalArr = []
        newListForReverse = Solution()
        returningList = newListForReverse
        while k <= totalLength:
            if k%2 == 0:
                newListForReverse.addElement(evenArr[j])
                # finalArr.append(evenArr[j])
                j+=1
            else:
                newListForReverse.addElement(oddArr[i])
                # finalArr.append(oddArr[j])
                i+=1
            # newListForReverse = newListForReverse.next
            k+=1
        
        return returningList
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addElement(self, elem, A):
        new_node = ListNode(elem)
        temp = A
        if temp is None:
            temp = new_node
            return
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    
    def addTwoNumbers(self, A, B):
        res1 = []
        res2 = []
        total = []
        temp1 = A
        temp2 = B
        
        if temp1 is None and temp2 is None:
            return 
        while(temp1 is not None):
            res1.append(temp1.val)
            temp1 = temp1.next

        while(temp2 is not None):
            res2.append(temp2.val)
            temp2 = temp2.next
        
        res1 = res1[::-1]
        res2 = res2[::-1]
            
        st1 = ""
        st2 = ""
        
        for i in range(len(res1)):
            st1 += str(res1[i])
        
        for i in range(len(res2)):
            st2 += str(res2[i])
        
        total = int(st1) + int(st2)
        total = str(total)
        total = total[::-1]
        
        finalList = ListNode(int(total[0]))
        returnList = finalList
        for index in range(1,len(total)):
            if finalList.next is None:
                finalList.next = ListNode(int(total[index]))
                finalList = finalList.next
        return returnList

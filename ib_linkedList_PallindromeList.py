# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return an integer
	def lPalin(self, A):
        arr = []
        temp = A
        while temp is not None:
            arr.append(str(temp.val))
            temp = temp.next
        arr = arr[::-1]
        temp = A
        for index in range(len(arr)):
            if arr[index] != str(temp.val):
                return 0
            temp = temp.next
        return 1
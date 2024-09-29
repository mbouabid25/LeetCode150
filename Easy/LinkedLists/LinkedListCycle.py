""" Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously 
following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false. """

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False

        point1 = head
        point2 = head.next

        while point1 != point2:
            if point2.next is None or point2.next.next is None:
                return False
            point1 = point1.next
            point2 = point2.next.next
        return True
    
"""     Explanation:
	1.	Pointer Initialization:
	•	point1 (slow pointer) starts at the head of the list.
	•	point2 (fast pointer) starts at head.next.
	2.	Cycle Detection Using Two Pointers:
	•	The slow pointer (point1) moves one step at a time.
	•	The fast pointer (point2) moves two steps at a time.
	•	If a cycle exists, the fast pointer will eventually meet the slow pointer.
	3.	While Loop:
	•	The loop continues as long as point1 and point2 do not meet.
	•	If point2 reaches the end (None), the function returns False, indicating no cycle.
	4.	Cycle Found:
	•	If point1 and point2 meet, it confirms a cycle exists, and the function returns True.

This method efficiently detects cycles in a linked list by using two pointers moving at different speeds. """

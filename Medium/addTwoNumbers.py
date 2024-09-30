""" You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1] """



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        tracker = dummy
        carry = 0

        while l1 or l2 or carry :
            if l1 :
                val1 = l1.val
            else:
                val1 = 0
            if l2 :
                val2 = l2.val
            else:
                val2 = 0

            total = val1 + val2 + carry
            carry = total//10
            tracker.next = ListNode(total%10)
            tracker = tracker.next

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next

        return dummy.next
    
""" Explanation:
ListNode class: This is the basic structure of a node in the linked list. It contains:

val: the value of the node (the digit).
next: the reference to the next node.
addTwoNumbers function:

We initialize a dummy node (dummy) and a current pointer to help us easily build the result list.
We also initialize a carry variable to store any overflow that happens when summing two digits.
Main logic:

We loop through the two linked lists (l1 and l2), adding corresponding digits along with the carry.
If the sum of the two digits and carry is 10 or more, we store the carry for the next iteration.
The node for the current digit (which is total % 10) is added to the result list.
If one of the linked lists runs out of nodes, we treat its value as 0.
Handling the carry: After processing all the nodes in both linked lists, we check if there is any carry left. 
If there is, we create a new node for the final carry. """

""" Time Complexity Analysis:

	•	You are traversing both linked lists l1 and l2 once.
	•	In each iteration of the while loop, you process one node from each list. This continues until both linked lists and the carry have been processed.
Let:
	•	n be the number of nodes in l1.
	•	m be the number of nodes in l2.
	•	The loop will run for max(n, m) iterations because you will stop once you’ve processed all nodes from both lists and handled any remaining carry.

Thus, the time complexity is O(max(n, m)) since you’re traversing both linked lists at most once.

Space Complexity Analysis:

	•	You are creating a new linked list to store the result. The length of this new list will be equal to max(n, m), plus one additional node if there’s a carry left after the final iteration.
	•	The auxiliary space used by the dummy node and tracker pointer is constant, but the space required for the result linked list depends on the number of nodes in the longer of the two input linked lists.

Therefore, the space complexity is also O(max(n, m)) because the output linked list will have at most max(n, m) + 1 nodes. """
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy_head = ListNode(0)  # Dummy head to simplify edge cases
        current = dummy_head
        carry = 0
        
        # Traverse both lists
        while l1 is not None or l2 is not None:
            # Get the values from the current nodes of l1 and l2 (0 if the node is None)
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            # Calculate the sum of the current digits plus the carry
            total = carry + x + y
            carry = total // 10  # Update the carry for next iteration
            current.next = ListNode(total % 10)  # Create the next node in the result
            
            # Move to the next node
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        # If there's any carry left, add a new node with that value
        if carry > 0:
            current.next = ListNode(carry)
        
        # Return the result linked list (skip the dummy head)
        return dummy_head.next
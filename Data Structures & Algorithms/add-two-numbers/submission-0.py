# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Continue looping if there are nodes left in l1 or l2, OR if a carry remains
        while l1 or l2 or carry:
            # Extract values; use 0 if a list has already reached its end
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the total sum for the current position
            total = val1 + val2 + carry
            
            # Determine the new carry and the digit to store in the node
            carry = total // 10
            digit = total % 10
            
            # Append the new digit to our result list
            current.next = ListNode(digit)
            current = current.next
            
            # Move to the next nodes in the input lists if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next
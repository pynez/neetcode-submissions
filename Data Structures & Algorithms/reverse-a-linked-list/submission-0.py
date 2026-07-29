# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ''' 
        twin we ALL know how to reverse a linked list
        1. maintain a prev, curr, and next variable
        2. as we iterate thru the linked list:
            a. set curr.next to prev
            b. set curr to next
            c. set prev to curr
            d. set next to next.next
        3. after iteration, prev will be the head of the list
        barbecue chicken 🍗
        '''
        prev = None
        curr = head

        while curr:
            nextn = curr.next
            curr.next = prev
            prev = curr
            curr = nextn

        return prev
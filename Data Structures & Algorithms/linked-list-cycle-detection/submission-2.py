# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
         We use a fast and slow pointer and iterate through the list
         if at any point the fast and slow pointer are at the same node,
         we know this is a circular array.
         '''

        fast = slow = head
        while fast and slow:
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                return false
            slow = slow.next
            if fast == slow:
                return True

        return False
        
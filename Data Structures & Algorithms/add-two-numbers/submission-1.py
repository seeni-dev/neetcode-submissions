# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.addTwoNumbersHelper(l1, l2, 0)
    
    def addTwoNumbersHelper(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        new_val = carry
        if l1 is not None:
            new_val += l1.val
        if l2 is not None:
            new_val += l2.val
        
        node = None
        carry = new_val // 10
        if new_val or l1 or l2:
            node = ListNode(new_val%10)
        if carry or (l1 and l1.next) or (l2 and l2.next):
            nl1 = None if not l1 else l1.next
            nl2 = None if not l2 else l2.next
            remaining = self.addTwoNumbersHelper(nl1, nl2, carry)
            node.next = remaining
        return node
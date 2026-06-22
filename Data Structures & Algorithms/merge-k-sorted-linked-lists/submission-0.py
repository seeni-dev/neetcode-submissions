# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = [
            (l.val, i, l, )
            for i, l in enumerate(lists)
            if l
        ]
        heapq.heapify(q)
        head = tail = None
        while q:
            val, i, l = heapq.heappop(q)
            if head is None:
                head = tail = l 
            else:
                tail.next = l
                tail = l
            if l.next:
                n = l.next
                heapq.heappush(q, (n.val, i, n, ))
            tail.next = None
        return head
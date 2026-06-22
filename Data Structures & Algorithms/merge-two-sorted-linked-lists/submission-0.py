# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = tail = None
        while list1 and list2:
            if list1.val < list2.val:
                if head is None:
                    head = tail = list1
                else:
                    tail.next = list1
                    tail = list1
                list1 = list1.next
            else:
                if head is None:
                    head = tail = list2
                else:
                    tail.next = list2
                    tail = list2
                list2 = list2.next
            tail.next = None
        while list1:
            if head is None:
                head = tail = list1
            else:
                tail.next = list1
                tail = list1
            list1 = list1.next
            tail.next = None
        while list2:
            if head is None:
                head = tail = list2
            else:
                tail.next = list2
                tail = list2
            list2 = list2.next
            tail.next = None
        return head
        

            
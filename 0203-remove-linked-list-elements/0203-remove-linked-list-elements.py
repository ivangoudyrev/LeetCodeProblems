# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # edge case when the list is empty
        if head == None:
            return head

        # if there are at least two elements in the list
        itr = head
        while itr and itr.next:
            if itr.next.val == val:
                itr.next = itr.next.next
            else:
                itr = itr.next

        # edge case when first(or all) list values match the val
        if head.val == val:
            head = head.next

        return head


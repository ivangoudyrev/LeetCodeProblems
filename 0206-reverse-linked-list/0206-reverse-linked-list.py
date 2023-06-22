# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        address_list = []
        itr = head
        while itr:
            address_list.append(itr.val)
            itr = itr.next
        address_list = address_list[::-1]
        
        new_head = ListNode(0)
        itr2 = new_head
        
        for i in address_list:
            itr2.next = ListNode(i)
            itr2 = itr2.next
        
        return new_head.next
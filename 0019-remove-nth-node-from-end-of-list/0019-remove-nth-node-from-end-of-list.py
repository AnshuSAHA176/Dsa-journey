# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        size=0
        temp=head
        while temp!=None:
            temp=temp.next
            size+=1
        if n == size:
            return head.next
            
        i=1
        iToFind=size-n
        prev=head
        while i<iToFind:
            prev=prev.next
            i+=1
        prev.next=prev.next.next
        return head

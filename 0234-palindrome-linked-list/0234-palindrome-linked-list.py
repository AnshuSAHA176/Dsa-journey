# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        def FindMid():
            slow=head
            fast=head
            while fast!=None and fast.next !=None:
                slow = slow.next
                fast=fast.next.next
            return slow
        if head==None or head.next==None:
            return True
        mid=FindMid()
        prev=None
        current=mid
        next=None
        while current != None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        
        left=head
        right=prev
        while right!=None:
            if left.val != right.val:
                return False
            left=left.next
            right=right.next
        return True
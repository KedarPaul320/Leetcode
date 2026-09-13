# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def isPalindrome(self, head):
    #     a = []

    #     while head:
    #         a.append(head.val)
    #         head = head.next

    #     return a == a[::-1]
    def reverse(self,head:ListNode):
        curr = head 
        prev = None 
        nxt = None 

        while curr!= None :
            nxt = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nxt 
        return prev
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(0)
        copy_curr = dummy
        curr = head
        while curr:
            copy_curr.next = ListNode(curr.val)
            copy_curr = copy_curr.next
            curr = curr.next
        rev = self.reverse(dummy.next)
        while rev:
            if head.val != rev.val:
                return False
            head = head.next 
            rev = rev.next 
        return True 

        

        
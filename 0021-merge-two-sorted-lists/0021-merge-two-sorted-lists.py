# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # Initialize trackers to safeguard parameter references
        iterator1 = list1
        iterator2 = list2
        
        # Use a dummy node to eliminate initial null pointer checks
        head = ListNode(0)
        curr = head 
        
        # Move forward while both linked lists have unvisited nodes
        while iterator1 and iterator2:
            if iterator1.val < iterator2.val :
                curr.next = iterator1
                iterator1 = iterator1.next  # Move list 1 pointer ahead
            else :
                curr.next = iterator2
                iterator2 = iterator2.next  # Move list 2 pointer ahead
            curr = curr.next 
            
        # Append the entire remaining segment of the non-empty list
        curr.next = iterator1 or iterator2
        
        # Discard the dummy head and return the actual merged head node
        return head.next 

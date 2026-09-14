class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:     
        p1 = headA
        p2 = headB 
        
        # Loop continues until they meet (either at a node or both at None)
        while p1 != p2:
            # If p1 reaches the end, switch to headB; otherwise, move forward
            p1 = p1.next if p1 else headB
            
            # If p2 reaches the end, switch to headA; otherwise, move forward
            p2 = p2.next if p2 else headA
            
        # Returns either the intersection node or None
        return p1
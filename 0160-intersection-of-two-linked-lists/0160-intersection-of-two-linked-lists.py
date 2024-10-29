# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        lenA, lenB = get_length(headA), get_length(headB)

        currA, currB = headA, headB

        if lenA > lenB:
            for _ in range(lenA - lenB):
                currA = currA.next
        elif lenB > lenA:
            for _ in range(lenB - lenA):
                currB = currB.next
                
        while currA and currB:
            if currA == currB:
                return currA

            currA = currA.next
            currB = currB.next
        return None
            
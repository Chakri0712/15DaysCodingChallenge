# Last updated: 8/6/2025, 2:40:20 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False

        # Brute Force (using set)

        # visited_nodes = set()
        # current = head
        # while current is not None:
        #     if current in visited_nodes:
        #         return True
        #     visited_nodes.add(current)
        #     current = current.next

        # return False

        # Floyd cycle detection (tortoise-hare algorithm)

        hare=tortoise=head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return True
        return False


        
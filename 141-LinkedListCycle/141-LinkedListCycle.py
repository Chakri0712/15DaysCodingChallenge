# Last updated: 8/6/2025, 12:10:14 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Brute Force (using set)
        if not head:
            return False
        visited_nodes = set()
        current = head
        while current is not None:
            if current in visited_nodes:
                return True
            visited_nodes.add(current)
            current = current.next

        return False
        
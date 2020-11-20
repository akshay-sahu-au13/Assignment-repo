# https://leetcode.com/problems/merge-k-sorted-lists/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        min_heap, pointer = [], {}

        for i, list_node in enumerate(lists):
            if list_node:  # filter those [] in lists
                pointer[i] = list_node
                heapq.heappush(min_heap, (list_node.val, i))

        # check null
        if not min_heap:
            return None

        header = cur = None
        while(min_heap):

            _, list_index = heapq.heappop(min_heap)
            node = pointer[list_index]

            # replenish heap if the list didn't end
            if node.next:
                pointer[list_index] = node.next
                heapq.heappush(min_heap, (node.next.val, list_index))

            if not header:  # intialize header, cur
                header = cur = node
            else:
                cur.next = node
                cur = cur.next
        return header

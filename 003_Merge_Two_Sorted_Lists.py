# Problem: Merge Two Sorted Lists
# URL: https://leetcode.com/problems/merge-two-sorted-lists
# Difficulty: Easy
# Topics: Linked List, Recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(N + M), where N and M are the lengths of list1 and list2.
        # Space: O(N + M) due to the recursion stack in the worst case.
        
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
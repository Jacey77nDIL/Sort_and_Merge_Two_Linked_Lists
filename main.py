# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val  # Value of the current node
#         self.next = next  # Pointer to the next node in the list

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to simplify the merging process.
        # This node serves as the starting point for the merged list.
        dummy = ListNode()
        # A pointer (current) is used to build the merged list starting from the dummy node.
        current = dummy

        # Loop through both lists as long as neither is fully traversed.
        while list1 and list2:
            # Compare the values of the current nodes of list1 and list2.
            if list1.val < list2.val:
                # If the value in list1 is smaller, append it to the merged list.
                current.next = list1
                # Move the list1 pointer to its next node.
                list1 = list1.next
            else:
                # Otherwise, append the value from list2 to the merged list.
                current.next = list2
                # Move the list2 pointer to its next node.
                list2 = list2.next

            # Move the current pointer to the newly appended node.
            current = current.next

        # At this point, at least one of the lists is fully traversed.
        # Append the remaining nodes of the non-empty list to the merged list.
        if list1:
            current.next = list1  # Append remaining nodes of list1.
        elif list2:
            current.next = list2  # Append remaining nodes of list2.

        # Return the merged list starting from the first real node (skip the dummy node).
        return dummy.next
#Code by me
#comments by GPT
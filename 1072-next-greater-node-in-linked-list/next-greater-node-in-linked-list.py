# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []
        # Convert linked list to array
        while head:
            values.append(head.val)
            head = head.next
        ans = [0] * len(values)
        stack = []

        for i in range(len(values)):
            while stack and values[i] > values[stack[-1]]:
                j = stack.pop()
                ans[j] = values[i]

            stack.append(i)

        return ans       
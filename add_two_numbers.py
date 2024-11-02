# Definition for singly-linked list.
from itertools import zip_longest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def addTwoNumbers(self, l1: list[int], l2: list[int]) -> list[int]:
#         result = []
#         carry = 0
#         for elem1, elem2 in zip_longest(l1, l2, fillvalue=0):
#             cur = elem1 + elem2
#             result.append(cur % 10 + carry)
#             carry = 1 if cur > 9 else 0

#         return result

# print(Solution().addTwoNumbers([2, 4, 3], [5, 6, 4]))

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        carry = 0
        dummy = ListNode()
        dummy.next = None
        dummy.val = 0

        elem1 = l1.val
        elem2 = l2.val

        while l1.next or l2.next:
            cur = l1.val or 0 + l2.val or 0
            result.append(cur % 10 + carry)
            carry = 1 if cur > 9 else 0

            l1 = l1.next or dummy
            l2 = l2.next or dummy
        
        return result



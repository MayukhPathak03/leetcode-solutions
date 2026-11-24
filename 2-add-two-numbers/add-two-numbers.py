# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        # This will probably be the most inefficient way to solve this
        # I will look at more efficient ways to solve this after I have done it myself once
        cur1, cur2 = l1, l2
        mul1, mul2 = 1, 1
        num1, num2 = 0, 0

        # This is taking from the linked list, and inverting the number. So the new values get multiplied by 10, 100 and so on.
        while cur1:
            num1 += (mul1 * cur1.val)
            mul1 *= 10
            cur1 = cur1.next

        while cur2:
            num2 += (mul2 * cur2.val)
            mul2 *= 10
            cur2 = cur2.next

        num = num1 + num2

        if num == 0:
            return ListNode(0)

        engine = ListNode()
        dummy = engine

        while num > 0:
            digit = num % 10
            dummy.next = ListNode(digit)
            dummy = dummy.next
            num //= 10

        return engine.next
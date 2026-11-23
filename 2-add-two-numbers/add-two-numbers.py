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
        num1, num2 = 0,0
        digit1, digit2 = 1,1
        while cur1:
            num1 += cur1.val * digit1
            digit1 *= 10
            cur1 = cur1.next
        while cur2:
            num2 += cur2.val * digit2
            digit2 *= 10
            cur2 = cur2.next
        num3 = num1 + num2

        if num3 == 0:
            return ListNode(0)
        dummy = ListNode(0)
        cur = dummy
        while num3 > 0:
            digit = num3 % 10
            cur.next = ListNode(digit)
            cur = cur.next
            num3 //= 10
        return dummy.next
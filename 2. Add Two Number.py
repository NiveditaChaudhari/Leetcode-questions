# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr=dummy
        carry=0

        while l1 or l2 or carry:
            sum=carry
            if l1:
                sum+=l1.val
                l1= l1.next
            if l2:
                sum+=l2.val
                l2= l2.next
            carry,val=divmod(sum,10)
            curr.next=ListNode(val)
            curr=curr.next
        return dummy.next
    
def print_LL(node:Optional[ListNode]):
    arr=[]
    while node:
        arr.append(node.val)
        node=node.next
    print(arr)


l1 = (ListNode(2, ListNode(4, ListNode(3))))
l2 = (ListNode(5, ListNode(6, ListNode(4))))

result = Solution().addTwoNumbers(l1, l2)
print("List is: ")
print_LL(result)
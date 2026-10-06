# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowP = head
        try: 
            fastP = head.next
        except:
            return False
        while True:
            if fastP == None:
                return False
            if fastP == slowP:
                return True
            slowP = slowP.next
            try: 
                fastP = fastP.next.next
            except:
                return False
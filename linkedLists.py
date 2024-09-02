
from collections import deque
from typing import List, Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Auxiliary:
    def arrayToLinkedList(elements: list):

        if len(elements)==0:
            return None
        
        head=ListNode(val=elements[0])
        prev=head
        for i in range(1,len(elements)):
            curr=ListNode(val=elements[i])
            prev.next=curr
            prev=curr
        return head
    
    def listToArray(head: Optional[ListNode]):
        res=[]
        while head:
            #print(head.val)
            res.append(head.val)
            head=head.next
        return res

        
class Solution:
    # 206. Reverse Linked List        https://leetcode.com/problems/reverse-linked-list/description/
    # Given the head of a singly linked list, reverse the list, and return the reversed list.
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currNode=head
        prevNode=None

        while currNode:
            aux=currNode.next
            currNode.next=prevNode
            prevNode=currNode
            currNode=aux
        return prevNode

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        def reverse(currNode):
            if not currNode:    
                return dummy
            restList=reverse(currNode.next)
            restList.next=currNode
            currNode.next=None
            return currNode
        reverse(head)
        return dummy.next

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        
        newHead=head
        if head.next:
            newHead=self.reverseListRecursive(head.next)
            head.next.next=head
        head.next=None

        return newHead
    

    # 21. Merge Two Sorted Lists      https://leetcode.com/problems/merge-two-sorted-lists/description/
    # Merge the two lists into one sorted list
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy

        while list1 and list2:
            if list1.val<=list2.val:
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            curr=curr.next

        if list1:
            curr.next=list1
        if list2:
            curr.next=list2

        return dummy.next
        

    # 143. Reorder List       https://leetcode.com/problems/reorder-list/description/
    # Input: head = [1,2,3,4,5]   Output: [1,5,2,4,3]
    def reorderList(self, head: Optional[ListNode]) -> None:

        def invert(currNode):
            if not currNode:
                return False
            newHead=currNode
            if currNode.next:
                newHead=invert(currNode.next)
                currNode.next.next=currNode
            currNode.next=None
            return newHead
        
        #get middle list
        # slow=head
        # fast=head.next
        # while fast and fast.next:
        #     slow=slow.next
        #     fast=fast.next.next

        slow,fast=head,head

        while fast:
            fast=fast.next.next if fast.next else None
            if fast:
                slow=slow.next
        list2=slow.next
        slow.next=None
        list2=invert(list2)
        list1=head
        
        while list1 and list2:
            aux1=list1.next
            list1.next=list2
            aux2=list2.next
            list2.next=aux1

            list1=aux1
            list2=aux2
        return head
        


#19. Remove Nth Node From End of List, tambuien se puede resolver en una sola pasada
# dandole ventaja de n al apuntador fast, y luego moviendo slow y fast de uno en uno
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        currNode=head

        while currNode:
            count+=1
            currNode=currNode.next

        if n>count:
            return head
        if n==count:
            return head.next
        
        index=1
        curr=head
        while index<count-n:
            index+=1
            curr=curr.next
        curr.next=curr.next.next
    # 138. Copy List with Random Pointer          https://leetcode.com/problems/copy-list-with-random-pointer/description/
    # Construct a deep copy of the list.
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr=head
        oldToNew={}
        oldToNew[None]=None

        while curr:
            newNode=Node(curr.val)
            oldToNew[curr]=newNode
            curr=curr.next

        curr=head
        while curr:
            newNode=oldToNew[curr]
            newNode.random=oldToNew[curr.random]
            newNode.next=oldToNew[curr.next]
            
            curr=curr.next
        return oldToNew[head]
    
    # 2. Add Two Numbers      https://leetcode.com/problems/add-two-numbers/description/
    # Add the two numbers and return the sum as a linked list.
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        prev=dummy
        carry=0
        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            summ=val1+val2+carry
            prev.next=ListNode(summ%10)
            carry=summ//10

            prev=prev.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None

        return dummy.next
    
    #141. Linked List Cycle         https://leetcode.com/problems/linked-list-cycle/description/
    # Return true if there is a cycle in the linked list.
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes=set()

        while head and head not in nodes:
            nodes.add(head)
            head=head.next

        return bool(head)       
        
    #287. Find the Duplicate Number     https://leetcode.com/problems/find-the-duplicate-number/description/
    # There is only one repeated number in nums, return this repeated number
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        slow2=0
        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow==slow2:
                return slow
 
if __name__ == '__main__':
    solution_instance = Solution()
    print(solution_instance.findDuplicate(nums =[1,3,4,2,2]))
    # list1=Auxiliary.arrayToLinkedList([2,4,3])
    # list2=Auxiliary.arrayToLinkedList([5,6,4])

    # res=solution_instance.addTwoNumbers(list1,list2)
    # print(*Auxiliary.listToArray(res))
    

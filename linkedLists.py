
from collections import deque
from typing import List, Optional

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
    def reverseListUsingStack(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=deque()
        if not head:
            return None
        
        curr=head
        stack.append(None)
        while curr.next:
            #print(curr.val)
            stack.append(curr)
            curr=curr.next

        newHead=curr
        prev=newHead
        print(prev.val)
        while stack:
            prev.next=stack.pop()
       
            prev=prev.next
         

        return newHead
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode=None
        currNode=head
    
        
        while currNode:
            
            nextNode=currNode.next
            currNode.next=prevNode
            
            prevNode=currNode
            currNode=nextNode

        return prevNode
    
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        
        newHead=head
        if head.next:
            newHead=self.reverseListRecursive(head.next)
            head.next.next=head
        head.next=None

        return newHead
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=None
        curr=ListNode()
        first=True

        while list1 and list2:
            if list1.val<=list2.val:
                curr.next=list1
                list1=list1.next

            else:
                curr.next=list2
                list2=list2.next
            curr=curr.next

            if first:
                head=curr
                first=False 

        #better solution 
        # if list1 or list2:
        #     cur.next = list1 if list1 else list2

        while list1:
            curr.next=list1
            curr=curr.next

            if first:
                head=curr
                first=False
            list1=list1.next

        while list2:
            curr.next=list2
            curr=curr.next
            if first:
                head=curr
                first=False
            list2=list2.next
        return head
    
    # cur = dummy = ListNode()
    # cur.next = list1....
    # return dummy.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head
        
        #get middle list
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        #reverse second half
        curr=slow.next
        slow.next=None
        prev=None

        while curr:
            foll=curr.next
            curr.next=prev
            prev=curr
            curr=foll
        
        list2=prev
        list1=head

        #join two lists
        while list1:
            list1Prev=list1
            list1=list1.next
            list1Prev.next=list2

            if  list2:
                list2Prev=list2
                list2=list2.next
                list2Prev.next=list1


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

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry=0
        dummy=ListNode()
        prev=dummy


        while l1 and l2:
            curr=ListNode()
            curr.val=(l1.val+l2.val+carry)%10
            carry=int((l1.val+l2.val+carry)/10)
            prev.next=curr
            prev=curr
            l1=l1.next
            l2=l2.next
            print(*Auxiliary.listToArray(dummy))

        while l1:
            curr=ListNode()
            curr.val=(l1.val+carry)%10
            carry=int((l1.val+carry)/10)
            prev.next=curr
            prev=curr
            l1=l1.next

        while l2:
            curr=ListNode()
            curr.val=(l2.val+carry)%10
            carry=int((l2.val+carry)/10)
            prev.next=curr
            prev=curr
            l2=l2.next
        if carry>0:
            curr=ListNode()
            curr.val=carry
            prev.next=curr


        if not dummy.next:
            return dummy
        
        return dummy.next
    
    #141. Linked List Cycle
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes=set()


        while head and head not in nodes:
            nodes.add(head)
            head=head.next
        if head:
            return True
        else:
            return False
        
    #287. Find the Duplicate Number
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return nums[0]
        
        walker=0
        runner=0
        

        while nums[walker]!=nums[runner] or walker==runner:
            walker=(walker+1)%len(nums)
            runner=(runner+2)%len(nums)
            
        return nums[walker]
 
if __name__ == '__main__':
    solution_instance = Solution()
    print(solution_instance.findDuplicate(nums =[1,3,4,2,2]))
    # list1=Auxiliary.arrayToLinkedList([2,4,3])
    # list2=Auxiliary.arrayToLinkedList([5,6,4])

    # res=solution_instance.addTwoNumbers(list1,list2)
    # print(*Auxiliary.listToArray(res))
    

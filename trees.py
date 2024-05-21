from typing import List, Optional
from collections import deque
import math
import ast

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isLeaf(self, node):
        return (not node.left) and (not node.right)   

class BST:
    def __init__(self,root: Optional[TreeNode]=None,nodes:List=[]):
        self.root=root
        if not root and len(nodes)>0:
            self.setValues(nodes)

        
    def getRoot(self):
        return self.root

    

    def insert(self,num:int):
        leaf=TreeNode(val=num)
        if not self.root:
            self.root=leaf
        else:
            #print('no raiz')
            node=self.root
            if num:
                while node:
                    parent=node
                    if num <= node.val:
                        node=node.left
                    else:
                        node=node.right
                
                if num <= parent.val:
                    print('insertando ',num ,'en izquierda de ',parent.val)
                    parent.left=TreeNode(val=num)
                else:
                    print('insertando ',num ,'en derecha de ',parent.val)
                    parent.right=TreeNode(val=num)

    def setValues(self,values:List):
        for x in values:
            #print('insertndo ',x)
            self.insert(x)

    def printTree(self):
        next=deque()
        next.append(self.root)

        while len(next)>0:
            node=next.popleft()
            print(node.val,end="-")
            if node.left:
                next.append(node.left)
            if node.right:
                next.append(node.right)

class BT:
    def __init__(self,root: Optional[TreeNode]=None,nodes:List=[]):
        print('creado')
        self.root=root
        if not root and len(nodes)>0:
            print('insertando nodos')
            self.insertAll(nums=nodes)

        
    def getRoot(self):
        return self.root
    
    def insertAll(self,nums):
        next=deque()
        if len(nums)>0 and nums[0]:
            self.root=TreeNode(nums[0])
            next.append(self.root)
        index=1

        while next and index<len(nums):
            node=next.popleft()
            
            if nums[index]!=None:
                node.left=TreeNode(nums[index])
                next.append(node.left)
                print('insertando ',nums[index] ,'en izquierda de ',node.val)
            index+=1
            if index<len(nums)and nums[index]!=None:
                node.right=TreeNode(nums[index])
                next.append(node.right)
                print('insertando ',nums[index] ,'en derecha de ',node.val)
            index+=1
    

    def printTree(self):
        next=deque()
        next.append(self.root)

        while len(next)>0:
            node=next.popleft()
            print(node.val,end="-")
            if node.left:
                next.append(node.left)
            if node.right:
                next.append(node.right)

        

        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
         
        next=deque()
        print(root.val)
        next.append(root)

        while next:
            node=next.popleft()
            print(node.val)
            aux=node.left
            node.left=node.right
            node.right=aux
            if node.left:
                next.append(node.left)
            if node.right:
                next.append(node.right)

        return root
    
    #104. Maximum Depth of Binary Tree
    def maxDepth(root: Optional[TreeNode]) -> int:
        def maxDepthAux(node:Optional[TreeNode],count):
            if node.left or node.right:
                if node.left:
                    countLeft=maxDepthAux(node.left,count+1)
                if node.right:
                    countRight=maxDepthAux(node.right,count+1)

                return max(countLeft,countRight)
            else: 
                return count
        if root:
            return maxDepthAux(root,1)
        else:
            return 0
    
    #543. Diameter of Binary Tree
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=[0]

        def dfs(node):

            if not node:
                return -1
            
            left=dfs(node.left)
            right=dfs(node.right)

            height=left+right+2
            res[0]=max(res[0],height)

            return 1+max(left,right)
        dfs(root)
        return res[0]

        #110. Balanced Binary Tree
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res=[True]

        def dfs(node):
            if not node:
                return -1
            
            left=dfs(node.left)
            right=dfs(node.right)

            if left-right>1 or right - left>1:
                res[0]=False

            return max(left,right)+1


        dfs(root)
        return res[0]
    
    #100. Same Tree
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        if not p or not q or p.val!=q.val:
            return False


        return ( self.isSameTree(p.left,q.left)   and self.isSameTree(p.right,q.right)   )
    

    #572. Subtree of Another Tree
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

            if not p and not q:
                return True
            if not p or not q or p.val!=q.val:
                return False


            return ( isSameTree(p.left,q.left)   and isSameTree(p.right,q.right)   )
        if not root:
            return False

        if isSameTree(root,subRoot):
            return True 
        
  
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot) 
    

    #235. Lowest Common Ancestor of a Binary Search Tree
    #Este es un caso general en el que no esta ordenado, si esta ordenado se puede eln O(logn) sin recursividad 

    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

    #     def findTwoNodes( root: 'TreeNode', p: 'TreeNode', q: 'TreeNode',nodesFound:int):
    #         if not root:
    #             return nodesFound
    #         if root.val==p.val:
    #             if nodesFound<1:
    #                 return findTwoNodes(root.left,p,q,nodesFound)+findTwoNodes(root.right,p,q,nodesFound)+nodesFound+1
    #             else:
    #                 return nodesFound+1
    #         if root.val ==q.val:
    #             if nodesFound<1:
    #                 return findTwoNodes(root.left,p,q,nodesFound)+findTwoNodes(root.right,p,q,nodesFound)+nodesFound+1
    #             else:
    #                 return nodesFound+1
    #         return findTwoNodes(root.left,p,q,nodesFound)+findTwoNodes(root.right,p,q,nodesFound)

    #     if findTwoNodes(root.left,p,q,0)<2 and findTwoNodes(root.right,p,q,0)<2:
    #         return root
    #     else:
    #         if findTwoNodes(root.left,p,q,0)==2 :
    #             return self.lowestCommonAncestor(root.left,p,q)
    #         if findTwoNodes(root.right,p,q,0)==2 :
    #             return self.lowestCommonAncestor(root.right,p,q)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr=root
        while True:
            if p.val < curr.val and q.val <curr.val:
                curr=curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr=curr.right
            else:
                break
        return curr
    
    #102. Binary Tree Level Order Traversal
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        #bfs but i need to separate each level
        #i could use aa counter or separators?
        res=[]
        que=deque()

        if root:  
            que.append(root)
            que.append(None)
            sublist=[]
        
        while que:
            
            curr=que.popleft()
            if curr:
                sublist.append(curr.val)
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
                next=que.popleft()
                if not next:
                    que.append(None)
                que.appendleft(next)
            elif len(que)>0:
                res.append(sublist)
                sublist=[]
                #que.append(None)
        return res
    
    #199. Binary Tree Right Side View
    #its easier with a for len(que)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        que=deque()

        if root:  
            que.append(root)
            print(root.val)
            que.append(None)
        
        while que:
            
            curr=que.popleft()
            if curr:
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
                next=que.popleft()
                if not next:
                    res.append(curr.val)
                    que.append(None)
                que.appendleft(next)
         
        return res
    
    #1448. Count Good Nodes in Binary Tree

    def goodNodes(self, root: TreeNode) -> int:
        count=[0]

        def countGoodNodes(root:TreeNode, maxNode):
            if not root:
                return count
            #print(root.val,' >= max ',maxNode)
            if root.val>=maxNode:
                count[0]+=1
                maxNode=root.val
           
       
            return countGoodNodes(root.left,maxNode)+countGoodNodes(root.right,maxNode)
        if not root:
            return 0
        
        countGoodNodes(root,root.val)
        return count[0]
    
    #98. Validate Binary Search Tree
    #boundaries
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, inferiorLimit, superiorLimit):
            if not root:
                return True
            if not inferiorLimit<root.val or not root.val<superiorLimit:
                return False
            else:
                return dfs(root.left, inferiorLimit, root.val) and dfs(root.right, root.val, superiorLimit)
        
            
        return dfs(root,-math.inf,math.inf)
      

    #230. Kth Smallest Element in a BST
    #dfs inorder traversal
    def kthSmallest(self, root: Optional[TreeNode],k: int) -> int:
        counter=[0]
        res=[]



        def dfsInorder(root):
            if root:

            # First recur on left child
                dfsInorder(root.left)
                counter[0]+=1
                if counter[0]==k:
                    res.append(root.val)
                    #print(' ---',root.val)

                # Then print the data of node
                #print(root.val, end=" "),

                # Now recur on right child
                dfsInorder(root.right)
        dfsInorder(root)

        return res[0]
    
    #105. Construct Binary Tree from Preorder and Inorder Traversal
    #first value o preorder is root
    #preorder tells me next root, inorder tells me how many nodes in left and right, divided by root
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0 or len(inorder)==0:
            return None
        
        root=TreeNode(preorder[0])
        mid=inorder.index(root.val)
        root.left=self.buildTree(preorder=preorder[1:mid+1], inorder=inorder[:mid])
        root.right=self.buildTree(preorder=preorder[mid+1:],inorder=inorder[mid+1:])
        return root
    
    #124. Binary Tree Maximum Path Sum
    #each Node left+right chain can be the max sum 
    #or, it can help the chain max(left, right)+its value
    # i dont add the child if its less than 0
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum=[-math.inf]

        def maxPathSumAux(root):
            if not root:
                return 0
            left=max(maxPathSumAux(root.left),0)
            right=max(maxPathSumAux(root.right),0)
            
            thisPath=left+right+root.val
            if thisPath>maxSum[0]:
                maxSum[0]=thisPath
            return max(left,right)+root.val
        
        maxPathSumAux(root)
        return maxSum[0]


# 297. Serialize and Deserialize Binary Tree
#bfs for both, its easier to deserialize 
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        que=deque()
        res=[]
        if root:
            que.append(root)
            res.append(str(root.val))
        while que:
            validLevel=False
            levelLength=len(que)
            appendedNones=0
            for _ in range(levelLength):
                node=que.popleft()
                left=node.left
                right=node.right
                if left:
                    res.append(str(left.val))
                    que.append(left)
                    validLevel=True
                else:
                    res.append("None")
                    appendedNones+=1

                if right:
                    res.append(str(right.val))
                    que.append(right)
                    validLevel=True
                else:
                    res.append("None")
                    appendedNones+=1
                #print(node.val,' ',validLevel)
                

            if not validLevel:
                res=res[:-appendedNones]
        result_string = '[' + ', '.join(res) + ']'

        return result_string

            
                


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodesString=deque(ast.literal_eval(data))
        nodes=deque()
        if nodesString:
            nextValue=nodesString.popleft()
            if nextValue:
                
                nextNode=TreeNode(nextValue)
                nodes.appendleft(nextNode)
                mainNode=nextNode
            
        while nodesString:
            root=nodes.popleft()
            nextValue=nodesString.popleft()

            if nextValue:

                nextNode=TreeNode(nextValue)
                root.left=nextNode
                nodes.append(nextNode)
                print('Insertando ', nextValue, ' a la izquierda de: ',root.val)
            
            if nodesString:
                nextValue=nodesString.popleft()
                if nextValue:
                    nextNode=TreeNode(nextValue)
                    root.right=nextNode
                    nodes.append(nextNode)
                    print('Insertando ', nextValue, ' a la derecha de: ',root.val)

        return mainNode
            
            
                
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))




    
if __name__ == '__main__':
    # mySolution=Solution()
    # inputTree=BT( [1,2,3,None,None,4,5])
    # inputTree.printTree()
    # root=inputTree.getRoot()
    # # print(root.val)
    # print(' ')
    # word="[1,2,3,None,None,4,5]"
    # arr=ast.literal_eval(word)
    # for x in arr:
    #     print(x)

    word="hola"
    print(word[1:])
    codec=Codec()
    root=codec.deserialize("[1,2,3,None,None,4,5]")
    tree=BT(root)
    tree.printTree()

    word=codec.serialize(tree.getRoot())
    print('res ',word)




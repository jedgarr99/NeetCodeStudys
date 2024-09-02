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
    #226. Invert Binary Tree        https://leetcode.com/problems/invert-binary-tree/description/
    #Given the root of a binary tree, invert the tree, and return its root.
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        que=deque()
        que.append(root)

        while que:
            node=que.popleft()
            node.left,node.right=node.right,node.left
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)

        return root
    
    #104. Maximum Depth of Binary Tree      https://leetcode.com/problems/maximum-depth-of-binary-tree/
    # Given the root of a binary tree, return its maximum depth.
    def maxDepth(root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            return 1+max(dfs(node.left), dfs(node.right))
        
        return dfs(root)
        
    
    #543. Diameter of Binary Tree           https://leetcode.com/problems/diameter-of-binary-tree/
    #The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
    #  This path may or may not pass through the root (number of edges)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            l=dfs(node.left)
            r=dfs(node.right)

            res[0]=max(res[0],l+r)
            return max(l,r)+1

        res=[0]
        dfs(root)
        return res[0]

        #110. Balanced Binary Tree
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (True,0)
            valueL,l=dfs(node.left)
            valueR,r=dfs(node.right)
            if not valueL or not valueR:
                return((False,0))
            if max(l,r)-min(l,r)>1:
                return((False,0))
            else: 
                return((True,max(l,r)+1))
        return dfs(root)[0]
        
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
        def isSameTree( p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return (isSameTree(p.left,q.left) and isSameTree(p.right,q.right))
        if not subRoot:
            return True
        if not root:
            return False
        return isSameTree(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
        
    

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
    
    #102. Binary Tree Level Order Traversal     https://leetcode.com/problems/binary-tree-level-order-traversal/
    # Given the root of a binary tree, return the level order traversal of its nodes' values.
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que=deque()
        que.append(root)
        res=[]
        while que:
            partialRes=[]
            for i in range(len(que)):
                node=que.popleft()
                partialRes.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(partialRes)
        return res

    
    #199. Binary Tree Right Side View       https://leetcode.com/problems/binary-tree-right-side-view/
    #Given the root of a binary tree, imagine yourself standing on the right side of it, return the 
    # values of the nodes you can see ordered from top to bottom.its easier with a for len(que)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        que=deque()
        que.append(root)
        res=[]

        while que:
            for i in range(len(que)):
                node=que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            res.append(node.val)
        return res
    
    #1448. Count Good Nodes in Binary Tree      https://leetcode.com/problems/count-good-nodes-in-binary-tree/
    # Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no 
    # nodes with a value greater than X.
    def goodNodes(self, root: TreeNode) -> int:
        self.count=0

        def dfs(node,maxValue):
            if not node:
                return
            
            if node.val>= maxValue:
                self.count+=1
            dfs(node.left,max(maxValue,node.val))
            dfs(node.right,max(maxValue,node.val))
            return
        
        dfs(root,root.val)
        return self.count
    
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
    #dfs inorder traversal, it can be done iteratively
    def kthSmallest(self, root: Optional[TreeNode],k: int) -> int:
        res=[]

        def dfs(node):
            if not node: 
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
            return
        
        dfs(root)
        return res[k-1]
    
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
        self.res=-math.inf

        def dfs(node):
            if not node:
                return 0
            l=max(dfs(node.left),0)
            r=max(dfs(node.right),0)
            self.res=max(self.res,  l+r+node.val  )

            return max(l,r)+node.val
            
        dfs(root)
        return self.res


# 297. Serialize and Deserialize Binary Tree
#bfs for both, its easier to deserialize 
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """


        que=deque([root])
        res=[]
        while que:
            node=que.popleft()
            
            if node:
                res.append(str(node.val))
                que.append(node.left)
                que.append(node.right)
            else:
                res.append('None')
        for x in res[::-1]:
            if x=='None':
                res.pop()
            else:
                break

        return '#'.join(res)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data=data.split('#') 
        queData=deque(data)
        queData.appendleft('None')

        dummy=TreeNode(0)
        queNodes=deque()
        queNodes.append(dummy)
             
        while queNodes and queData:
           
            node=queNodes.popleft()
            valueL=queData.popleft()
            valueR=queData.popleft() if queData else 'None'

            if valueL != 'None':
                valueL=int(valueL)
                node.left=TreeNode(valueL)
                queNodes.append(node.left)
            if valueR != 'None':
                valueR=int(valueR)
                node.right=TreeNode(valueR)
                queNodes.append(node.right)
                
        return dummy.right
             
        

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





from typing import List, Optional

class Solution:


    #78. Subsets
    #Given an integer array nums of unique elements, return all possible subsets
    #dfs, each num has the option to appear or not
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        def dfs(index):
            if index>=len(nums):
                res.append(subset.copy())
                return 
            subset.append(nums[index])
            dfs(index+1)
            subset.pop()
            dfs(index+1)
        dfs(0)
        return res
    
     #This works because using + creates a new object
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res=[]

    #     def dfs(index:int,subset:List[int]):
    #         if index>=len(nums):
    #             res.append(subset)
    #             return

    #         dfs(index+1,subset+[nums[index]])
    #         dfs(index+1,subset)

    #     dfs(0,[])
    #     return res
    
    #39. Combination Sum
    #Given an array of distinct integers candidates and a target integer target, return a
    #list of all unique combinations of candidates where the chosen numbers sum to target. 
    #You may return the combinations in any order.
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        subset=[]

        def dfs(index,summ):
       
            if summ>target or index>=len(candidates):
                return
            if summ==target:
                res.append(subset.copy())
                return 
            dfs(index+1,summ)

            subset.append(candidates[index])
            dfs(index,summ+candidates[index])
            subset.pop()
            
        dfs(0,0)
        return res
    
    #46. Permutations
    #Given an array nums of distinct integers, return all the possible permutations. 
    def permute(self, nums: List[int]) -> List[List[int]]:
        subset=[]
        res=[]
        availableNums=set(nums)

        def dfs():
            if len(subset)==len(nums):
                res.append(subset.copy())
                return
            for i in range(len(nums)):
                if nums[i] in availableNums:
                    subset.append(nums[i])
                    availableNums.remove(nums[i])
                    dfs()
                    subset.pop()
                    availableNums.add(nums[i])
        dfs()
        return res
        
    
    #90. Subsets II
    #Given an integer array nums that may contain duplicates, return all possible subsets
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        #nums.sort()

        def subsetsAux(index:int,subset:List[int]):
            if index>=len(nums):
                res.append(subset)
                return 
            subsetsAux(index+1,subset+[nums[index]])
            if nums[index] not in subset:
                subsetsAux(index+1,subset)

        subsetsAux(0,[])
        return res

        # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # res=[]
        # nums.sort()

        # def subsetsAux(index:int,subset:List[int]):
        #     if index>=len(nums):
        #         res.append(subset.copy())
        #         return 
        #     subset.append(nums[index])
        #     subsetsAux(index+1,subset)
        #     subset.pop()
        #     while index+1<len(nums) and nums[index]== nums[index+1]:
        #         index+=1

        #     #if nums[index] not in subset:
        #     subsetsAux(index+1,subset)

        # subsetsAux(0,[])
        # return res
    
    #40. Combination Sum II
    #find all unique combinations in candidates where the candidate numbers sum to target
    #el problema de copiar el metodo de arriba es que ahi siempre acumulo, aqui puedo regresar una solucion antes, 
    #y despues encontrar la misma solucion 
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()

        def subsetsAux(index:int,subset:List[int],partialSum):
            if partialSum<=0:
                if partialSum==0:
                    res.append(subset.copy())
                return
            
            prev=-1
            for i in range(index,len(candidates)):
                
                
                if candidates[i]==prev:
                    continue
                

                subsetsAux(i+1,subset+[candidates[i]],partialSum-candidates[i])
                prev=candidates[i]

        subsetsAux(0,[],target)
        return res
    
    #79. Word Search
    #Given an m x n grid of characters board and a string word, return true if word exists in the grid.
    def exist(self, board: List[List[str]], word: str) -> bool:
        res=[False]
        
        

        def existAux(node:matrixNode,word:str,visited):
            if node and len(word)==1 and node.value==word[0]:
                print('caso A')
                res[0]=True
                return 
            if len(word)<=0:
                print('caso B')
                return 
            if not node or node.value!= word[0]:
                print('caso C')
                return
            nextNode=True
            while nextNode  and not res[0]:
                print('caso D')
                print(node.value,' ',word[1:])
                nextNode=node.nextNode()
                if nextNode in visited:
                    print('Ya lo visite')
                    return
                visited.add(nextNode)
                existAux(nextNode,word[1:],visited)
               
            return res[0]
                
        for m in range(len(board)):
            for n in range (len(board[0])):
                if res[0]:
                    break
                visited=set()
                
                
                firstNode=matrixNode(board,m,n)
                print('--------Iniciando busquedaa desde ',firstNode.value,m,' ',n)
                existAux(firstNode,word,visited)
                
        
        return res[0]
    
    #79. Word Search
    #Given an m x n grid of characters board and a string word, return true if word exists in the grid.
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS=len(board)
        if ROWS:
            COLS=len(board[0])
        visited=set()

        def dfs(m,n,index):
            if index >=len(word):
                return True
            if m<0 or m>=ROWS or n<0 or n>=COLS or word[index]!=board[m][n]or (m,n) in visited:
                return False
            
            visited.add((m,n))
            res= dfs(m+1,n,index+1) or dfs(m-1,n,index+1) or dfs(m,n+1,index+1) or dfs(m,n-1,index+1) 
            visited.remove((m,n))

            return res
        
        for m in range(ROWS):
            for n in range(COLS):
                res=dfs(m,n,0)
                if res:
                    return True
        return False

    #131. Palindrome Partitioning
    #Given a string s, partition s such that every  substring of the partition is a 
    #palindrome. Return all possible palindrome partitioning of s.
    #it could be more efficient by not making copys of word, just using indexex dfs(i),where i start
    #for j in range(i,len(s))
    #is palindrome is easier with one pointer at start, another at the end, while end>start
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(word):
            l,r=0,len(word)-1
            while l<=r:
                if word[l]!= word[r]:
                    return False
                l+=1
                r-=1
            return True
    
        res=[]
        subset=[]
        def dfs(i,j):
            if i==len(s): 
                res.append(subset.copy())
                return
            if j>len(s):
                return
            if isPalindrome(s[i:j]):
                subset.append(s[i:j])
                dfs(j,j+1)
                subset.pop()
            dfs(i,j+1)

        dfs(0,1)
        return res

    #17. Letter Combinations of a Phone Number
    #Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
    def letterCombinations(self, digits: str) -> List[str]:
        phoneMap = {
            1: "",
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
            0: ""
        }

        res=[]

        def dfs(index,subset):
            if index>=len(digits):
                res.append(subset)
                return
            num=int(digits[index])
            for x in phoneMap[num]:
                dfs(index+1,subset+x)
        dfs(0,"")
        return res
    
    # if len(digits)==0:
    #         return[]
    #     phoneMap = {
    #         "1": "",
    #         "2": "abc",
    #         "3": "def",
    #         "4": "ghi",
    #         "5": "jkl",
    #         "6": "mno",
    #         "7": "pqrs",
    #         "8": "tuv",
    #         "9": "wxyz",
    #         "0": ""
    #     }

    #     res=[]
    #     word=[]
    #     def dfs(i):
    #         if i==len(digits):
    #             res.append(''.join(word))
    #             return
    #         for letter in phoneMap[digits[i]]:
    #             word.append(letter)
    #             dfs(i+1)
    #             word.pop()
    #     dfs(0)
    #     return res


    #51. N-Queens
    #The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.' for i in range(n)] for j in range(n)]
        rows=set() #from 0 to n-1
        cols=set() #from 0 to n
        positiveD=set() #from 0 to 2n (r+c)
        negativeD=set()# from -n to n (r-c)

        def addQueen(r,c):
            if (r not in rows and c not in cols and
                r+c not in positiveD and r-c not in negativeD):
                board[r][c]='Q'
                rows.add(r)
                cols.add(c)
                positiveD.add(r+c)
                negativeD.add(r-c)
                return True
            return False

        def removeQueen(r,c):
            board[r][c]='.'
            rows.remove(r)
            cols.remove(c)
            positiveD.remove(r+c)
            negativeD.remove(r-c)
           
        res=[]
        
        def dfs(r,queens):
            if queens==n:
                res.append( [''.join(row) for row in board])
                return
            if r>=n:
                return
            
            for c in range(n):
                if addQueen(r,c):
                    dfs(r+1,queens+1)
                    removeQueen(r,c)
        dfs(0,0)
        return res


    
if __name__=='__main__':
    mySolution=Solution()
    print(mySolution.solveNQueens(4))



        
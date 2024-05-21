

from typing import List, Optional


class matrixNode():
    def __init__(self,board,i,j,path=""):
        self.board=board
        self.value=board[i][j]
        self.i=i
        self.j=j
        self.up=False
        self.right=False
        self.down=False
        self.left=False

        if path=='up':
            self.up=True
        elif path=='down':
            self.down=True
        elif path=='left':
            print('vengo desde la izquierda ')
            self.left=True
        elif path=='right':
            print('vengo desde la derecha ')
            self.right=True


            

        self.rows=len(board)
        if self.rows>0:
            self.columns=len(board[0])

    def nextNode(self):


        if not self.right and self.isValid(self.i,self.j+1):
            print('right')
            self.right=True
            print(matrixNode(self.board,self.i,self.j+1).value)
            return matrixNode(self.board,self.i,self.j+1,"left")
    
        elif not self.left and self.isValid(self.i,self.j-1):
            print('left')
            self.left=True
            print(matrixNode(self.board,self.i,self.j-1).value)
            return matrixNode(self.board,self.i,self.j-1,"right")
    
        elif not self.down and self.isValid(self.i+1,self.j):
            print('down')
            self.down=True
            print(matrixNode(self.board,self.i+1,self.j).value)
            return matrixNode(self.board,self.i+1,self.j,"up")
    
        if not self.up and self.isValid(self.i-1,self.j):
            print('up')
            self.up=True
            print(matrixNode(self.board,self.i-1,self.j).value)
            return matrixNode(self.board,self.i-1,self.j,"down")
        
        else:
            print('no')
            return None

    def isValid(self,i,j):
        if i>=0 and i <self.rows and j>=0 and j<self.columns:
            return True
        else:
            return False
        
    def __eq__(self, other):
        return self.i == other.i and self.j == other.j

    def __hash__(self):
        return hash((self.i, self.j))



class Solution:


    #78. Subsets
    #Given an integer array nums of unique elements, return all possible subsets
    #dfs, each num has the option to appear or not
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def dfs(index:int,subset:List[int]):
            if index>=len(nums):
                res.append(subset)
                return

            dfs(index+1,subset+[nums[index]])
            dfs(index+1,subset)

        dfs(0,[])
        return res
    
    #39. Combination Sum
    #Given an array of distinct integers candidates and a target integer target, return a
    #list of all unique combinations of candidates where the chosen numbers sum to target. 
    #You may return the combinations in any order.
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]

        def combinationSumAux(newTarget:int,subset:List[int],index:int):
            if newTarget==0:
                res.append(subset)
                return
            if newTarget<0 or index>=len(candidates):
                return
            
            
            combinationSumAux(newTarget-candidates[index],subset+[candidates[index]],index)
            combinationSumAux(newTarget,subset,index+1)
        
        combinationSumAux(target,[],0)
        return res
    
    #46. Permutations
    #Given an array nums of distinct integers, return all the possible permutations. 
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def permutesAux(remainingNums:List[int],subset:List[nums]):
            if len(remainingNums)==0:
                res.append(subset)
                return
            
            for i in range(len(remainingNums)):
                print(i,' ',*remainingNums)
                remainingNumsInput=remainingNums.copy()
                num=remainingNumsInput[i]
                remainingNumsInput[i]=remainingNumsInput[-1]
                remainingNumsInput.pop()
                permutesAux(remainingNumsInput,subset+[num])

        permutesAux(nums,[])
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
        def isPalindrome(word:str):
            for i in range(int(len(word)/2)):
                j=len(word)-i-1
                if word[i]!=word[j]:
                    return False
            return True

        res=[]
        def dfs(subRes,word):
            if len(word)==0:
                print('finished ',*subRes)
                res.append(subRes.copy())
                return
            
            somePalidrome=False
            print('Analizando ',word)
            for i in range(1,len(word)+1):
                print('isPalindrome?',word[:i] )
                if isPalindrome(word[:i]):
                    somePalidrome=True
                    subRes.append(word[:i])
                    print('Agregado ',*subRes)
                    print('sobra ',word[i:])
                    dfs(subRes,word[i:])
                    subRes.pop()

            if not somePalidrome:
                print('palabra sin mas palindromos')
                return
        dfs([],s)
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


    #51. N-Queens
    #The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['o' for _ in range(n)] for _ in range(n)]
        res=[]

        def nextAvailablePosition(board):
            for i in range(n):
                for j in range(n):
                    if board[i][j]=='o':
                        return (i,j)
            return(-1,-1)
        def markInvalid(i,j,board):
            for m in range(n):
                if board[m][j]=='o':
                    board[m][j]='.'

            for m in range(n):
                if board[i][m]=='o':
                    board[i][m]='.'
            
            r=i
            c=j
            while r>-1 and c>-1:
                if board[r][c]=='o':
                    board[r][c]='.'
                r-=1
                c-=1
            r=i
            c=j
            while r<n and c<n:
                if board[r][c]=='o':
                    board[r][c]='.'
                r+=1
                c+=1
            r=i
            c=j
            while r>-1 and c<n:
                if board[r][c]=='o':
                    board[r][c]='.'
                r-=1
                c+=1
            r=i
            c=j  
            while r<n and c>-1:
                if board[r][c]=='o':
                    board[r][c]='.'
                r+=1
                c-=1

        def isValid(i,j,board):
            if board[i][j]!='o':
                return False
            else:
                return True

            

        def dfs(queenCount,board,r):
            if queenCount>=n:
                print('----------------')
                subRes=[]
                for row in board:
                    subRes.append(''.join(row))
                res.append(subRes)
                return
            # if i<0 or i>=n or j<0 or j>=n or board[i][j] != 'o':
            #     return

            isSomeValid=False
            #print('entrando en for')
           
            for c in range(n):
                
                thisBoard=[row[:] for row in board]
                if isValid(r,c,thisBoard):
                    #print('Agregando ',r,' ',c)
                    isSomeValid=True
                    thisBoard[r][c]='Q'
                    markInvalid(r,c,thisBoard)
                    # print('***************')
                    # for row in thisBoard:
                    #     print(' '.join(row))
                    # print('***************')

                    dfs(queenCount+1,thisBoard,r+1)

            if not isSomeValid:
                #print('No se pueden poner mas reinas')
                return 
            
        dfs(0,board.copy(),0)
        return res


    
if __name__=='__main__':
    mySolution=Solution()
    print(mySolution.solveNQueens(4))



        
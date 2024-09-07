from collections import defaultdict
from typing import List

class Solution:
    
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":return "0"
        num1,num2=num1[::-1],num2[::-1]
        res=[0]*(len(num1)+len(num2))

        for j in range(len(num2)):
            for i in range(len(num1)):
                curr=i+j
                nextPos=i+j+1
                res[curr]+=(int(num1[i]) * int(num2[j]))
                res[nextPos]+=res[curr]//10
                res[curr]%=10
        zeros=True
        resString=""
        for digit in res[::-1]:
            if  digit:
                zeros=False
            if not zeros:
                resString+=str(digit)
        return resString

    def rotate(self, matrix: List[List[int]]) -> None:
        N=len(matrix)
        def transpose():
            for i in range(N):
                for j in range(i+1,N):
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        def reflect():
            for r in range(N):
                for c in range(N//2):
                    matrix[r][c],matrix[r][N-c-1]=matrix[r][N-c-1],matrix[r][c]
        transpose()
        reflect()

    # Spiral Matrix       https://leetcode.com/problems/spiral-matrix/description/
    # Given an m x n matrix, return all elements of the matrix in spiral order.
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS,COLS=len(matrix),len(matrix[0])
        l,b,t,r=0,ROWS-1,0,COLS-1
        res=[]
        while l<=r and b>=t:
            for i in range(l,r+1):
                res.append(matrix[t][i])
            t+=1
            for i in range(t,b+1):
                res.append(matrix[i][r])
            r-=1
            if l>r or b<t:
                break
            for i in range(r,l-1,-1):
                res.append(matrix[b][i])
            b-=1
            for i in range(b,t-1,-1):
                res.append(matrix[i][l])
            l+=1
        return res

        
    # 73. Set Matrix Zeroes       https://leetcode.com/problems/set-matrix-zeroes/description/
    # Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
    def setZeroes(self, matrix: List[List[int]]) -> None:
        firstRow=False
        ROWS,COLS=len(matrix),len(matrix[0])
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c]==0:
                    if r==0 :
                        firstRow=True
                    else:
                        matrix[r][0]=0
                    matrix[0][c]=0
        def setRow(r):
            for c in range(COLS):
                matrix[r][c]=0
        def setCol(c):
            for r in range(ROWS):
                matrix[r][c]=0
        for c in range(1,COLS):
            if matrix[0][c]==0:
                setCol(c)
        for r in range(1,ROWS):
            if matrix[r][0]==0:
                setRow(r)
        if matrix[0][0]==0:
            setCol(0)
        if firstRow:
            setRow(0)
        
    # 202. Happy Number   https://leetcode.com/problems/happy-number/
    # Return true if n is a happy number, and false if not.
    def isHappy(self, n: int) -> bool:
        visited=set()
    
        while n not in visited:
            visited.add(n)
            nextN=0
            while n:
                digit=n%10
                n //=10
                nextN+=digit*digit
            n=nextN
        return True if n==1 else False
    
    # 66. Plus One    https://leetcode.com/problems/plus-one/description/
    # Increment the large integer by one and return the resulting array of digits.
    def plusOne(self, digits: List[int]) -> List[int]:
        i=len(digits)-1
        carry=1
        while carry and i>=0:
            digits[i]+=1
            carry=1 if digits[i]>=10 else 0
            digits[i]%=10
            i-=1
        if carry:
            digits.insert(0,1)
        return digits

        
    # Pow(x, n)   https://leetcode.com/problems/powx-n/
    # Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        if not x:
            return 0
            
        dp=defaultdict(int)
        dp[1]=x
        def pow(n):
            if dp[n]!=0:
                return dp[n]
            if n%2==0:
                dp[n]=pow(n//2)*pow(n//2)
            else:
                dp[n]=pow(n//2)*pow(n//2)*dp[1]
            return dp[n]
        res=pow(abs(n))
        return res if n>0 else 1/res
    
    def myPowFaster(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = helper(x, n // 2)
            res=res*res
            return x * res if n % 2 else res

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res


        
        
class DetectSquares:

    def __init__(self):
        self.countPoints=defaultdict(int)
        self.points=[]
        

    def add(self, point: List[int]) -> None:
        self.countPoints[tuple(point)]+=1
        self.points.append(point)
        
    def count(self, point: List[int]) -> int:
        x1,y1=point
        res=0
        for x2,y2 in self.points:
            if abs(x1-x2) ==abs(y1-y2) and x1!=x2:
                res+=self.countPoints[x1,y2]*self.countPoints[x2,y1]
        return res

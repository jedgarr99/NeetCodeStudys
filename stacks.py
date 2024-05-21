from collections import deque
from typing import List

# 155. Min Stack    https://leetcode.com/problems/min-stack/description/  
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
class MinStack:

    def __init__(self):
        return
        

    def push(self, val: int) -> None:
        return
        

    def pop(self) -> None:
        return
        

    def top(self) -> int:
        return
        

    def getMin(self) -> int:
        return
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


class Solution():

    # 20. Valid Parentheses       https://leetcode.com/problems/valid-parentheses/description/
    # Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    def isValid(self, s: str) -> bool:
        return
    
    # 150. Evaluate Reverse Polish Notation       https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
    # Evaluate the expression
    def evalRPN(self, tokens: list[str]) -> int:
        stack=deque()
        operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: int(x / y)
         }   

        for n in tokens:
            isDigit=False
            try:
                int(n)
                isDigit=True
            except:
                pass
            if isDigit:
                stack.append(int(n))
            else:
                a=stack.pop()
                b=stack.pop()
                operation = operations[n]
                result = operation(b, a)
                stack.append(result)
        return stack.pop()
    

    # 22. Generate Parentheses        https://leetcode.com/problems/generate-parentheses/description/
    # Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    def generateParenthesis(self, n: int) -> list[str]:
        def generateAux(l:int,r:int,par:str):


            if len(par)==2*n:
                res.append(par)
                return

            if l<n:
                newPar=par+'('
                generateAux(l+1,r,newPar)
            if r<l:
                newPar=par+')'
                generateAux(l,r+1,newPar)
        res=[]
        generateAux(0,0,'')
        return res
    

    # 739. Daily Temperatures     https://leetcode.com/problems/daily-temperatures/description/
    # Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] 
    # is the number of days you have to wait after the ith day to get a warmer temperature. 
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return

    # 853. Car Fleet      https://leetcode.com/problems/car-fleet/description/
    # Return the number of car fleets that will arrive at the destination.
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        eta=[0]*len(speed)
        
        for i in range(len(speed)):
            eta[i]=(target-position[i])/speed[i]
          
        position, eta = (list(t) for t in zip(*sorted(zip(position, eta))))
        
        fleets=1
        time=eta[len(speed)-1]
        for i in range(len(speed)-2,-1,-1):
            if eta[i]>time:
                time=eta[i]
                fleets+=1
        return fleets
    #limpiar y corregir este codigo , 84. Largest Rectangle in Histogram
    

    # 84. Largest Rectangle in Histogram      https://leetcode.com/problems/largest-rectangle-in-histogram/description/ 
    # Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the 
    # area of the largest rectangle in the histogram.
    def largestRectangleArea(self, heights: list[int]) -> int:
        minimumLeft=[-1]*len(heights)
        stack=deque()

        for i in range(len(heights)):
            #looking for the next smaller
            while stack and heights[stack[0]]>heights[i]:
                minimumLeft[stack[0]]=i+1
                stack.popleft()
            stack.appendleft(i)
        print(*minimumLeft)

        minimumRight=[-1]*len(heights)
        stack=deque()

        for i in range(len(heights)-1,-1,-1):
            #looking for the next smaller
            while stack and heights[stack[0]]>heights[i]:
                minimumRight[stack[0]]=i+1
                stack.popleft()
            stack.appendleft(i)
        print(*minimumRight)

        maxA=0
        for i in range(len(heights)):

            r=minimumLeft[i] if minimumLeft[i]!=-1 else len(heights)+1
            l=minimumRight[i] if minimumRight[i]!=-1 else 0
            wide=r-l-1
            area=wide*heights[i]
            if area>maxA:
                maxA=area


        return maxA
    
        

         

    
    
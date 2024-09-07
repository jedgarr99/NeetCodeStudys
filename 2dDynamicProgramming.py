
from typing import List
import math


class Solution:

    # 62. Unique Paths        https://leetcode.com/problems/unique-paths/description/
    # The robot can only move either down or right at any point in time.
    # return the number of possible unique paths that the robot can take to reach the 
    # bottom-right corner.
    def uniquePaths(self, m: int, n: int) -> int:
        board=[[1 for c in range(n)] for r in range(m)]

        for r in range(m-2,-1,-1):
            for c in range(n-2,-1,-1):
                board[r][c]=board[r+1][c]+board[r][c+1]
                
        return board[0][0]

    # 1143. Longest Common Subsequence        https://leetcode.com/problems/longest-common-subsequence/
    # Given two strings text1 and text2, return the length of their longest common subsequence. If there 
    # is no common subsequence, return 0.
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0 for col in range(len(text2)+1)] for row in range(len(text1)+1)]
        for r in range(len(text1)-1,-1,-1):
            for c in range(len(text2)-1,-1,-1):
                if text1[r]==text2[c]:
                    dp[r][c]=1+dp[r+1][c+1]
                else:
                    dp[r][c]=max(dp[r+1][c],dp[r][c+1])
                    
        return dp[0][0]

    def longestCommonSubsequenceTopDown(self, text1: str, text2: str) -> int:
        # Memoization table
        memo = [[-1] * len(text2) for _ in range(len(text1))]

        def lcs(i: int, j: int) -> int:
            # Base case: If either string is exhausted
            if i == len(text1) or j == len(text2):
                return 0
            
            # Return the result if it is already computed
            if memo[i][j] != -1:
                return memo[i][j]
            
            # If characters match
            if text1[i] == text2[j]:
                memo[i][j] = 1 + lcs(i + 1, j + 1)
            else:
                # If characters do not match
                memo[i][j] = max(lcs(i + 1, j), lcs(i, j + 1))
            
            return memo[i][j]

        return lcs(0, 0)
        
    # Best Time to Buy And Sell Stock With Cooldown	https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
    # Find the maximum profit you can achieve. After you sell your stock, you cannot buy stock on the next day 
    def maxProfit(self, prices: List[int]) -> int:
        dp={} #(canBuy,i):currProfit

        def  dfs(canBuy,i):
            if i>=len(prices):
                return 0

            if (canBuy,i) in dp:
                return dp[(canBuy,i)]

            cooldown=dfs(canBuy,i+1)

            if canBuy:
                toBuy=dfs(False,i+1)-prices[i]
                profit=max(toBuy,cooldown)
                dp[(canBuy,i)]=profit
                return profit
            else:
                toSell=dfs(True,i+2)+prices[i]
                profit=max(toSell,cooldown)
                dp[(canBuy,i)]=profit
                return profit

        return dfs(True,0)
        



    # 518. Coin Change II         https://leetcode.com/problems/coin-change-ii/description/
    # Return the number of combinations that make up that amount.     
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)
        dp[0]=1

        for c in coins:
            for i in range(len(dp)):
                if i+c<=amount:
                    dp[i+c]+=dp[i]
            #print(dp)
        return dp[amount]
    

    def changeTopDown(self, amount: int, coins: List[int]) -> int:
    
        dp={}

        def dfs(i, total):
            if total> amount or i>=len(coins):
                return 0
            if total==amount:  
                return 1
            if (i,total) in dp:
                return dp[(i,total)]
            

            include=dfs(i,total+coins[i])
            dontInclude=dfs(i+1,total)
            dp[(i, total)]=include+dontInclude

            
            return dp[(i, total)]
        return dfs(0,0)
    
    # Target Sum	https://leetcode.com/problems/target-sum/description/
    # build an expression out of nums by adding one of the symbols '+' 
    # and '-' before each integer in nums
    # Return the number of different expressions that you can build,
    # which evaluates to target.
    def findTargetSumWaysTopDown(self, nums: List[int], target: int) -> int:
        dp={}
        def dfs(i,total):
            if total==target and i==len(nums):
                return 1
            if i>=len(nums):
                return 0
            if (i,total) in dp:
                return dp[(i,total)]

            add=dfs(i+1,total+nums[i])
            substract=dfs(i+1,total-nums[i])
            dp[(i,total)]=add+substract
            return dp[(i,total)]
        return dfs(0,0)
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
    
        # Check if (S + target) is valid and an integer
        if (total_sum + target) % 2 != 0 or total_sum < abs(target):
            return 0
        
        # Calculate the subset sum P
        subset_sum = (total_sum + target) // 2
        
        # Initialize dp array where dp[i] is the number of ways to form sum i
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # There's one way to form sum 0 (by picking no elements)
        
        # Bottom-up calculation
        for num in nums:
            for i in range(subset_sum, num - 1, -1):
                dp[i] += dp[i - num]
        
        return dp[subset_sum]
    
    # Interleaving String	https://leetcode.com/problems/interleaving-string/
    # find whether s3 is formed by an interleaving of s1 and s2.
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp={}
        def dfs(i,j):
            if i==len(s1) and j==len(s2) and i+j ==len(s3):
                return True
            if i+j>=len(s3):
                return False
            if (i,j) in dp:
                return dp[(i,j)]
            #I can use both
            if i<len(s1) and j<len(s2) and s1[i]==s3[i+j] and s2[j]==s3[i+j]:
                dp[(i,j)]=dfs(i+1,j) or dfs(i,j+1)
                return dp[(i,j)]
            #Only can use s1
            elif i<len(s1) and s1[i]==s3[i+j]:
                dp[(i,j)]=dfs(i+1,j)
                return dp[(i,j)]

            #Only can use s2
            elif j<len(s2) and s2[j]==s3[i+j]:
                dp[(i,j)]=dfs(i,j+1)

                return dp[(i,j)]
            #Impossible
            else:
                dp[(i,j)]=False
                return False
        return dfs(0,0)
    
    # Longest Increasing Path In a Matrix	https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
    # Given an m x n integers matrix, return the length of the longest increasing path in matrix.  
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS,COLS=len(matrix),len(matrix[0])
        dp={}
        def dfs(i,j,prev):
            if i<0 or j<0 or i>=ROWS or j>= COLS or matrix[i][j]>= prev:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            curr=matrix[i][j]
            dp[(i,j)]=1+ max(dfs(i+1,j,curr),dfs(i-1,j,curr),dfs(i,j+1,curr),dfs(i,j-1,curr))
            return dp[(i,j)]
        res=-1
        for r in range(ROWS):
            for c in range(COLS):
                res=max(dfs(r,c,math.inf),res)
        return res
    
    # Distinct Subsequences	https://leetcode.com/problems/distinct-subsequences/
    # Given two strings s and t, return the number of distinct subsequences of s which equals t.
    def numDistinctTopDown(self, s: str, t: str) -> int:
        dp={}
        def dfs(i,j):
           
            if i>=len(s) and j<len(t):
                return 0
            if j==len(t):
                return 1
            if (i,j) in dp:
                return dp[(i,j)]

            include=0
            dontInclude=dfs(i+1,j)
            if s[i]==t[j]:
                include=dfs(i+1,j+1)
            dp[(i,j)]=include+dontInclude
            return dp[(i,j)]
        res=dfs(0,0)
        for i in range(len(s)):
            print([dp[(i,j)] if (i,j) in dp else -1 for j in range(len(t)) ])
        return res
        

    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)  # Store lengths of s and t
        dp = [[0] * (m + 1) for _ in range(n + 1)]  # Create dp table

        # Initialize the last column (dp[r][m]) to 1 since an empty t can be formed from any suffix of s
        for r in range(n + 1):
            dp[r][m] = 1

        # Fill dp table from bottom-right to top-left
        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                # Add the result of skipping s[r]
                dp[r][c] = dp[r + 1][c]
                # If characters match, add the result of matching both s[r] and t[c]
                if s[r] == t[c]:
                    dp[r][c] += dp[r + 1][c + 1]

        return dp[0][0]  # The final answer is in dp[0][0]
    
    # Edit Distance	https://leetcode.com/problems/edit-distance/
    # Given two strings word1 and word2, return the minimum number of operations required 
    # to convert word1 to word2.
    # Insert a character Delete a character Replace a character
    def minDistanceTopDown(self, word1: str, word2: str) -> int:
        dp={}

        def dfs(i,j):
            if i>= len(word1) and j>=len(word2):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            delete=math.inf
            insert=math.inf
            use=math.inf
            replace=math.inf
            if i<len(word1):
                delete=1+dfs(i+1,j)
            if j<len(word2):
                insert=1+dfs(i,j+1)
            if i<len(word1) and j<len(word2):
                if word1[i]==word2[j]:
                    use=dfs(i+1,j+1)
                else:
                    replace=1+dfs(i+1,j+1)
            dp[(i,j)]=min(delete,insert,use,replace)
            return dp[(i,j)]
        return dfs(0,0)
    
    def minDistanceTopDown(self, word1: str, word2: str) -> int:
        ROWS,COLS=len(word1),len(word2)
        dp=[[0]* (COLS+1) for r in range(ROWS+1)]
        for r in range(ROWS,-1,-1):
            dp[r][-1]=ROWS-r
        for c in range(COLS,-1,-1):
            dp[-1][c]=COLS-c
        
        for i in range(ROWS-1,-1,-1):
            for j in range(COLS-1,-1,-1):
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i+1][j+1]
                else:
                    insert= 1+ dp[i][j+1]
                    replace=1+ dp[i+1][j+1]
                    delete=1+ dp[i+1][j]
                    dp[i][j]=min(insert,replace,delete)
        return dp[0][0]
    
    # Burst Balloons	https://leetcode.com/problems/burst-balloons/
    # Return the maximum coins you can collect by bursting the balloons wisely.
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0,1)
        nums.append(1)
        l,r=1,len(nums)-2
        dp={}

        def dfs(l,r):
            if l>r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]

            bestCoins=0
            for i in range(l,r+1):
                
                popIlast=nums[l-1]*nums[i]*nums[r+1]
                restOfCoins=dfs(l,i-1)+dfs(i+1,r)
                totalCoins=popIlast+restOfCoins

                bestCoins=max(bestCoins,totalCoins)
            dp[(l,r)]=bestCoins
            return bestCoins
        return dfs(l,r) 
    
    # Regular Expression Matching	https://leetcode.com/problems/regular-expression-matching/    
    # Given an input string s and a pattern p, implement 
    # regular expression matching with support for '.' and '*'
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            # If both pattern and string are fully matched
            if i == len(p) and j == len(s):
                return True

            # If pattern is consumed but string is not
            if i == len(p):
                return False

            # Check if characters match
            match = j < len(s) and (p[i] == '.' or p[i] == s[j])

            # Handle '*' wildcard
            if i + 1 < len(p) and p[i + 1] == '*':
                dp[(i, j)] = dfs(i + 2, j) or (match and dfs(i, j + 1))
            else:
                dp[(i, j)] = match and dfs(i + 1, j + 1)

            return dp[(i, j)]

        return dfs(0, 0)
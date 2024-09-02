
from collections import defaultdict
from typing import List


class Solution():

    # 70. Climbing Stairs     https://leetcode.com/problems/climbing-stairs/description/
    # It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.
    # In how many distinct ways can you climb to the top?
    def climbStairs(self, n: int) -> int:
        one=1
        two=1

        for _ in range(n-1):
            one=two+one
            two=one-two
        return one
        
    # 746. Min Cost Climbing Stairs       https://leetcode.com/problems/min-cost-climbing-stairs/description/
    # Return the minimum cost to reach the top of the floor.
    # Input: cost = [10,15,20]   Output: 15
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost)-3,-1,-1):
            cost[i]=min(cost[i+1],cost[i+2])+cost[i]
            print(*cost)
        return min(cost[0],cost[1])
    
    # 198. House Robber       https://leetcode.com/problems/house-robber/
    # Given an integer array nums representing the amount of money of each house, 
    # return the maximum amount of money you can rob tonight without alerting the police. Input: nums = [1,2,3,1] Output: 4
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        nums.append(0)

        for i in range(len(nums)-3,-1,-1):
            nums[i]= max(nums[i+2]+nums[i],nums[i+1])
            print(*nums)
        return max(nums[0],nums[1])
    
    # 213. House Robber II        https://leetcode.com/problems/house-robber-ii/description/
    # houses at this place are arranged in a circle.
    def rob2(self, nums: List[int]) -> int:
        def aux():
            rob1=0
            rob2=0
            for n in nums:
                temp=max(n+rob1,rob2)
                rob1=rob2
                rob2=temp
            return rob2
        return max(aux(nums[1:]),aux(nums[:-1]),nums[0])
    
    # 5. Longest Palindromic Substring        https://leetcode.com/problems/longest-palindromic-substring/description/        
    # Given a string s, return the longest palindromic substring in s. s = "babad" Output: "bab"
    def longestPalindrome(self, s: str) -> str:
        maxLen=0
        maxSubs=""

        for i in range(len(s)):
            l=i
            r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l +1>maxLen:
                    maxLen=r-l+1
                    maxSubs=s[l:r]
                l-=1
                r+=1
            l=i
            r=i+1       
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l +1>maxLen:
                    maxLen=r-l+1
                    maxSubs=s[l:r]
                l-=1
                r+=1
        return maxSubs
    
    # 647. Palindromic Substrings         https://leetcode.com/problems/palindromic-substrings/description/
    # Given a string s, return the number of palindromic substrings in it.
    def countSubstrings(self, s: str) -> int:
        amount=0

        for i in range(len(s)):
            l=i
            r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                amount+=1
                l-=1
                r+=1
            l=i
            r=i+1       
            while l>=0 and r<len(s) and s[l]==s[r]:
                amount+=1
                l-=1
                r+=1
        return amount
    
    # 91. Decode Ways         https://leetcode.com/problems/decode-ways/description/
    # Given a string s containing only digits, return the number of ways to decode it.
    def numDecodings(self, s: str) -> int:
        dp={len(s):1}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            if s[i]=="0":
                return 0
            
            res= dfs(i+1)

            if (s[i]=="1" or (s[i]=="2" and s[i+1] in "0123456")):
                res+= dfs(i+2)
            return res
        return dfs(0)
    
    # 322. Coin Change            https://leetcode.com/problems/coin-change/description/
    # Return the fewest number of coins that you need to make up that amount.
    def coinChange(self, coins: List[int], amount: int) -> int:

        #i want to calculate every amount up to amount
        #if i substract coin to amount, ill get to a known answer amount-coin<amount
        dp=[(amount+2)]*(amount+1)
        dp[0]=0

        for target in range (1,amount+1):

            for coin in coins:
                if target-coin>=0:
                    dp[target]=min(dp[target],dp[target-coin]+1)
                
                

        if dp[amount]==amount+2:
            return -1
        else:
            return dp[amount]
        
    # 152. Maximum Product Subarray
    # Given an integer array nums, find a subarray that has the largest product, and return the product.
    #store max and min and res, new max can be min*n, max*n , n
    def maxProduct(self, nums: List[int]) -> int:

        maxRes=nums[0]
        everything=1
        partial=1

        for n in nums:
            everything=n*everything
            partial=partial*n

            maxRes=max(maxRes,everything,partial)
            if n==0:
                everything=1
                partial=1

            elif partial<0:
                partial=1

        everything=1
        partial=1

        for i in range(len(nums)-1,-1,-1):
            everything=nums[i]*everything
            partial=partial*nums[i]

            maxRes=max(maxRes,everything,partial)
            if nums[i]==0:
                everything=1
                partial=1

            elif partial<0:
                partial=1

        return maxRes


    # 139. Word Break
    # Given a string s and a dictionary of strings wordDict, return true if s can be segmented
    # into a space-separated sequence of one or more dictionary words.
    def wordBreakBottomUp(self, s: str, wordDict: List[str]) -> bool:

        dp=[False]*(len(s)+1)
        dp[len(s)]=True

        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                j=i+len(word) #one character after end 
                if j<=len(s)  and s[i:j]==word:
                    dp[i]=dp[j]
                if  dp[i]:
                    break
        return dp[0]
    def wordBreakTopDown(self, s: str, wordDict: List[str]) -> bool:
        validStrings=set()
        invalidStrings=set()

        def dfs(s):
            if s in invalidStrings:
                return False
            if s in validStrings:
                return True
            if len(s)==0:
                return True
            validPath=False
            for w in wordDict:
                if s[:len(w)] in validStrings or len(s)>=len(w) and s[:len(w)]==w:
                    validPath=validPath or dfs(s[len(w):])
            if validPath:
                validStrings.add(s)
            else:
                invalidStrings.add(s)
                    
            return validPath
        return dfs(s)



    

    # 300. Longest Increasing Subsequence
    # Given an integer array nums, return the length of the longest strictly increasing subsequence.
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS=[1]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    LIS[i]=max(LIS[i],LIS[j]+1)
        return max(LIS)
    

    # 416. Partition Equal Subset Sum         https://leetcode.com/problems/partition-equal-subset-sum/description/
    # Given an integer array nums, return true if you can partition the array into two subsets such that the sum of
    # the elements in both subsets is equal or false
    def canPartition(self, nums: List[int]) -> bool: 
        if sum(nums)%2:
            return False
        target=sum(nums)//2
        dp=set([0])

        for n in  nums:
            nextDp=set()
            for t in dp:
                if t+n==target:
                    return True
                nextDp.add(t)
                nextDp.add(t+n)
            dp=nextDp
        return False






            




            



    
if __name__=="__main__":
    mySolution=Solution()
    # print(mySolution.climbStairs(5))

    # print(mySolution.minCostClimbingStairs(cost = [10,15,20]))

    # print(mySolution.rob(nums = [2,3,2]))

    mySolution.numDecodings("2232")

    
    



    
    


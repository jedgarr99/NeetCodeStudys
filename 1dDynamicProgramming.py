
import bisect
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
        oneStep=cost[-2]
        twoSteps=cost[-1]

        for i in range((len(cost)-3),-1,-1):
            bestOption=cost[i]+ min(oneStep,twoSteps)
            oneStep,twoSteps=bestOption,oneStep
        return min(oneStep,twoSteps)
        
    def minCostClimbingStairsExtraMemory(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost)-3,-1,-1):
            cost[i]=min(cost[i+1],cost[i+2])+cost[i]
            print(*cost)
        return min(cost[0],cost[1])
    
    # 198. House Robber       https://leetcode.com/problems/house-robber/
    # Given an integer array nums representing the amount of money of each house, 
    # return the maximum amount of money you can rob tonight without alerting the police. Input: nums = [1,2,3,1] Output: 4
    def rob(self, nums: List[int]) -> int:
        oneHouse=0
        twoHouses=0

        for i in range(len(nums)-1,-1,-1):
            curr=max(nums[i]+ twoHouses, oneHouse)
            oneHouse,twoHouses=curr,oneHouse
           
        return oneHouse
    
    def robExtraMemory(self, nums: List[int]) -> int:
        nums.append(0)
        nums.append(0)

        for i in range(len(nums)-3,-1,-1):
            nums[i]= max(nums[i+2]+nums[i],nums[i+1])
            print(*nums)
        return max(nums[0],nums[1])
    
    # 213. House Robber II        https://leetcode.com/problems/house-robber-ii/description/
    # houses at this place are arranged in a circle.
    def rob2(self, nums: List[int]) -> int:
        def robHelper(nums):
            oneHouse=0
            twoHouses=0

            for i in range(len(nums)-1,-1,-1):
                curr=max(nums[i]+ twoHouses, oneHouse)
                oneHouse,twoHouses=curr,oneHouse
            
            return oneHouse
        return max(robHelper(nums[:-1]),robHelper(nums[1:]),nums[0])
        
    
    # 5. Longest Palindromic Substring        https://leetcode.com/problems/longest-palindromic-substring/description/        
    # Given a string s, return the longest palindromic substring in s. s = "babad" Output: "bab"
    def longestPalindrome(self, s: str) -> str:
        self.maxPal=""
        self.maxLen=0
        def isPalindromeExpand(i,j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                if j-i+1>self.maxLen:
                    self.maxLen=j-i+1
                    self.maxPal=s[i:j+1]
                i-=1
                j+=1
            
        for i in range(len(s)):
            isPalindromeExpand(i,i)
            isPalindromeExpand(i,i+1)
           
        return self.maxPal
                
        
    
    # 647. Palindromic Substrings         https://leetcode.com/problems/palindromic-substrings/description/
    # Given a string s, return the number of palindromic substrings in it.
    def countSubstrings(self, s: str) -> int:
        self.numberPalindromes=0
        def isPalindromeExpand(i,j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                self.numberPalindromes+=1
                i-=1
                j+=1
            
        for i in range(len(s)):
            isPalindromeExpand(i,i)
            isPalindromeExpand(i,i+1)
           
        return self.numberPalindromes
        
    
    # 91. Decode Ways         https://leetcode.com/problems/decode-ways/description/
    # Given a string s containing only digits, return the number of ways to decode it.
    def numDecodings(self, s: str) -> int:
        dp={}
        def dfs(i):
            if i>=len(s):
                return 1
            if i in dp:
                return dp[i]

            dp[i]=0
            if s[i] !='0':
                dp[i]+=dfs(i+1)
                if i+1<len(s) and (s[i] =='1' or (s[i]=='2' and s[i+1] in "0123456")):
                    dp[i]+=dfs(i+2)
            return dp[i]
        return dfs(0)
    
    # 322. Coin Change            https://leetcode.com/problems/coin-change/description/
    # Return the fewest number of coins that you need to make up that amount.
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)  # Initialize with an impossible large value
        dp[0] = 0  # 0 coins are needed to make the amount 0

        for c in coins:
            for i in range(c, amount + 1):  # Start from `c` to avoid going out of bounds
                dp[i] = min(dp[i], dp[i - c] + 1)  # Either use the current coin or skip it

        return dp[amount] if dp[amount] != amount + 1 else -1
            
        
    # 152. Maximum Product Subarray
    # Given an integer array nums, find a subarray that has the largest product, and return the product.
    #store max and min and res, new max can be min*n, max*n , n
    def maxProduct(self, nums: List[int]) -> int:
        currMax=1
        currMin=1
        maxP=nums[0]

        for n in nums:
            if n==0: #not necessary
                currMax,currMin=1,1
            
            auxMax=currMax
            currMax=max(n,currMax*n,currMin*n)
            currMin=min(n,auxMax*n,currMin*n)

            maxP=max(maxP,currMax)

        return maxP
        


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
        dp={}

        def dfs(i):
            if i in dp:
                return dp[i]
            if i==len(s):
                return True

            dp[i]=False
            for word in wordDict:
                if s[i:i+len(word)]==word:
                    dp[i]=dp[i] or dfs(i+len(word))
            return dp[i]
        return dfs(0)

        
    

    # 300. Longest Increasing Subsequence
    # Given an integer array nums, return the length of the longest strictly increasing subsequence.
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS=[1]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    LIS[i]=max(LIS[i],LIS[j]+1)
        return max(LIS)
    
    def lengthOfLISBinary(self, nums: List[int]) -> int:
       # List to store the smallest tail of all increasing subsequences
        subseq = []

        for num in nums:
            # Find the index where 'num' can replace an element in 'subseq'
            idx = bisect.bisect_left(subseq, num)
            
            # If 'num' is larger than any element in 'subseq', it extends the subsequence
            if idx == len(subseq):
                subseq.append(num)
            else:
                # Otherwise, replace the existing element with 'num' to maintain the smallest possible tail
                subseq[idx] = num

        # The length of 'subseq' is the length of the longest increasing subsequence
        return len(subseq)
    

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

    
    



    
    



from typing import List


class Solution:

    # 1143. Longest Common Subsequence        https://leetcode.com/problems/longest-common-subsequence/
    # Given two strings text1 and text2, return the length of their longest common subsequence. If there 
    # is no common subsequence, return 0.
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[]


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
        
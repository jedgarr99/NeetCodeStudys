    
from collections import Counter, deque
from typing import List


class Solution():

    # 121. Best Time to Buy and Sell Stock        https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
    # Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    def maxProfit(self, prices: List[int]) -> int:
        profit,l,r=0,0,1

        while r<len(prices):
            if prices[r]<prices[l]:
                l,r=r,r+1
            else:
                profit=max(profit,prices[r]-prices[l])
                r+=1
        return profit   
    
    # 3. Longest Substring Without Repeating Characters       https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
    # Given a string s, find the length of the longest substringwithout repeating characters.
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring=set()
        subLen,res,l,r=0,0,0,0
        while r<len(s):
            if s[r] in substring:
                res=max(res,subLen)
                while s[r] in substring:
                    substring.remove(s[l])
                    subLen-=1
                    l+=1
            substring.add(s[r])
            r+=1
            subLen+=1
        res=max(res,subLen)
        return res



    
    # 424. Longest Repeating Character Replacement        https://leetcode.com/problems/longest-repeating-character-replacement/description/
    # Return the length of the longest substring containing the same letter you can get after performing the above operations.
    #esta lento 
    def characterReplacement(self, s: str, k: int) -> int:
        count=defaultdict(int)
        res,l,most=0,0,0

        for r in range(len(s)):
            count[s[r]]+=1
            most=max(most, count[s[r]])
            while (r-l+1)-most>k:
                count[s[l]]-=1
                most=max(most,count[s[l]])
                l+=1
            res=max(res,r-l+1)
        return res 
    

    # 567. Permutation in String      https://leetcode.com/problems/permutation-in-string/description/
    # return true if one of s1's permutations is the substring of s2.
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter={}
        for c in s1:
            if c not in counter:
                counter[c]=0
            counter[c]+=1
        l=0
        for r in range(len(s2)):
            #print((l,r,s2[r]))
            if s2[r] not in counter:
                while l<r:
                    counter[s2[l]]+=1 
                    l+=1
                l+=1
            else:
                counter[s2[r]]-=1
                while counter[s2[r]]<0:
                    counter[s2[l]]+=1
                    l+=1
                if (r-l+1)==len(s1):
                    return True
        return False
    

    #76. Minimum Window Substring       https://leetcode.com/problems/minimum-window-substring/description/
    # Given two strings s and t of lengths m and n respectively, return the minimum window substring
    # of s such that every character in t (including duplicates) is included in the window.
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        
        counter={}
        for c in t:
            if c not in counter:
                counter[c]=0
            counter[c]+=1
        util,l,maxLen=0,0,len(s)
        index=[0,0]

        for r in range(len(s)):
            if s[r] in counter:
                counter[s[r]]-=1
                util+=1 if counter[s[r]]>=0 else 0
                #print('Agregando ',s[r],' ',util)
                if util>= len(t):

                    while util>=len(t):
                        
                        if s[l] in counter:
                            counter[s[l]]+=1
                            util-=1 if counter[s[l]]>0 else 0
                            #print('Quitando ',s[l],' ',util)
                        l+=1
                    l-=1
                    counter[s[l]]-=1
                    util+=1 if counter[s[l]]>=0 else 0
                    #print('Regresando ',s[l],' ',util)
                if util >= len(t) and (r-l+1)<=maxLen:
                    #print('Nuevo rango ',(l,r))
                    maxLen=r-l+1
                    index=[l,r+1]
        return s[index[0]:index[1]]
                

        


    #239. Sliding Window Maximum        https://leetcode.com/problems/sliding-window-maximum/description/
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res=[]
        l=r=0
        que=deque()

        for r in range(len(nums)):

            #check que to delete smaller elements and add next
            while que and nums[que[-1]]<nums[r]:
                que.pop()
            que.append(r)
            
            #check que to delete out of window elements
            if  que[0]<l:
                que.popleft()

            #update res
            if r-l+1>=k:
                res.append(nums[que[0]])
                l+=1
        
        return res
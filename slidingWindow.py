    
from collections import Counter, deque
from typing import List


class Solution():

    # 121. Best Time to Buy and Sell Stock        https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
    # Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    def maxProfit(self, prices: List[int]) -> int:
        return
    
    # 3. Longest Substring Without Repeating Characters       https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
    # Given a string s, find the length of the longest substringwithout repeating characters.
    def lengthOfLongestSubstring(self, s: str) -> int:
        return
    
    # 424. Longest Repeating Character Replacement        https://leetcode.com/problems/longest-repeating-character-replacement/description/
    # Return the length of the longest substring containing the same letter you can get after performing the above operations.
    #esta lento 
    def characterReplacement(self, s: str, k: int) -> int:
        rep=[0]*26
        l=0
        r=0
        chain=0
        while r<len(s):
            rep[ord(s[r])-65]+=1
            # print(*rep)
            repeating=0
            total=0
            for i in range(len(rep)):
                print(i)
                total+=rep[i]
                if rep[i]>rep[repeating]:
                    repeating=i
            print('l ',l,'r ',r,chr(repeating+65))

            if total-rep[repeating]>k:
                rep[ord(s[l])-65]=rep[ord(s[l])-65]-1
                l+=1
            else:
                if r-l+1>chain:
                    chain=r-l+1
            # print(*rep)
            # print(chain)

            r+=1
        return chain
    

    # 567. Permutation in String      https://leetcode.com/problems/permutation-in-string/description/
    # return true if one of s1's permutations is the substring of s2.
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letter_counts =Counter(s1)
        l=0
        r=0
        perm=False
        total=len(s1)
        thisCounts=letter_counts.copy()

        #traverse the array until i find perm or r is out of bounds

        while not perm and r<len(s2):

            #check r, its part of permutation or not 
            if s2[r] in thisCounts:
                # print('Case 1 l: ',l, 'r ',r, 'total', total)

                #either that letter still needs to be found, or not
                if thisCounts[s2[r]]>0:
                    thisCounts[s2[r]]-=1
                    r+=1
                    total-=1
                    print(total)
                    if total==0:
                        perm =True
                # i need to move my left until I find the character that had too many appearances, and then on more
                #meanwhile, i need to adjust the counters
                else:

                    while s2[l]!=s2[r]:
                        
                        thisCounts[s2[l]]+=1
                        total+=1
                        l+=1
                    # i found it, so i update it and move to the next one
                    thisCounts[s2[l]]+=1
                    l+=1
                    thisCounts[s2[r]]-=1
                    r+=1

            #if not, possibility ends so we restart from next position of r
            else:
                print('Case 2 l: ',l, 'r ',r, 'total', total)
                l=r+1
                r+=1
                thisCounts=letter_counts.copy() 
                total=len(s1)

        return perm
    

    #76. Minimum Window Substring       https://leetcode.com/problems/minimum-window-substring/description/
    # Given two strings s and t of lengths m and n respectively, return the minimum window substring
    # of s such that every character in t (including duplicates) is included in the window.
    def minWindow(self, s: str, t: str) -> str:
        
        minWindow=""
        l=0
        r=0
        counts=Counter(t)
        

        #find first window
        #remove first letter in t and excess
        while r<len(s):
            # print('l ',l,'r ',r)
            # for i in range(l,r+1):
            #     print(s[i], end=" ")
            # print(' ')
            # for key,value in counts.items():
            #     print(key,' ',value ,end=" ")
            # print(' ')

            #move l to start of next window
            while l<len(s) and s[l] not in counts :
                l+=1
            if l>=len(s):
                break
            if r==l:
                counts=Counter(t)
                counts[s[r]]-=1
            if r<l:
                # print('xxxx')
                r=l
                counts=Counter(t)
                counts[s[r]]-=1
            
            if s[r] in counts :
                
                
                #either i finished my window, or not 
                validWindow=True
                for value in counts.values():
                    if value>0:
                        validWindow=False
                        break
                if validWindow:
                    # print('Valid window')

                    if len(minWindow)==0 or r-l+1<len(minWindow):
                       
                        newWindow=""
                        for i in range(l,r+1):
                            newWindow+=s[i]
                  
                        minWindow=newWindow
                    

                    counts[s[l]]+=1
                    l+=1
                else:
                    r+=1
                    while r<len(s) and s[r] not in counts:
                        r+=1
                    
                    if r<len(s):
                        counts[s[r]]-=1

            else:
                r+=1
       
        return minWindow


    #239. Sliding Window Maximum        https://leetcode.com/problems/sliding-window-maximum/description/
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res=[]
        l=r=0
        que=deque()

        while r<len(nums):

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
            r+=1
        return res
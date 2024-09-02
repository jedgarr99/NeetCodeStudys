from collections import Counter, deque
import heapq
from typing import List


class Solution():

    # 53. Maximum Subarray        https://leetcode.com/problems/maximum-subarray/description/
    # Given an integer array nums, find the subarray with the largest sum, and return its sum.
    def maxSubArray(self, nums: List[int]) -> int:
        curr,res=0,nums[0]

        for n in nums:
            curr= max(curr+n,n)
            res=max(curr,res)
            
        return res

       
    
    # 55. Jump Game       https://leetcode.com/problems/jump-game/description/
    # You are given an integer array nums. You are initially positioned at the array's first 
    # index, and each element in the array represents your maximum jump length at that position.
    # Return true if you can reach the last index, or false otherwise.
    def canJump(self, nums: List[int]) -> bool:
        target=len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=target:
                target=i
        return target==0
        # maxJump=0
        # for i in range(len(nums)):
        #     if i>maxJump:
        #         return False
        #     maxJump=max(maxJump, i+nums[i])
        #     if maxJump>=len(nums)-1:
        #         return True
        # return False
    
    # 45. Jump Game II        https://leetcode.com/problems/jump-game-ii/description/
    # Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated 
    # such that you can reach nums[n - 1].
    def jump(self, nums: List[int]) -> int:
        currentLimit=0
        maxJump=0
        jumps=0
        for i in range(len(nums)):
            if i>currentLimit:
                currentLimit=maxJump
                jumps+=1
            maxJump=max(maxJump,i+nums[i])
        return jumps
    
    # 134. Gas Station        https://leetcode.com/problems/gas-station/description/
    # Given two integer arrays gas and cost, return the starting gas station's index if you 
    # can travel around the circuit once in the clockwise direction, otherwise return -1.
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas,totalCost=sum(gas),sum(cost)
        if totalCost>totalGas: return -1

        gain=[g-c for g, c in zip(gas,cost)]
        index,curr=0,0

        for i in range(len(gain)):
            curr+=gain[i]
            if curr<0:
                index=i+1
                curr=0
        return index
    
    # Hand of Straights       https://leetcode.com/problems/hand-of-straights/
    # return true if she can rearrange the cards, or false:  rearrange the cards into groups 
    # so that each group is of size groupSize, and consists of groupSize consecutive cards
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cardCount=Counter(hand)
        minHeap=list(set(hand))
        heapq.heapify(minHeap)

        while minHeap:
            nextCard=minHeap[0]       
            for i in range(groupSize):
                if nextCard in cardCount and cardCount[nextCard]>0:
                    cardCount[nextCard]-=1
                    nextCard+=1  
                else:
                    return False
  
            while minHeap and cardCount[minHeap[0]]==0:
                heapq.heappop(minHeap)

        return True
    
    # 1899. Merge Triplets to Form Target Triplet https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
    # Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets,
    # or false otherwise.
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res=[0,0,0]
        for t in triplets:
            if t[0]<=target[0] and t[1]<=target[1] and t[2]<=target[2]:
                res=[max(res[0],t[0]),max(res[1],t[1]),max(res[2],t[2])]
        return res==target
    
    # Partition Labels        https://leetcode.com/problems/partition-labels/
    # We want to partition the string into as many parts as possible so that each 
    # letter appears in at most one part.
    def partitionLabels(self, s: str) -> List[int]:
        indexes={}
        for i in range(len(s)):
            if s[i] not in indexes:
                indexes[s[i]]=[i,i]
            else:
                indexes[s[i]][1]=i
                
        res=[]
        l,r=0,0
        for i in range(len(s)):
            r=max(r,indexes[s[i]][1])
            if i==r:
                res.append(r-l+1)
                l,r=i+1,i+1

        return res

    # 678. Valid Parenthesis String       https://leetcode.com/problems/valid-parenthesis-string/description/
    # Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
    def checkValidString(self, s: str) -> bool:
        stack=deque()
        for c in s:
            if c=='(':
                stack.append('(')
            elif c==')':
                if not stack:
                    return False
                if stack[-1]=='(':
                    stack.pop()
                
            elif c=='*':
                stack.append('*')
        print(stack)
        stack2=deque()
        while stack:
            last=stack.popleft()
            if last=='(':
                stack2.append('(')
            elif last=='*' and stack2:
                stack2.pop()
            else:
                return False
        return not stack2

        
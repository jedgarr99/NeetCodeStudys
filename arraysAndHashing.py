from collections import Counter
from typing import List

class Solution:

    # 217. Contains Duplicate   https://leetcode.com/problems/contains-duplicate/description/
    # Given an integer array nums, return true if any value appears at least twice in the array,
    # and return false if every element is distinct.
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet=set()
        isDuplicate=False
        for num in nums:
            if num in numsSet:
                isDuplicate=True
                break
            else:
                numsSet.add(num)
        return isDuplicate
    


    # 242. Valid Anagram   https://leetcode.com/problems/valid-anagram/description/
    # Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen={}
        for letter in s:
            if letter in seen:
                seen[letter]+=1
            else:
                seen[letter]=1
        
        for letter in t:
            if letter not in seen:
                return False
            else:
                seen[letter]-=1
                if seen[letter]<0:
                    return False
        return True

    def isAnagram(self, s:str,t:str)-> bool:
        if len(s) != len(t):
            return False
        
        counter = [0]*26

        for c in s:
            counter[ord(c)-ord('a')]+=1

        for c in t:
            counter[ord(c)-ord('a')]-=1
            if counter[ord(c)-ord('a')]<0:
                return False
        return True
        
    # 1. Two Sum       https://leetcode.com/problems/two-sum/description/    
    # Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        resultIndex={}
        for index  in range(len(nums)):
            print(index)
            if (target-nums[index]) in resultIndex:
                #print([resultIndex.get(target-nums[index]),index])
                return [resultIndex.get(target-nums[index]),index]
            else:
                resultIndex[nums[index]]=index
                #print('result '+str(nums[index])+ 'index   '+str(index))
        return [-1,-1]
    

    # 49. Group Anagrams          https://leetcode.com/problems/group-anagrams/description/
    # Given an array of strings strs, group the anagrams together.
    #using dictionaries bring order problem, you can use an array instead 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getKey(word):
            key=[0]*26
            for c in word:
                key[ord(c)-ord('a')]+=1
            return tuple(key)
        
        anagrams={}
        for word in strs:
            key=getKey(word)
            if key not in anagrams:
                anagrams[key]=[]
            anagrams[key].append(word)

        res=[]
        for key in anagrams:
            res.append(anagrams[key])
        return res
    
    #347. Top K Frequent Elements        https://leetcode.com/problems/top-k-frequent-elements/description/
    #Given an integer array nums and an integer k, return the k most frequent elements. 
    # You may return the answer in any order.
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter={}

        for x in nums:
            if x not in counter:
                counter[x]=0
            counter[x]+=1
        
        freq=[[] for i in range(len(nums)+1)]
        for num, f in counter.items():
            freq[f].append(num)
        #print(freq)
        res=[]
        for i in range(len(nums),0,-1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res)==k:
                    return res
    #String Encode and Decode
    # Design an algorithm to encode a list of strings to a single string.
    # The encoded string is then decoded back to the original list of strings.

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=str(len(s))+'&'+s
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        print(s)

        l=0
        while l < len(s):
            r=l
            while s[r]!= '&':
                r+=1
            print('aaa',s[l:r])
            wordLength=int(s[l:r])
            print(s[r+1:r+2+wordLength])
            res.append(s[r+1:r+1+wordLength])
            l=r+1+wordLength
        return res

    
    # 238. Product of Array Except Self            https://leetcode.com/problems/product-of-array-except-self/description/
    # Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product=1
        zeros=0
        
        for x in nums:
            if x == 0:
                zeros+=1
                if zeros ==2:
                    product=0
                    break
            else:
                product = product*x

        result=[0]*len(nums)

        if zeros==0:
            
            for i in range(len(nums)):
                result[i]=int(product/nums[i])
        elif zeros==1:
            for i in range(len(nums)):
                if nums[i]==0:
                    result[i]=product

        return result
    
    # 36. Valid Sudoku           https://leetcode.com/problems/valid-sudoku/description/
    # Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        #check rows
        for i in range(9):
            check=set()
            for j in range(9):
                if board[i][j]!='.':
                    if board[i][j] not in check:
                        check.add(board[i][j])
                    else:
                        return False

        #check columns
        for j in range(9):
            check=set()
            for i in range(9):
                if board[i][j]!='.':
                    if board[i][j] not in check:
                        check.add(board[i][j])
                    else:
                        return False

        for x in range (3):
            for y in range (3):

                check=set()
                for i in range(3):
                    for j in range(3):
                        if board[i+(x*3)][j+(y*3)] not in check:
                            check.add(board[i+(x*3)][j+(y*3)])
                        else:
                            return False
        return True
    
    # 128. Longest Consecutive Sequence       https://leetcode.com/problems/longest-consecutive-sequence/description/
    # Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet=set(nums)
        maxSequence=0

        for x in nums:
            if (x -1) not in numsSet:
                seqLen=1
                num=x+1
                while num in numsSet:
                    num+=1
                    seqLen+=1
                if seqLen>maxSequence:
                    maxSequence=seqLen
        return maxSequence



        

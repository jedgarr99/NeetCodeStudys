from typing import List


class Solution:

    # 125. Valid Palindrome       https://leetcode.com/problems/valid-palindrome/description/
    # Given a string s, return true if it is a palindrome, or false otherwise.
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        valid=set(c for c in "asdfghjklqwertyuiopzxcvbnm1234567890")
        l,r=0,len(s)-1

        while l<r:
            if not s[l] in valid or not s[r] in valid:
                if not s[l] in valid:                
                    l+=1
                if not s[r] in valid:
                    r-=1
            else:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
        return True

    
    # 167. Two Sum II - Input Array Is Sorted         https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
    # Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]<target:
                l+=1
            elif numbers[l]+numbers[r]>target: 
                r-=1
            else:
                return [l+1,r+1]
        return [-1,-1]      

    # 15. 3Sum        https://leetcode.com/problems/3sum/description/
    # Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        i=0
        while i <len(nums)-2:
            l=i+1
            r=len(nums)-1

            while l<r:
                if nums[i]+nums[l]+nums[r]<0:
                    l+=1
                elif nums[i]+nums[l]+nums[r]>0:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    curr=nums[l]
                    while l<len(nums) and nums[l]==curr:
                        l+=1
                    r-=1
                    
            curr=nums[i]
            while i<len(nums) and nums[i]==curr:
                i+=1
        return res
    
    # 11. Container With Most Water       https://leetcode.com/problems/container-with-most-water/description/
    # Find two lines that together with the x-axis form a container, such that the container contains the most water.
    def maxArea(self, height: List[int]) -> int:
        res=0
        l,r=0,len(height)-1

        while l<r:
            res=max(res,(r-l)*min(height[l],height[r]))
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
                
        return res
    
    # 42. Trapping Rain       https://leetcode.com/problems/trapping-rain-water/description/
    # Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
    def trap(self, height: list[int]) -> int:
        water,l,r=0,0,len(height)-1
        maxL,maxR=height[l],height[r]

        while l<r:
            if height[l]<height[r]:
                l+=1
                maxL=max(maxL,height[l])
                water+=maxL-height[l] #if min(maxL,maxR)-height[l]>0 else 0
                #print(min(maxL,maxR)-height[l])
            else:
                r-=1
                maxR=max(maxR,height[r])
                water+=maxR-height[r] #if min(maxL,maxR)-height[r]>0 else 0
                #print(min(maxL,maxR)-height[r])
        return water



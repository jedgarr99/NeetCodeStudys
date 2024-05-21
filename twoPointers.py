from typing import List


class Solution:

    # 125. Valid Palindrome       https://leetcode.com/problems/valid-palindrome/description/
    # Given a string s, return true if it is a palindrome, or false otherwise.
    def isPalindrome(self, s: str) -> bool:
        sen=s.lower()
        res=True

        i=0
        j=len(sen)-1
        while res and i < len(sen)/2 and j>  len(sen)/2 :
            
            while i < len(sen)/2 and not (sen[i].isalpha()):
                i+=1
            while j > len(sen)/2 and not( sen[j].isalpha()):
                j-=1
            
            print(sen[i])
            print(sen[j])
            if sen[i]!= sen[j]:

                res=False
            i+=1
            j-=1
        return res
    
    # 167. Two Sum II - Input Array Is Sorted         https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
    # Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return True

    # 15. 3Sum        https://leetcode.com/problems/3sum/description/
    # Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return
    
    # 11. Container With Most Water       https://leetcode.com/problems/container-with-most-water/description/
    # Find two lines that together with the x-axis form a container, such that the container contains the most water.
    def getArea(self,l:int, lHeight:int, r:int, rHeight:int):
        print('l  ',l, 'l geight  ',lHeight , 'r'   ,r,'rHeight  ', rHeight)
        return (r-l)*min(lHeight,rHeight)

    def maxArea(self, height: list[int]) -> int:
        l=0
        r=len(height)-1
        maxL=l
        maxR=r
        maxArea=Solution.getArea(self,l,height[l],r,height[r])

        while l<r:
            if height[l]< height[r]:
                l+=1
            else:
                r-=1

            newArea=Solution.getArea(self,l,height[l],r,height[r])
            print(newArea)
            if newArea>maxArea:
                maxL=l
                maxR=r
                maxArea=newArea
        return maxArea
    
    # 42. Trapping Rain       https://leetcode.com/problems/trapping-rain-water/description/
    # Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

    # def trap(self, height: list[int]) -> int:
    #     add=defaultdict(int)
    #     adding=0
    #     total=0
    #     c=0
    #     for h in height:

    #         #continue accumulating
    #         if h< adding:
    #             print('accumulating in', c, 'until height ',adding)    
    #             for i in range(h,adding):
    #                 add[i]+=1
    #             for i in range(h):
    #                 total += add[i]
    #                 add[i]=0
                
                

    #         #stop accumulting
    #         else:
    #             print('Stop accumulating ', c)           
    #             for i in range(h):
    #                 total += add[i]
    #                 add[i]=0
    #             print('total',total)   
    #             adding=h
    #         c+=1
    #     return total
    
    def trap(self, height: list[int]) -> int:
        total=0
        l=0
        r=len(height)-1
        minimum=0

        while l <r:
            
            
            if l<=r:
                acumulate=minimum-height[l]
                if acumulate>0:
                    total+=acumulate
                l+=1
            else:
                acumulate=minimum-height[r]
                if acumulate>0:
                    total+=acumulate
                r-=1

            newLimit=min(height[l],height[r])
            if newLimit>minimum:
                minimum=newLimit


        return total


import math
from typing import List


class Solution():

    # 704. Binary Search          https://leetcode.com/problems/binary-search/description/
    # write a function to search target in nums
    def search(self, nums: list[int], target: int) -> int:
        l,r=0,len(nums)-1

        while l<=r:
            mid=(l+r)//2
            if nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                return mid
        return -1
        
        

    # 74. Search a 2D Matrix      https://leetcode.com/problems/search-a-2d-matrix/description/
    # Given an integer target, return true if target is in matrix or false otherwise.
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows=len(matrix)
        columns= len(matrix[0]) if rows>0 else 0
        l=0
        h=rows*columns-1
        

        while l<h:
            mid=l+int((h-l)/2) #lower midpoint 
            midMatrix=matrix[int(mid/columns)][mid%columns]

            #target is in upper half
            if target > midMatrix:
                l=mid+1
            #target is in   upper half
            else:
                h=mid

        # Alternative
        # if matrix[int(l/columns)][l%columns] ==target:
        #     return True
        # else:
        #     return False
        
        # if not matrix:
        #     return False

        # l,rowL,r,rowR,row=0,0,len(matrix[0])-1 ,len(matrix)-1,-1

        # while rowL<=rowR:
        #     midRow=(rowL+rowR)//2
        #     if target <matrix[midRow][0]:
        #         rowR=midRow-1
                
        #     elif target>matrix[midRow][r]:
        #         rowL=midRow+1
                
        #     else:
        #         row=midRow
        #         break
        # if row==-1:
        #     return False
        
        # while l<=r:
        #     mid=(r+l)//2
        #     if target<matrix[row][mid]:
        #         r=mid-1
        #     elif target>matrix[row][mid]:
        #         l=mid+1
        #     else:
        #         return True
        # return False
    

#875. Koko Eating Bananas       https://leetcode.com/problems/koko-eating-bananas/description/
# Return the minimum integer k such that she can eat all the bananas within h hours.
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def isPosible(k):
            if not k:
                return False
            tot=0
            for p in piles:
                tot+=math.ceil(p/k)
            return tot<=h
        if h<len(piles):
            return -1

        res=max(piles)
        l,r=0,res
        #want to find possible(k-1) notpossible(k)
        while l<=r:
            mid=(l+r)//2
            if isPosible(mid) and isPosible(mid-1):
                r=mid-1
                
            elif not isPosible(mid) and not isPosible(mid-1):
                l=mid+1
               
            else:
                return mid 
        return -1
    
    # 153. Find Minimum in Rotated Sorted Array       https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
    # Given the sorted rotated array nums of unique elements, return the minimum element of this array.
    def findMin(self, nums: list[int]) -> int:
        l,r,res=0,len(nums)-1,nums[0]

        while l<=r:
            if nums[l]<nums[r]:
                return min(res,nums[l])
                
            mid=(r+l)//2
            res=min(nums[mid],res)
            if nums[l]<=nums[mid]:
                l=mid+1          
            else:
                r=mid-1
        return res
            
    
    #33. Search in Rotated Sorted Array ( )     https://leetcode.com/problems/search-in-rotated-sorted-array/description/
    #Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
    def searchRotated(self, nums: list[int], target: int) -> int:
        l,r=0,len(nums)-1

        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid

            #left part is sorted , think of 4 5 6 7< 8 0 1
            if nums[l]<=nums[mid]:
                if target > nums[mid] or target< nums[l]:
                    l=mid+1
                else:
                    r=mid-1
            #right part is sorted 
            else:
                if target<nums[mid] or target>nums[r]:
                    r=mid-1
                else:
                    l=mid+1
        return -1
    
    # Median of Two Sorted Arrays     https://leetcode.com/problems/median-of-two-sorted-arrays/description/
    # Given two sorted arrays nums1 and nums2 of size m and n respectively, 
    # return the median of the two sorted arrays.
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total=len(nums1)+len(nums2)
        half=total//2
        a,b=nums1,nums2
        if len(b)<len(a):
            a,b=b,a
        l,r=0,(len(a)-1)
        while True:
            i=(l+r)//2
            j=half-i-2

            leftA=a[i]  if i>=0 else -math.inf
            rightA=a[i+1] if i+1 <len(a) else math.inf
            leftB=b[j]  if j>=0 else -math.inf
            rightB=b[j+1] if j+1 <len(b) else math.inf
            if leftA<=rightB and leftB<=rightA:
                if total%2:
                    return min(rightA,rightB)
                else:
                    return (min(rightA,rightB)+max(leftA,leftB))/2
            elif leftA>rightB:
                r=i-1
            else:
                l=i+1
# 981. Time Based Key-Value Store     https://leetcode.com/problems/time-based-key-value-store/description/                
class TimeMap:

    def __init__(self):
        self.tMap={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tMap:
            self.tMap[key]=[]
        self.tMap[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tMap:
            return ""
        values=self.tMap[key]
        l, r=0,len(values)-1
        bestSol=""
        while l<=r:
            mid=(l+r)//2
            if values[mid][0]==timestamp:
                return values[mid][1]
            elif values[mid][0]<timestamp:
                bestSol=values[mid][1]
                l=mid+1
            else:
                r=mid-1
        return bestSol
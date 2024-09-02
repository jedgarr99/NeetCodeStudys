

import math


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

            #left part is sorted , think of 4 5 6 7 8 0 1
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
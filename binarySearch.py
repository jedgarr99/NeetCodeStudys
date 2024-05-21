



class Solution():

    # 704. Binary Search          https://leetcode.com/problems/binary-search/description/
    # write a function to search target in nums
    def search(self, nums: list[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while l<r:
            mid=l+int((r-l)/2) #lower middle
            if target > nums[mid]:
                l=mid+1
            else:
                r=mid
        if nums[l]==target:
            return l
        else:
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
            #target is in upper half
            else:
                h=mid


        if matrix[int(l/columns)][l%columns] ==target:
            return True
        else:
            return False
    

#875. Koko Eating Bananas       https://leetcode.com/problems/koko-eating-bananas/description/
# Return the minimum integer k such that she can eat all the bananas within h hours.
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def valid(n):
            total=0
            for x in piles:
                total+=ceil(x/n)
            
            if total<=h:
                return True
            else:
                return False
                
        if len(piles)>h:
            return -1

        #initialize variable
        l=1
        r=max(piles)

        while l<r:
            mid=l+int((r-l)/2) #lower mid

            isMidValid=valid(mid)

            # if mid-1>0:
            #     isBefMidInvalid=valid(mid-1)
            # else:
            #     isBefMidInvalid=False
            # isValid= isMidValid and not isBefMidInvalid

            #answer is after the middle
            if not isMidValid:
                l=mid+1
            #answer is before the middle
            else:
                r=mid
            
        return l
    
    # 153. Find Minimum in Rotated Sorted Array       https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
    # Given the sorted rotated array nums of unique elements, return the minimum element of this array.
    def findMin(self, nums: list[int]) -> int:
        l=0
        h=len(nums)-1

        while l<h:
            mid=l +int((h)/2) #lower mid

            #i want to move l +1 to avoid infinite loop
            # answer is in lower half
            if nums[mid]<nums[h]:
                h=mid
            #answer is in upper half
            else:
                l=mid+1
        return nums[l]
    
    #33. Search in Rotated Sorted Array ( )     https://leetcode.com/problems/search-in-rotated-sorted-array/description/
    #Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
    def searchRotated(self, nums: list[int], target: int) -> int:
        l=0
        h=len(nums)-1

        while l<h:
            mid= l+int((h-l)/2)#lower mid
            #se invierten en la primera mitad
            if nums[mid]<nums[h]:
                
                #el elemento esta en la primera mitad
                if target<nums[mid] or target>nums[h]:
                    h=mid   

                #el elemento esta en la segunda mitad
                else:
                    l=mid+1

            #se invierten en la segunda mitad
            else:
                #el elemento esta en la segunda mitad
                if target<nums[l] or target>nums[mid]:
                    l=mid+1

                #el elemento esta en la primera mitad
                else:
                    h=mid
                    
        if nums[l]==target:
            return l
        else:
            return -1
        


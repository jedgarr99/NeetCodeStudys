import math
from typing import List


class Solution:
    # 136. Single Number      https://leetcode.com/problems/single-number/description/
    # Given a non-empty array of integers nums, every element appears twice except for one. 
    # Find that single one.
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for n in nums:
            res ^=n
        return res
    

    # 191. Number of 1 Bits       https://leetcode.com/problems/number-of-1-bits/description/
    # Write a function that takes the binary representation of a positive integer and returns the number of 
    # set bits it has
    def hammingWeight(self, n: int) -> int:
        res=0
        while n:
            res+= n&1
            n>>=1
        return res
    
    def hammingWeightAlternative(self, n: int) -> int:
        res=0
        while n:
            res+=1
            n=n&(n-1)
            print(res)
        return res
    
    # Counting Bits   https://leetcode.com/problems/counting-bits/
    def countBits(self, n: int) -> List[int]:
        dp=[0]*(n+1)
        offset=1

        for i in range(1,n+1):
            if offset*2==i:
                offset*=2
            dp[i]=1+dp[i-offset]
        return dp
    
    # 190. Reverse Bits       https://leetcode.com/problems/reverse-bits/
    # Reverse bits of a given 32 bits unsigned integer.
    def reverseBits(self, n: int) -> int:
        res=0
        for i in range(32):
            res<<=1
            res= res+(n&1)
            n>>=1
        return res
    
    # Missing Number      https://leetcode.com/problems/missing-number/
    # Given an array nums containing n distinct numbers in the range [0, n], 
    # return the only number in the range that is missing from the array.
    def missingNumber(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            res=res^i+1
            res=res^nums[i]
        return res
    
    # 371. Sum of Two Integers        https://leetcode.com/problems/sum-of-two-integers/description/
    # Given two integers a and b, return the sum of the two integers without using the operators + and -.
    
    # This code works in java, because it uses fixed length ints and twos complement representation (so the 
    # code behaves like a sum 4 + (-3) )
    def getSumJavaVersion(self, a: int, b: int) -> int:

        while b:
            aux=(a&b)<<1
            a=a^b
            b=aux
        return a
    
    def getSum(self, a: int, b: int) -> int:
        # Define 32-bit integer mask and maximum positive integer in 32-bit
        MAX = 0xFFFFFFFF  # 32-bit mask
        INT_MAX = 0x7FFFFFFF  # Maximum positive int in 32-bit

        while b != 0:
            aux = (a & b) << 1 & MAX  # Calculate carry and mask to 32-bit
            a = (a ^ b) & MAX         # Calculate sum without carry and mask to 32-bit
            b = aux                   # Carry is shifted and reassigned

        # If a is negative (i.e., exceeds INT_MAX), return its 32-bit negative equivalent
        return a if a <= INT_MAX else ~(a ^ MAX)
    
    # Reverse Integer     https://leetcode.com/problems/reverse-integer/description/
    # return x with its digits reversed. If reversing x causes the value to go outside 
    # the signed 32-bit integer range [-231, 231 - 1], then return 0.
    def reverse(self, x: int) -> int:
        # Integer.MAX_VALUE = 2147483647 (end with 7)
        # Integer MIN_VALUE = 2147483648 (end with -8 )
        MIN = -2147483648
       
        MAX = 2147483647
        res = 0
        while x:
            digit = int (math.fmod(x,10))
            x = int(x / 10)

            if(res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10)):
                return 0
            if (res < MIN // 10 or (res == MIN // 10 and digit <= MIN % 10)): 
                return 0
            res = (res * 10) + digit
        return res


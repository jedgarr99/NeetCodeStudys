
from collections import deque
import heapq
import math
from typing import List

# 703. Kth Largest Element in a Stream        https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
# Design a class to find the kth largest element in a stream. Note that it is the kth largest
#  element in the sorted order, not the kth distinct element.
class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.heap=nums
        heapq.heapify(nums)
        while len(self.heap)>k:
            heapq.heappop(self.heap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        while len(self.heap)>self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

class Solution:

    # 1046. Last Stone Weight     https://leetcode.com/problems/last-stone-weight/
    # Return the weight of the last remaining stone. 
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-n for n in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            a=heapq.heappop(stones)
            b=heapq.heappop(stones)
            heapq.heappush(stones,-abs(a-b)) if abs(a-b) else None
            
        return -stones[0] if stones  else 0
        
    # 973. K Closest Points to Origin     https://leetcode.com/problems/k-closest-points-to-origin/description/
    # return the k closest points to the origin (0, 0).
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance=[(x**2+y**2,x,y) for x, y in points]
        heapq.heapify(distance)
        kSmalest=heapq.nsmallest(k,distance)

        return [[x,y] for _,x,y in kSmalest]
        # distanceCoordinates={}
        # distances=[]

        # for p in points:
        #     x=p[0]
        #     y=p[1]
        #     distance=math.sqrt(x**2 + y**2)
        #     if distance not in distanceCoordinates:
        #         distanceCoordinates[distance]=[]
        #     distanceCoordinates[distance].append(p)
        #     distances.append(distance)

        # heapq.heapify(distances)
        # res=[]
        # for i in range(k):
        #     distance=heapq.heappop(distances)
        #     res.append(distanceCoordinates[distance].pop())
        # return res 


    # 215. Kth Largest Element in an Array    https://leetcode.com/problems/kth-largest-element-in-an-array/description/
    # Given an integer array nums and an integer k, return the kth largest element in the array.
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums)>k: 
            heapq.heappop(nums)      
        return nums[0]
    
    # 621. Task Scheduler     https://leetcode.com/problems/task-scheduler/description/
    # ​Return the minimum number of intervals required to complete all tasks.
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter={}
        for t in tasks:
            if t not in counter:
                counter[t]=0
            counter[t]+=1

        nextTask=[-value for value in counter.values()]
        heapq.heapify(nextTask)
        que=deque()
        time=0
  
        while nextTask or que:
            if que and time>que[0][0]:
                quePop=que.popleft()
                heapq.heappush(nextTask,quePop[1]) if quePop[1] else None
            if nextTask:
                task=heapq.heappop(nextTask)+1
                que.append((time+n,task)) if task else None
            time+=1
            
        return time
    
# 295. Find Median from Data Stream  https://leetcode.com/problems/find-median-from-data-stream/description/
# Implement the MedianFinder class:
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 
# of the actual answer will be accepted.
class MedianFinder:

    def __init__(self):
        self.smallNums=[]
        self.bigNums=[]
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallNums, -num)

        if self.smallNums and self.bigNums and -self.smallNums[0]>self.bigNums[0]:
            big=-heapq.heappop(self.smallNums)
            heapq.heappush(self.bigNums,big)

        if len(self.smallNums)>len(self.bigNums)+1:
            bigSmall=-heapq.heappop(self.smallNums)
            heapq.heappush(self.bigNums,bigSmall)
        
        if len(self.bigNums)>len(self.smallNums)+1:
            smallBig=-heapq.heappop(self.bigNums)
            heapq.heappush(self.smallNums,smallBig)
        
 
    def findMedian(self) -> float:
        if len(self.smallNums)==len(self.bigNums):
            return (-self.smallNums[0]+self.bigNums[0])/2
        else:
            if len(self.smallNums)>len(self.bigNums):
                return -self.smallNums[0]
            else:
                return self.bigNums[0]

        

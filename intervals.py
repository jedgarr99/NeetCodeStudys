import heapq
from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    
    # 57. Insert Interval     https://leetcode.com/problems/insert-interval/description/
    # nsert newInterval into intervals such that intervals is still sorted in ascending order 
    # by starti and intervals still does not have any overlapping intervals
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        for i in range(len(intervals)):
            if newInterval[1]<intervals[i][0]:
                res.append(newInterval)
                return res+intervals[i:]
            elif intervals[i][1]<newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval=[min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
        res.append(newInterval)
        return res
    
    # 56. Merge Intervals     https://leetcode.com/problems/merge-intervals/description/
    # merge all overlapping intervals,
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        curr=intervals[0]
        res=[]

        for i in intervals:
            if curr[1]<i[0]:
                res.append(curr)
                curr=i
            else:
                curr=[curr[0],max(curr[1],i[1])]
        res.append(curr)
        return res
    
    # 435. Non-overlapping Intervals      https://leetcode.com/problems/non-overlapping-intervals/description/
    # return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res=0
        intervals.sort()
        prevEnd=intervals[0][1]

        for start,end in intervals[1:]:
            if prevEnd>start:
                prevEnd=min(prevEnd,end)
                res+=1
            else:
                prevEnd=end
        return res
    
    # Meeting Schedule        https://neetcode.io/problems/meeting-schedule
    # determine if a person could add all meetings to their schedule without any conflicts.
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not len(intervals):return True

        intervals.sort(key=lambda x:x.start)
        prevEnd=intervals[0].end
        
        for iv in intervals[1:]:
            if iv.start < prevEnd:
                return False
            else:
                prevEnd=iv.end
        return True
    
    # Meeting Schedule II     https://neetcode.io/problems/meeting-schedule-ii
    # find the minimum number of days required to schedule all meetings without any conflicts.
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not len(intervals): return 0
        
        intervals.sort(key=lambda x: x.start)
        remainingIntervals=[]
        days=0

        while intervals:
            prevEnd=intervals[0].end
            for iv in intervals[1:]:
                if iv.start<prevEnd:
                    remainingIntervals.append(iv)
                else:
                    prevEnd=iv.end

            days+=1
            intervals=remainingIntervals
            remainingIntervals=[]
        return days
    
    def minMeetingRoomsAlternative(self, intervals: List[Interval]) -> int:
        start=[i.start for i in intervals]
        end=[i.end for i in intervals]
        start.sort()
        end.sort()
        s,e,days,maxDays=0,0,0,0

        while s<len(intervals):
            if end[e]<=start[s]:
                days-=1
                e+=1
            else:
                days+=1
                s+=1
                maxDays=max(maxDays,days)
        return maxDays
    

    # 1851. Minimum Interval to Include Each Query        https://leetcode.com/problems/minimum-interval-to-include-each-query/
    # The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        dp={}
        minHeap=[]
        i=0

        for q in sorted(queries):
            if q not in dp:
                while i<len(intervals) and intervals[i][0] <= q:
                    l,r=intervals[i][0],intervals[i][1]
                    heapq.heappush(minHeap,(r-l+1,r))
                    i+=1
                while minHeap and minHeap[0][1]<q:
                    heapq.heappop(minHeap)
                dp[q]=minHeap[0][0] if minHeap else -1

        return [dp[q] for q in queries]

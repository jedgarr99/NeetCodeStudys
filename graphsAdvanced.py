
from collections import deque
import heapq
import math
from typing import List


class Solution:

    # 332. Reconstruct Itinerary      https://leetcode.com/problems/reconstruct-itinerary/description/
    # return the itinerary that has the smallest lexical order when read as a single string.
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        flightMap={src:[] for src,_ in tickets}
        tickets.sort()
        for src,dst in tickets:
            flightMap[src].append(dst)
        
        res=['JFK']
        def dfs(currAirport):
            if  len(res) ==len(tickets)+1 :
                return True
            
            if currAirport not in flightMap :      
                return False

            temp=list(flightMap[currAirport])
            for i,airport in enumerate(temp):
                flightMap[currAirport].pop(i)
                res.append(airport)
                
                if dfs(airport): return True
              
                flightMap[currAirport].insert(i,airport)
                res.pop()
            return False

        dfs('JFK')
        return res
    
    # Min Cost to Connect All Points      https://leetcode.com/problems/min-cost-to-connect-all-points/description/
    # Return the minimum cost to make all points connected. 
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        distance={i:[] for i in range(len(points))} #[cost,node]
        for i in range(len(points)):
            x1,y1=points[i]
            for j in range(i+1,len(points)):
                x2,y2=points[j]
                dis=abs(x1-x2)+abs(y1-y2)
                distance[i].append([dis,j])
                distance[j].append([dis,i])
        # print(distance)

        #Prims algorithmn
        minHeap=[[0,0]]
        res=0
        visited=set()

        while len(visited)<len(points):
            cost,node=heapq.heappop(minHeap)
            if node in visited:
                continue
            res+=cost
            visited.add(node)
            for nextCost,nextNode in distance[node]:
                if nextNode not in visited:
                    heapq.heappush(minHeap,[nextCost,nextNode])
        return res
    # Network Delay Time      https://leetcode.com/problems/network-delay-time/
    #  Return the minimum time it takes for all the n nodes to receive the signal.
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj={i:[] for i in range(1,n+1)}

        for u,v,w in times:
            adj[u].append((w,v))

        minHeap=[(0,k)]
        visited=set()
        maxTime=0

        while minHeap and len(visited)!= n:
            time, node=heapq.heappop(minHeap)
            if node in visited:
                continue

            visited.add(node)
            maxTime=max(time,maxTime)

            for nextTime,nextNode in adj[node]:
                if nextNode not in visited:
                    heapq.heappush(minHeap,(time+nextTime,nextNode))
                    
        return maxTime if len(visited)== n else -1



        
    
    # Swim in Rising Water        https://leetcode.com/problems/swim-in-rising-water/description/
    # Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start 
    # at the top left square (0, 0).
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap=[(grid[0][0],0,0)] #(height(cost),r,c)
        res=0
        visited=set()#(r,c)
        ROWS,COLS=len(grid),len(grid[0])

        def addNext(r,c):
            directions=[(1,0),(-1,0),(0,1),(0,-1)]
            for dr,dc in directions:
                newR,newC=r+dr,c+dc
                if (newR>=0 and newR<ROWS and newC>=0 
                    and newC<COLS and (newR,newC) not in visited):
                    visited.add((newR,newC))
                    heapq.heappush(minHeap,(grid[newR][newC],newR,newC))

        currR,currC=0,0
        visited.add((0,0))
        resTime=0
        while currR!=ROWS-1 or currC!=COLS-1:
            time,currR,currC=heapq.heappop(minHeap)
            resTime=max(resTime,time)
            #print((currR,currC,resTime))
            addNext(currR,currC)
        return resTime
    
    # Foreign Dictionary      https://neetcode.io/problems/foreign-dictionary
    # Derive the order of letters in this language.
    def foreignDictionary(self, words: List[str]) -> str:
        adj={c:set() for w in words for c in w}

        for i in range(len(words)-1):
            word1,word2=words[i],words[i+1]
            minLen=min(len(word1),len(word2))
            if word1[:minLen]== word2[:minLen] and len(word1)>len(word2):
                return ""
            for j in range(minLen):
                if word1[j]!=word2[j]:
                    adj[word1[j]].add(word2[j])
                    break

        res=deque()
        visit,cycle=set(),set()

        def dfs(letter):
            if letter in cycle:
                return False
            if letter in visit:
                return True

            cycle.add(letter)
            for nextLetter in adj[letter]:
                if not dfs(nextLetter):
                    return False

            cycle.remove(letter)
            visit.add(letter)
            res.appendleft(letter)

            return True

        for letter in adj.keys():
            if not dfs(letter):
                return ""
                
        return ''.join(res)
    
    # 787. Cheapest Flights Within K Stops        https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
    # return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices=[math.inf]*n
        prices[src]=0

        for _ in range(k+1):
            auxPrices=prices.copy()
            for s,d,p in flights:
                if prices[s]!=math.inf:
                    auxPrices[d]=min(auxPrices[d],prices[s]+p)
            prices=auxPrices

        return prices[dst] if prices[dst] != math.inf else -1
                    
     

import collections
from typing import List, Optional

class Node():
    def __init__(self,val=0):
        self.val=val
        self.neighbors=[]

    def addNeighbor(self,node):
        self.neighbors.append(node)


class Solution():

    # 200. Number of Islands          https://leetcode.com/problems/number-of-islands/description/
    # Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid)<=0 and len(grid[0])<=0:
            return 0
        
        total=0
        visited=set()
        
        def searchIsland(i,j):
            if i>=0 and i<len(grid) and j>=0 and j<len(grid[0]) and (i,j) not in visited and grid[i][j]=='1':
                visited.add((i,j))
                searchIsland(i+1,j)
                searchIsland(i-1,j)
                searchIsland(i,j+1)
                searchIsland(i,j-1)

        
        #row
        for i in range(len(grid)):
            #column
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j]=='1':
                    total+=1
                    searchIsland(i,j)
                    
        return total
    
    # 695. Max Area of Island
    # Return the maximum area of an island in grid.
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid)<=0 and len(grid[0])<=0:
            return 0
        rows=len(grid)
        cols=len(grid[0])
        
        total=0
        maxArea=0
        visited=set()
        area=[0]
        
        def searchIsland(i,j):
            if i>=0 and i<rows and j>=0 and j<cols and (i,j) not in visited and grid[i][j]==1:
                print(i,' ',j)
                area[0]+=1
                visited.add((i,j))
                searchIsland(i+1,j)
                searchIsland(i-1,j)
                searchIsland(i,j+1)
                searchIsland(i,j-1)

        
        #row
        for i in range(rows):
            #column
            for j in range(cols):
                if (i,j) not in visited and grid[i][j]==1:
                    
                    print('Empezando busqueda en ',i,' ',j)
                    searchIsland(i,j)
                    maxArea=max(maxArea,area[0])
                    print('Max area', maxArea)
                    area[0]=0
                    
        return maxArea
    
    # 133. Clone Graph            https://leetcode.com/problems/clone-graph/description/
    # Return a deep copy (clone) of the graph.
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew={}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy=Node(node.val)
            oldToNew[node]=copy

            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        return dfs(node) if node else None
    
    # Islands and Treasure            https://neetcode.io/problems/islands-and-treasure   
    # Fill each land cell with the distance to its nearest treasure chest
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        que=collections.deque()
        ROWS,COLS=len(grid),len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    que.append((r,c,0))
        
        def bfs():

            while que:
                r,c,distance=que.popleft()
                directions=((1,0),(-1,0),(0,1),(0,-1))
                newDistance=distance+1
                for dr,dc in directions:
                    row,col=r+dr,c+dc
                    if (row>=0 and row<ROWS and
                    col>=0 and col<COLS and
                    grid[row][col]>=0 and grid[row][col]>newDistance):
                       grid[row][col]=newDistance
                       que.append((row,col,newDistance))
        bfs()

    # 994. Rotting Oranges            https://leetcode.com/problems/rotting-oranges/description/
    # Return the minimum number of minutes that must elapse until no cell has a fresh orange.
    #puedo modificar mi arreglo "descomponiendo" las naranjas y asi no tengo que guardar visited
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])

        que=collections.deque()
        visited=set()
        toVisit=[0]
        apples=0
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==2:
                    que.append([i,j])
                    visited.add((i,j))
                    apples+=1
                if grid[i][j]==1:
                    apples+=1
                    toVisit[0]+=1
                    print('agregando naranja ',i,' ',j)
                    print('+++++++',toVisit[0])
                    
        minutes=0
        def addOrange(r,c):
            if r>=0 and r<ROWS and c>=0 and c<COLS and (r,c) not in visited and grid[r][c]!=0:
                toVisit[0]-=1
                print('quitando naranja ',r,' ',c)
                print('------',toVisit[0])
                visited.add((r,c))
                que.append([r,c])

        while que:     

            for i in range(len(que)):
                r,c=que.popleft()
                addOrange(r+1,c) 
                addOrange(r-1,c)
                addOrange(r,c+1)
                addOrange(r,c-1)

            minutes+=1
            print('Aumnetando tiempo a ',minutes)
        if apples==0:
            minutes+=1

        return minutes-1 if toVisit[0]==0 else -1


    # 417. Pacific Atlantic Water Flow            https://leetcode.com/problems/pacific-atlantic-water-flow/description/
    # Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) 
    # to both the Pacific and Atlantic oceans.
    #you can use just two fors, calling for each ocean
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific=set()
        atlantic=set()
        ROWS,COLS=len(heights),len(heights[0])

        def dfs(r,c,prev,ocean):
            if r>=0 and r<ROWS and c>=0 and c<COLS and heights[r][c]>=prev and (r,c) not in visited:
                print('Adding ', r,' ',c)
                visited.add((r,c))
                ocean.add((r,c))
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                newHeight=heights[r][c]

                for dr,dc in directions:
                    dfs(r+dr,c+dc,newHeight,ocean)
        print('PACIFIC')
        visited=set()
        for i in range(ROWS):
            if (i,0) not in visited:
                dfs(i,0,heights[i][0],pacific)
        for j in range(COLS):
            if (0,j) not in visited:
                dfs(0,j,heights[0][j],pacific)
        print('ATLANTIC')
        visited=set()
        for i in range(ROWS):
            if (i,COLS-1) not in visited:
                dfs(i,COLS-1,heights[i][COLS-1],atlantic)
        for j in range(COLS):
            if (ROWS-1,j) not in visited:
                dfs(ROWS-1,j,heights[ROWS-1][j],atlantic)

        return pacific.intersection(atlantic)
    
    # 130. Surrounded Regions         https://leetcode.com/problems/surrounded-regions/description/
    # capture all regions that are 4-directionally surrounded by 'X'.
    #puedo no usar set, puedo cambar las Os por valores temporales "T"
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS=len(board),len(board[0])
        visited=set()

        def dfs(r,c):
            if r>=0 and r<ROWS and c>=0 and c<COLS and board[r][c]=="O" and (r,c) not in visited:
                visited.add((r,c))
                print('FOUND ',r,' ',c)
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    dfs(r+dr,c+dc)

        for i in range(ROWS):
            if board[i][0]=="O":
                print('a')
                dfs(i,0)
            if board[i][COLS-1]=="O":
                print('b')
                dfs(i,COLS-1)
        for j in range(1,COLS):
            if board[0][j]=="O":
                print('c')
                dfs(0,j)
            if board[ROWS-1][j]=="O":
                print('d')
                dfs(ROWS-1,j)
        print(visited)
        for i in range(1,ROWS):
            for j in range(1,COLS):
                if board[i][j]=="O" and (i,j) not in visited:
                    board[i][j]="X"


    # 207. Course Schedule            https://leetcode.com/problems/course-schedule/description/
    # Return true if you can finish all courses. Otherwise, return false.
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courses=[[] for _ in range(numCourses)]
        for nextCourse, index in prerequisites:
            courses[index].append(nextCourse)
        print(courses)

        visited=set()

        def dfs(index):
            print('Checando curso ',index)
            if index in visited:
                return False
            if courses[index]==[]:
                return True
            visited.add(index)
            for c in courses[index]:
                if not dfs(c,visited):
                    return False
            courses[index]=[]
            visited.remove(index)
            return True

        for i in range(len(courses)):
            if not dfs(i):
                return False       

        return True
    
    # 210. Course Schedule II             https://leetcode.com/problems/course-schedule-ii/description/
    # Return the ordering of courses you should take to finish all courses.
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses=[[] for _ in range(numCourses)]
        for nextCourse, index in prerequisites:
            courses[index].append(nextCourse)

    # Count Connected Components      https://neetcode.io/problems/count-connected-components
    # Return the total number of connected components in that graph.
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par=[i for i in range(n)]
        rank=[1]*n

        def findPar(node):
            nextPar=par[node]
            while nextPar != par[nextPar]:
                par[nextPar]=par[par[nextPar]]
                nextPar=par[nextPar]
            return nextPar

        def union(node1,node2):
            par1,par2=findPar(node1),findPar(node2)
            if par1==par2:
                return 0
            rank1,rank2=rank[node1],rank[node2]
            if rank1>rank2:
                par[par2]=par1
                rank[par1]+=rank[par2]
            else:
                par[par1]=par2
                rank[par2]+=rank[par1]
            return 1
        res=n
        for node1, node2 in edges:
            res-=union(node1,node2)
        return res

            
    # 684. Redundant Connection      https://leetcode.com/problems/redundant-connection/
    # Return an edge that can be removed so that the resulting graph is a tree of n nodes. 
    # If there are multiple answers, return the answer that occurs last in the input.
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par=[i for i in range(len(edges))]
        rank=[1]*len(edges)

        def findPar(node):
            nextPar=par[node]
            while nextPar != par[nextPar]:
                par[nextPar]=par[par[nextPar]]
                nextPar=par[nextPar]
            return nextPar

        def union(node1,node2):
            par1,par2=findPar(node1),findPar(node2)
            if par1==par2:
                return 0
            rank1,rank2=rank[node1],rank[node2]
            if rank1>rank2:
                par[par2]=par1
                rank[par1]+=rank[par2]
            else:
                par[par1]=par2
                rank[par2]+=rank[par1]
            return 1
        res=[-1,-1]
        for node1, node2 in edges:
            if not union(node1-1,node2-1):
                res=[node1,node2]
        return res

if __name__=="__main__":
    mySolution=Solution()
    print(mySolution.maxAreaOfIsland(grid =[[1]]))
    help(dict)




class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n =len(heights),len(heights[0])

        def search(nums:List[Tuple[int,int]])->Set[Tuple[int,int]]:
            def dfs(i:int,j:int)->None:
                if (i,j) in vis:
                    return
                vis.add((i,j))
                for x,y in (i,j-1),(i, j + 1), (i - 1, j), (i + 1, j):  
                    if 0 <= x < m and 0 <= y < n and heights[x][y] >= heights[i][j]:  # 往高处走
                        dfs(x, y)
            vis=set()
            for i,j in nums:
                dfs(i,j)
            return vis
            
        pacific = [(0, j) for j in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m - 1, j) for j in range(n)] + [(i, n - 1) for i in range(m - 1)]
        return list(search(pacific) & search(atlantic))  # 交集即为答案

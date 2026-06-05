class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n,m =len(image),len(image[0])
        cur_color = image[sr][sc]
        if cur_color == color:
            return image
        q =deque([(sr,sc)])
        image[sr][sc] =color
        while q:
            i,j =q.popleft()
            for x,y in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
                if 0<=x<n and 0<=y<m and image[x][y] ==cur_color:
                    image[x][y] =color
                    q.append((x,y))
        return image

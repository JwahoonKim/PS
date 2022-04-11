from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        startColor = image[sr][sc]
        
        if image[sr][sc] == newColor:
            return image
        
        def dfs(x, y):
            image[x][y] = newColor
            dx = [0,0,1,-1]
            dy = [1,-1,0,0]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(image) and 0 <= ny < len(image[0]):
                    if image[nx][ny] == startColor:
                        dfs(nx, ny)
                        
        dfs(sr, sc)
        
        # q = deque()
        # q.append((sr, sc))
        # while(q):
        #     x, y = q.popleft()
        #     if image[x][y] == startColor:
        #         image[x][y] = newColor
        #         dx = [0,0,1,-1]
        #         dy = [1,-1,0,0]
        #         for i in range(4):
        #             nx = x + dx[i]
        #             ny = y + dy[i]
        #             if 0 <= nx < len(image) and 0 <= ny < len(image[0]):
        #                 if image[nx][ny] == startColor:
        #                     q.append((nx, ny))
        return image
        
    
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        rows,cols = len(image),len(image[0])
        original_color = image[sr][sc]

        if original_color == color:
            return image
        
        visited = [[False]*cols for _ in range(rows)]
        visited[sr][sc] = True
        image[sr][sc] = color

        queue = deque([sr,sc])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if not visited[nr][nc] and image[nr][nc] == original_color:
                        visited[nr][nc] = True
                        image[nr][nc] = color
                        queue.append((nr, nc))
        return image


        

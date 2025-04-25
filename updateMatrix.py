from collections import deque

class Solution(object):

    def updateMatrix(self, mat):
        if not mat or not mat[0]:
            return mat

        rows, cols = len(mat), len(mat[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            curr_r, curr_c = queue.popleft()
            for dr, dc in directions:
                new_r, new_c = curr_r + dr, curr_c + dc

                if (0 <= new_r < rows and
                    0 <= new_c < cols and
                    dist[new_r][new_c] > dist[curr_r][curr_c] + 1):

                    dist[new_r][new_c] = dist[curr_r][curr_c] + 1
                    queue.append((new_r, new_c))

        return dist

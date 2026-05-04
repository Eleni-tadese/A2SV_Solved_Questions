class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j: continue
                xi, yi, ri = bombs[i]
                xj, yj, rj = bombs[j]
                
             
                distance_sq = (xi - xj)**2 + (yi - yj)**2
                if distance_sq <= ri**2:
                    adj[i].append(j)
        
        def dfs(node, visited):
            visited.add(node)
            count = 1
            for neighbor in adj[node]:
                if neighbor not in visited:
                    count += dfs(neighbor, visited)
            return count
        
      
        max_bombs = 0
        for i in range(n):
            max_bombs = max(max_bombs, dfs(i, set()))
            
        return max_bombs
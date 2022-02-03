class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        
        ''' BFS '''
        paths, path =[], [0]
        queue=deque([path])
        if not graph:
            return paths
        
        while queue:
            cur_path = queue.popleft()
            node=cur_path[-1]
            
            for neighbour in graph[node]:
                temp_path=cur_path[:]
                temp_path.append(neighbour)
                
                if neighbour == len(graph)-1:
                    paths.append(temp_path)
                else:
                    queue.append(temp_path)
        return paths
    
    
    
    
        '''DFS'''
        def dfs(node):
            path.append(node)
            if node==len(graph)-1:
                paths.append(path[:])
                return
            
            for next_node in graph[node]:
                dfs(next_node)
                path.pop()
            
        paths, path =[], []
        dfs(0)
        return paths
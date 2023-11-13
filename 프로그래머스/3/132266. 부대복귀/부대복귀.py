from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    graph = {i:list() for i in range(1, n+1)}
    visited = [False for _ in range(n+1)]
    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)
        
    dijk = [0] + [float("inf") for _ in range(n)]
    dijk[destination] = 0
    
    queue = deque([destination])
    
    while queue:
        node = queue.popleft()
        visited[node] = True
        
        for next_node in graph[node]:
            if not visited[next_node]:
                queue.append(next_node)
            if dijk[node] + 1 < dijk[next_node]:
                dijk[next_node] = dijk[node] + 1
    
    
    for source in sources:
        if dijk[source] == float("inf"):
            answer.append(-1)
        else:
            answer.append(dijk[source])
    return answer
graph={
    'A':["B","C","D"],
    'B':["E","F"],
    "C":["G":"H"],
    "D":["H"],
    "E":[],
    "F":[],
    "G":[],
    "H":[]
}

def bfs(visit,graph,node):
    visit.append(node)
    queue=[]
    queue.append(node)
    while queue:
        s=queue.pop(0)
        print(s)
        for next in graph[s]:
            if next not in visit:
                visit.append(next)
                queue.append(next)
bfs([],graph,"A")
    

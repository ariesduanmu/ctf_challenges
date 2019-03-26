# Fucking kill me

class Team(object):
    def __init__(self, names):
        self.names = names

    def __bool__(self):
        
        return self.isConnect()
    
    def name_graph(self):
        from collections import defaultdict
        n = len(self.names)
        f = [n[0].lower() for n in self.names]
        l = [n[-1].lower() for n in self.names]
        
        f_graph = defaultdict(list)
        l_graph = defaultdict(list)
        
        for i in range(n):
            f_graph[f[i]].append(i)
            l_graph[l[i]].append(i)
        
        graph_in = defaultdict(list)
        graph_out = defaultdict(list)
        
        for i in range(n):
            graph_in[i] = f_graph[l[i]]
            graph_out[i] = l_graph[f[i]]
            
        return f_graph, l_graph, graph_in, graph_out, set(f+l)
    
    def BFS(self, graph_in, graph_out, node):
        queue = [node]
        visited = [False] * len(self.names)
        visited[node] = True
        while queue:
            s = queue.pop(0)
            nodes = graph_in[s]+graph_out[s]
            for n in nodes:
                if visited[n] is False:
                    queue.append(n)
                    visited[n] = True
        return all(visited)
                
    def isConnect(self):
        f_graph, l_graph, graph_in, graph_out, keys = self.name_graph()
        start_point = 0
        end_point = 0
        for i in list(keys):
            if abs(len(f_graph[i])-len(l_graph[i]))>1:
                return False
            if len(f_graph[i])>len(l_graph[i]):
                start_point += 1
            if len(f_graph[i])<len(l_graph[i]):
                end_point += 1
            
            if start_point > 1 or end_point > 1:
                return False
        
        return self.BFS(graph_in, graph_out, 0)
            

def isCoolTeam(team):
    return bool(Team(team))

from SAL.Graph import Graph
def closeness_centrality(G):
    nodes = G.nodes()
    closeness_dict = {}
    for n in nodes:
        sp = single_source_shortest_path_length(G, n)
        totsp = sum(sp.values())
        len_G = len(G)
        _closeness_centrality = 0.0
        if totsp > 0.0 and len_G > 1:
            _closeness_centrality = (len(sp) - 1.0) / totsp
            # normalize to number of nodes-1 in connected part         
        closeness_dict[n] = _closeness_centrality
   
    return closeness_dict


def single_source_shortest_path_length(G, source):
    if source not in G:
        raise Exception(f"Source {source} is not in G")
    cutoff = float("inf")
    nextlevel = {source: 1}
    return dict(_single_shortest_path_length(G.adj(), nextlevel, cutoff))

def _single_shortest_path_length(adj, firstlevel, cutoff):
    seen = {}  # level (number of hops) when seen in BFS
    level = 0  # the current level
    nextlevel = set(firstlevel)  # set of nodes to check at next level
    n = len(adj)
    while nextlevel and cutoff >= level:
        thislevel = nextlevel  # advance to next level
        nextlevel = set()  # and start a new set (fringe)
        found = []
        for v in thislevel:
            if v not in seen:
                seen[v] = level  # set the level of vertex v
                found.append(v)
                yield (v, level)
        if len(seen) == n:
            return
        for v in found:
            nextlevel.update(adj[v])
        level += 1
    del seen
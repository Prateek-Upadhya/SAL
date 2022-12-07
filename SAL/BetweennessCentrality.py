from collections import deque

def betweenness_centrality(G):
    betweenness = dict.fromkeys(G, 0.0)
    nodes = G
    for s in nodes:
        S, P, sigma, _ = bfs_for_path(G, s)
        betweenness, _ = get_betweenness(betweenness, S, P, sigma, s)
    betweenness = _rescale(
        betweenness,
        directed = False
    )
    return betweenness


def bfs_for_path(G, s):
    S = []
    P = {}
    for v in G:
        P[v] = []
    sigma = dict.fromkeys(G, 0.0)
    D = {}
    sigma[s] = 1.0
    D[s] = 0
    Q = deque([s])
    while Q:
        v = Q.popleft()
        S.append(v)
        Dv = D[v]
        sigmav = sigma[v]
        for w in G[v]:
            if w not in D:
                Q.append(w)
                D[w] = Dv + 1
            if D[w] == Dv + 1:
                sigma[w] += sigmav
                P[w].append(v)
    return S, P, sigma, D


def get_betweenness(betweenness, S, P, sigma, s):
    delta = dict.fromkeys(S, 0)
    while S:
        w = S.pop()
        coeff = (1 + delta[w]) / sigma[w]
        for v in P[w]:
            delta[v] += sigma[v] * coeff
        if w != s:
            betweenness[w] += delta[w]
    return betweenness, delta


def _rescale(betweenness, directed=False):
    if not directed:
        scale = 0.5
    else:
        scale = None
    if scale is not None:
        for v in betweenness:
            betweenness[v] *= scale
    return betweenness

import math

def eigenvector_centrality(G, max_iter=100, tol=1.0e-6, nstart=None, weight=None):
    if nstart is None:
        nstart = {v: 1 for v in G}

    nstart_sum = sum(nstart.values())
    x = {k: v / nstart_sum for k, v in nstart.items()}
    nnodes = G.number_of_nodes()

    for _ in range(max_iter):
        xlast = x
        x = xlast.copy() 
        for n in x:
            for nbr in G[n]:
                w = G[n][nbr].get(weight, 1) if weight else 1
                x[nbr] += xlast[n] * w

        norm = math.hypot(*x.values()) or 1
        x = {k: v / norm for k, v in x.items()}
        if sum(abs(x[n] - xlast[n]) for n in x) < nnodes * tol:
            return x
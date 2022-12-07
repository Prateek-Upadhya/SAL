from SAL.BetweennessCentrality import betweenness_centrality
from SAL.DegreeCentrality import degree_centrality


def call_algorithm(G, k, method):
    if method == "betweenness":
        betweenness = sorted(betweenness_centrality(G).items(), key=lambda x: x[1], reverse=True)[0:k]
        
        dictionary = {}
        betw_dict = Convert(betweenness, dictionary)
        
        return betw_dict

    
    elif method == "degree_centrality":
        centrality = sorted(degree_centrality(G).items(), key=lambda x: x[1], reverse=True)[0:k]
        
        dictionary = {}
        centrality_dict = Convert(centrality, dictionary) 

        return centrality_dict
    else:
        return "This method is not supported."
    
def Convert(tup, di):
    di = dict(tup)
    return di
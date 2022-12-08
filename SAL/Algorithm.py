from SAL.BetweennessCentrality import betweenness_centrality
from SAL.DegreeCentrality import degree_centrality
from SAL.EigenvectorCentrality import eigenvector_centrality
from SAL.ClosenessCentrality import closeness_centrality
from SAL.KernighanLinBisection import kernighan_lin_bisection

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

    elif method == "eigenvector_centrality":
        centrality = sorted(eigenvector_centrality(G).items(), key=lambda x: x[1], reverse=True)[0:k]
        
        dictionary = {}
        eigenvector_dict = Convert(centrality, dictionary) 

        return eigenvector_dict
    
    elif method == "closeness_centrality":
        centrality = sorted(closeness_centrality(G).items(), key=lambda x: x[1], reverse=True)[0:k]
        dictionary = {}
        closeness_dict = Convert(centrality, dictionary) 
        return closeness_dict
    
    elif method =="kernighan_lin_bisection":
        get_partition = kernighan_lin_bisection(G)
        dictionary = {"subset_1":list(get_partition[0])[0:k], "subset_2":list(get_partition[1])[0:k]}
        return dictionary
        
    else:
        return "This method is not supported."
    
def Convert(tup, di):
    di = dict(tup)
    return di
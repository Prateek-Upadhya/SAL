import sys
import pandas as pd
from SAL.ConvertToGraph import convert_from_pandasDF_to_graph
from SAL.Algorithm import call_algorithm


def get_top_K_nodes(DATASET_PATH, K, METHOD):
    relations = pd.read_csv(DATASET_PATH, sep=' ')
    G = convert_from_pandasDF_to_graph(relations, source='source', target='target')
    
  
    res = call_algorithm(G, K, METHOD)
    
    if(type(res) == str):
        print(res)
    else:
        userIds = list(res.keys())
        vals = list(res.values())
    
    
    if METHOD == "degree_centrality": 
        for i in range(K):
            print(f"User ID : {str(userIds[i]):9s}, Degree Centrality value: {vals[i]:.3f}") 
    
    elif METHOD == "betweenness":
        for i in range(K):
            print(f"User ID : {str(userIds[i]):9s}, Betweenness value: {vals[i]:.3f}")
            
    elif METHOD == "eigenvector_centrality":
        for i in range(K):
            print(f"User ID : {str(userIds[i]):9s}, Eigenvector Centrality value: {vals[i]:.3f}")
            
    elif METHOD == "closeness_centrality":
        for i in range(K):
            print(f"User ID : {str(userIds[i]):9s}, Closeness Centrality value: {vals[i]:.3f}")



def example():
    if len(sys.argv) == 4:
        DATASET_PATH = sys.argv[1]
        K = int(sys.argv[2])
        METHOD = sys.argv[3]

        get_top_K_nodes(DATASET_PATH, K, METHOD)
    else:
        print("Enter valid number of arguments.")


if __name__ == '__main__':
    example()
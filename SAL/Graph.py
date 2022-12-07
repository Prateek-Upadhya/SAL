from SAL.Neighbour import Neighbour
from SAL.Degree import Degree


class Graph:
    node_dict = dict
    node_attr_dict = dict
    adjlist_outer_dict = dict
    adjlist_inner_dict = dict
    edge_attr_dict = dict
    graph_attr_dict = dict

    def __init__(self, incoming_graph_data=None, **attr):
        self.graph_attr_dict = self.graph_attr_dict
        self.node_dict = self.node_dict
        self.node_attr_dict = self.node_attr_dict
        self.adjlist_outer_dict = self.adjlist_outer_dict
        self.adjlist_inner_dict = self.adjlist_inner_dict
        self.edge_attr_dict = self.edge_attr_dict

        self.graph = self.graph_attr_dict()  # dictionary for graph attributes
        self._node = self.node_dict()  # empty node attribute dict
        self._adj = self.adjlist_outer_dict()  # empty adjacency dict
        self.graph.update(attr)

    def adj(self):
        return Neighbour(self._adj)

    def __iter__(self):
        return iter(self._node)

    def __len__(self):
        return len(self._node)

    def __getitem__(self, n):
        return self._adj[n]

    def add_node(self, node_for_adding, **attr):
        if node_for_adding not in self._node:
            self._adj[node_for_adding] = self.adjlist_inner_dict()
            attr_dict = self._node[node_for_adding] = self.node_attr_dict()
            attr_dict.update(attr)
        else:  # update attr even if node already exists
            self._node[node_for_adding].update(attr)

    def add_nodes_from(self, nodes_for_adding, **attr):
        for n in nodes_for_adding:
            try:
                newnode = n not in self._node
                newdict = attr
            except TypeError:
                n, ndict = n
                newnode = n not in self._node
                newdict = attr.copy()
                newdict.update(ndict)
            if newnode:
                self._adj[n] = self.adjlist_inner_dict()
                self._node[n] = self.node_attr_dict()
            self._node[n].update(newdict)

    def add_edge(self, u_of_edge, v_of_edge, **attr):
        u, v = u_of_edge, v_of_edge
        # add nodes
        if u not in self._node:
            self._adj[u] = self.adjlist_inner_dict()
            self._node[u] = self.node_attr_dict()
        if v not in self._node:
            self._adj[v] = self.adjlist_inner_dict()
            self._node[v] = self.node_attr_dict()
        # add the edge
        datadict = self._adj[u].get(v, self.edge_attr_dict())
        datadict.update(attr)
        self._adj[u][v] = datadict
        self._adj[v][u] = datadict

    def add_edges_from(self, ebunch_to_add, **attr):
        for e in ebunch_to_add:
            ne = len(e)
            if ne == 3:
                u, v, dd = e
            elif ne == 2:
                u, v = e
                dd = {}  # doesn't need edge_attr_dict
            if u not in self._node:
                self._adj[u] = self.adjlist_inner_dict()
                self._node[u] = self.node_attr_dict()
            if v not in self._node:
                self._adj[v] = self.adjlist_inner_dict()
                self._node[v] = self.node_attr_dict()
            datadict = self._adj[u].get(v, self.edge_attr_dict())
            datadict.update(attr)
            datadict.update(dd)
            self._adj[u][v] = datadict
            self._adj[v][u] = datadict

    def update(self, edges=None, nodes=None):
        if edges is not None:
            if nodes is not None:
                self.add_nodes_from(nodes)
                self.add_edges_from(edges)
            else:
                # check if edges is a Graph object
                try:
                    graph_nodes = edges.nodes
                    graph_edges = edges.edges
                except AttributeError:
                    # edge not Graph-like
                    self.add_edges_from(edges)
                else:  # edges is Graph-like
                    self.add_nodes_from(graph_nodes.data())
                    self.add_edges_from(graph_edges.data())
                    self.graph.update(edges.graph)
        elif nodes is not None:
            self.add_nodes_from(nodes)

    def degree(self):
        return Degree(self)

    def adjacency(self):
        return iter(self._adj.items())
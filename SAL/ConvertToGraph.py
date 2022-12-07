from SAL.Graph import Graph


def convert_from_pandasDF_to_graph(
    df,
    source="source",
    target="target"
):
    g = Graph()
    g.add_edges_from(zip(df[source], df[target]))
    return g
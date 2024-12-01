from rdflib import Graph
import networkx as nx
import matplotlib.pyplot as plt

# Đọc tệp RDF
rdf_file = "/home/dream-base/Documents/Github/knowledge-harvest-from-lms/hcmut_data/knowledge_graph.rdf"
g = Graph()
g.parse(rdf_file, format="xml")

# Chuyển RDF Graph sang NetworkX Graph
nx_graph = nx.DiGraph()  # Directed graph cho RDF

print(len(g), type(g))
for subj, pred, obj in list(g)[:2]:
    print('subj', subj)
    print('pred', pred)
    print('obj', obj)
    print('----------------------------------------------------------------')
    nx_graph.add_edge(str(subj), str(obj), label=str(pred))

# Vẽ đồ thị
pos = nx.spring_layout(nx_graph)  # Bố cục đồ thị
plt.figure(figsize=(12, 8))

# Vẽ các cạnh với nhãn
edge_labels = nx.get_edge_attributes(nx_graph, 'label')
nx.draw(nx_graph, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=1, font_weight="bold")
nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=edge_labels, font_size=8)

plt.title("RDF Graph Visualization", fontsize=15)
plt.show()

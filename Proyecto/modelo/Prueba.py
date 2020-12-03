import networkx as nx
G= nx.Graph()

#Añadir nodos 
G.add_node("Kevin Bacon")
G.add_node("Tom Hanks")
G.add_nodes_from(["Meg Ryan", "Parker Posey", "Lisa Kudrow"])

#Añadir aristas
G.add_edge("Kevin Bacon", "Tom Hanks")
G.add_edge("Kevin Bacon", "Meg Ryan")
G.add_edges_from([("Tom Hanks", "Meg Ryan"), ("Tom Hanks", "Parker Posey")])
G.add_edges_from([("Parker Posey", "Meg Ryan"), ("Parker Posey", "Lisa Kudrow")])

#Tamaño del grafo 

print(f"Numero de nodos: {len(G.nodes)}")
print(f"Numero de aristas: {len(G.edges)}")
print(f"Lista de nodos: {G.nodes}")
print(f"Lista de Aristas {G.edges}")

G.nodes["Tom Hanks"]["oscars"] = 100
G.nodes["Kevin Bacon"]["Numero de Peliculas"]=20
G.add_weighted_edges_from["Kevin Bacon","Tom hanks",]
G.edges["Kevin Bacon", "Tom Hanks"]["pelicula"] = "Apolo 13"
G.edges["Kevin Bacon", "Meg Ryan"]["pelicula"] = "En carne viva"
G.edges["Parker Posey", "Meg Ryan"]["pelicula"] = "Algo para recordar"
G.edges["Parker Posey", "Tom Hanks"]["pelicula"] = "Tienes un email"
G.edges["Parker Posey", "Lisa Kudrow"]["pelicula"] = "Esperando la hora"
print(G.nodes(data=True))
print(G.edges(data=True))
print(G["Kevin Bacon"])
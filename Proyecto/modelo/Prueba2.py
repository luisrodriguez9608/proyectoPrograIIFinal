import networkx as nx

Grapho=nx.Graph()

Grapho.add_node("Sanjose")
Grapho.add_nodes_from(["Herdia","Cartago","Alajuela","Guanacaste","Puntarenas","Limon"])
Grapho.add_edge("Heredia","Cartago")
Grapho.add_edges_from([("Cartago","Sanjose"),("Guanacaste","Puntarenas")])

print("Bienvenido al mapa de Costa Rica")
print("Opciones: \n 1) Ver mapa de CostaRica \n 2)Terminar programa")
Op=int(input("Digite la opcion que desea relizar: "))
if Op==1:
    print(f"Lista de Provincias: {Grapho.nodes}")
    print(f"Lista de Conexiones de las Provincias: {Grapho.edges}")
    print("Opciones: \n 1) CerrarPrograma \n 2)Eliminar una provincia \n 3)Agregar una conexion entre provincias")
    De=int(input("Digite la opcion que desea relizar: "))
    if De==1:
        SystemExit
    if De==2:
        print("Digite la provincia que desea elminar")
        s=input("")
        Grapho.remove_node(s)
    if De==3:
        print("Digite la conecion que desea relizar")
        primero=input("Primera provincia: ")
        segunda=input("Segunda provincia:")
        Grapho.add_edge(primero,segunda)
    print(f"Lista de nodos actualizada: {Grapho.nodes}")
    print(f"Lista de aristas actulizada: {Grapho.edges}")
if Op !=1:
    SystemExit
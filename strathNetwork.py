import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict 
class GBfsTraverser: 
  # Constructor 
  def __init__(self): 
    self.visited = []
    self.end_search = False
  def GBFS(self,graph, start_node, goal_node):
    queue = []
    queue.append(start_node)
    #print(queue)
    #set of visited nodes
    self.visited.append(start_node)
    while queue and not self.end_search: 
      # Dequeue a vertex from 
      s = queue.pop(0)          

      for i in list(graph[s]):
        if i not in self.visited:
          
          print ("Command; Drive to " ,i, " Estate/Junction", end = "\n")
          if i is goal_node:
            print("We have reached ",i," the final destination")
            self.visited.append(i)
            self.end_search = True
            break
          else:
            #print("Here",self.end_search)
            queue.append(i)
            #visited[i] = True
            self.visited.append(i)

G = nx.Graph()
nodes=["SportsComplex","Siwaka","Ph.1A","Ph.1B","Phase2","J1","Mada","STC","Phase3","ParkingLot"]
G.add_nodes_from(nodes)
G.nodes()#confirm nodes
#Add Edges and their weights
G.add_edge("SportsComplex","Siwaka",weight="450")
G.add_edge("Siwaka","Ph.1A",weight="10")
G.add_edge("Siwaka","Ph.1B",weight="230")
G.add_edge("Ph.1A","Mada",weight="850")
G.add_edge("Ph.1A","Ph.1B",weight="100")
G.add_edge("Ph.1B","Phase2",weight="112")
G.add_edge("Ph.1B","STC",weight="50")
G.add_edge("Phase2","J1",weight="600")
G.add_edge("Phase2","STC",weight="50")
G.add_edge("Phase2","Phase3",weight="500")
G.add_edge("J1","Mada",weight="200")
G.add_edge("Mada","ParkingLot",weight="700")
G.add_edge("Phase3","ParkingLot",weight="350")
G.add_edge("STC","ParkingLot",weight="250")

#position the nodes to resemble Nairobis map
G.nodes["SportsComplex"]['pos']=(0,0)
G.nodes["Siwaka"]['pos']=(2,0)
G.nodes["Ph.1A"]['pos']=(4,0)
G.nodes["Ph.1B"]['pos']=(4,-2)
G.nodes["Phase2"]['pos']=(6,-2)
G.nodes["J1"]['pos']=(10,-2)
G.nodes["Mada"]['pos']=(12,-2)
G.nodes["STC"]['pos']=(4,-4)
G.nodes["Phase3"]['pos']=(10,-4)
G.nodes["ParkingLot"]['pos']=(10,-6)

#store all positions in a variable
node_pos = nx.get_node_attributes(G,'pos')
#call BFS to return set of all possible routes to the goal
route_bfs = GBfsTraverser()
routes = route_bfs.GBFS(G,"SportsComplex","ParkingLot")
#print(route_bfs.visited)
route_list = route_bfs.visited
#color the nodes in the route_bfs
node_col = ['darkturquoise' if not node in route_list else 'peru' for node in G.nodes()]

peru_colored_edges = list(zip(route_list,route_list[1:]))
edge_col = ['darkturquoise' if not edge in peru_colored_edges else 'peru' for edge in G.edges()]
arc_weight=nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, node_pos,node_color= node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos,width=2,edge_color= edge_col)


nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()

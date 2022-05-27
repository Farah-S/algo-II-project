from collections import defaultdict

class Node_Distance :

    def __init__(self, name : int, dist : int) :
        self.name = name
        self.dist = dist

class Graph :

    def __init__ (self, node_count : int) :
        # Store the adjacency list as a dictionary
        # The default dictionary would create an empty list as a default (value) 
        # for the nonexistent keys.
        self.adjlist = defaultdict(list)
        self.node_count = node_count

    def Add_Into_Adjlist (self, src : int, node_dist : Node_Distance(int,int)) :
        self.adjlist[src].append(node_dist)

    def Dijkstras_Shortest_Path (self, source : int) :

        # Initialize the distance of all the nodes from the source node to infinity
        distance = [999999999999] * self.node_count
        # Distance of source node to itself is 0
        distance[source] = 0

        # Create a dictionary of { node, distance_from_source }
        dict_node_length = {source: 0}

        while dict_node_length :

            # Get the key for the smallest value in the dictionary
            # i.e Get the node with the shortest distance from the source
            current_source_node = min(dict_node_length, key = lambda k: dict_node_length[k])
            del dict_node_length[current_source_node]

            for node_dist in self.adjlist[current_source_node] :
                adjnode = node_dist.name
                length_to_adjnode = node_dist.dist

                # Edge relaxation
                if distance[adjnode] > distance[current_source_node] + length_to_adjnode :
                    distance[adjnode] = distance[current_source_node] + length_to_adjnode
                    dict_node_length[adjnode] = distance[adjnode]

        for i in range(self.node_count) :
            print("Source Node ("+str(source)+")  -> Destination Node(" + str(i) + ")  : " + str(distance[i]))

def main() :

	g = Graph(53)

    # Node 1: 
	g.Add_Into_Adjlist(1, Node_Distance(11, 2))

    # Node 2:
	g.Add_Into_Adjlist(2, Node_Distance(11, 7))
	g.Add_Into_Adjlist(2, Node_Distance(12, 2))
	g.Add_Into_Adjlist(2, Node_Distance(21, 16))

    # Node 3:
	g.Add_Into_Adjlist(3, Node_Distance(10, 1))

    # Node 4:
	g.Add_Into_Adjlist(4, Node_Distance(9, 1))
	g.Add_Into_Adjlist(4, Node_Distance(10, 3))
	g.Add_Into_Adjlist(4, Node_Distance(14, 3))

    # Node 5: 
	g.Add_Into_Adjlist(5, Node_Distance(7, 1))

	# Node 6: 
	g.Add_Into_Adjlist(6, Node_Distance(18, 7))

	# Node 7:
	g.Add_Into_Adjlist(7, Node_Distance(5, 1))
	g.Add_Into_Adjlist(7, Node_Distance(8, 1))
	g.Add_Into_Adjlist(7, Node_Distance(16, 1))

	# Node 8:
	g.Add_Into_Adjlist(8, Node_Distance(7, 1))
	g.Add_Into_Adjlist(8, Node_Distance(15, 1))

	# Node 9:
	g.Add_Into_Adjlist(9, Node_Distance(4, 1))

	# Node 10:
	g.Add_Into_Adjlist(10, Node_Distance(4, 3))
	g.Add_Into_Adjlist(10, Node_Distance(3, 1))
	g.Add_Into_Adjlist(10, Node_Distance(11, 3))

	# Node 11:
	g.Add_Into_Adjlist(11, Node_Distance(1, 2))
	g.Add_Into_Adjlist(11, Node_Distance(2, 7))
	g.Add_Into_Adjlist(11, Node_Distance(10, 3))

	# Node 12:
	g.Add_Into_Adjlist(12, Node_Distance(2, 2))

	# Node 13:
	g.Add_Into_Adjlist(13, Node_Distance(21, 11))

	# Node 14:
	g.Add_Into_Adjlist(14, Node_Distance(4, 3))
	g.Add_Into_Adjlist(14, Node_Distance(8, 5))
	g.Add_Into_Adjlist(14, Node_Distance(23, 10))

	# Node 15:
	g.Add_Into_Adjlist(15, Node_Distance(8, 1))

	# Node 16:
	g.Add_Into_Adjlist(16, Node_Distance(7, 1))
	g.Add_Into_Adjlist(16, Node_Distance(17, 1))
	g.Add_Into_Adjlist(16, Node_Distance(18, 1))

	# Node 17:
	g.Add_Into_Adjlist(17, Node_Distance(16, 1))

	# Node 18:
	g.Add_Into_Adjlist(18, Node_Distance(6, 7))
	g.Add_Into_Adjlist(18, Node_Distance(16, 1))
	g.Add_Into_Adjlist(18, Node_Distance(35, 11))

	# Node 19:
	g.Add_Into_Adjlist(19, Node_Distance(23, 20))

	# Node 20:
	g.Add_Into_Adjlist(20, Node_Distance(22, 1))

	g.Dijkstras_Shortest_Path(0)
	print("\n")
	g.Dijkstras_Shortest_Path(5);


if __name__ == "__main__" :
	main()

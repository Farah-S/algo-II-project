# Python Program for Floyd Warshall Algorithm

# Number of vertices in the graph
V = 53

# Define infinity as the large
# enough value. This value will be
# used for vertices not connected to each other
INF = 99999

# Solves all pair shortest path
# via Floyd Warshall Algorithm

def floydWarshall(graph):

	""" dist[][] will be the output
	matrix that will finally
		have the shortest distances
		between every pair of vertices """
	""" initializing the solution matrix
	same as input graph matrix
	OR we can say that the initial
	values of shortest distances
	are based on shortest paths considering no
	intermediate vertices """

	dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

	""" Add all vertices one by one
	to the set of intermediate
	vertices.
	---> Before start of an iteration,
	we have shortest distances
	between all pairs of vertices
	such that the shortest
	distances consider only the
	vertices in the set
	{0, 1, 2, .. k-1} as intermediate vertices.
	----> After the end of a
	iteration, vertex no. k is
	added to the set of intermediate
	vertices and the
	set becomes {0, 1, 2, .. k}
	"""
	for k in range(V):

		# pick all vertices as source one by one
		for i in range(V):

			# Pick all vertices as destination for the
			# above picked source
			for j in range(V):

				# If vertex k is on the shortest path from
				# i to j, then update the value of dist[i][j]
				dist[i][j] = min(dist[i][j],
								dist[i][k] + dist[k][j]
								)
	printSolution(dist)


# A utility function to print the solution
def printSolution(dist):
	print ("Following matrix shows the shortest distances\
between every pair of vertices")
	for i in range(V):
		for j in range(V):
			if(dist[i][j] == INF):
				print ("%7s" % ("INF"),end=" ")
			else:
				print ("%7d\t" % (dist[i][j]),end=' ')
			if j == V-1:
				print ()
		print("___________________________________________________________________________________________________________________________________________________________________")

# Driver program to test the above program
# Let us create the following weighted graph
"""
			10
	(0)------->(3)
		|		 /|\
	5 |		 |
		|		 | 1
	\|/		 |
	(1)------->(2)
			3		 """
             # 0   1   2   3   4   5   6   7   8   9    10  11  12  13  14  15  16  17  18  19    20  21  22  23  24  25  26  27  28  29    30  31  32  33  34  35  36  37  38  39     40  41  42  43  44  45  46  47  48  49     50  51  52
graph =	    [[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    2, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #0
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    7,  2, INF, INF, INF, INF, INF, INF, INF, INF,   16, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #1
			[INF, INF, INF, INF, INF, INF, INF, INF, INF,  1,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #2
			[INF, INF, INF, INF, INF, INF, INF, INF,  1,  3,   INF, INF, INF,  3, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #3
			[INF, INF, INF, INF, INF, INF,  1, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #4
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF,  7, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #5
			[INF, INF, INF, INF,  1, INF, INF,  1, INF, INF,   INF, INF, INF, INF, INF,  1, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #6
			[INF, INF, INF, INF, INF, INF,  1, INF, INF, INF,   INF, INF, INF,  5,  1, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #7
			[INF, INF, INF,  1, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #8
			[INF, INF,  1,  3, INF, INF, INF, INF, INF, INF,    3, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #9
			
			# 0   1   2   3   4   5   6   7   8   9    10  11  12  13  14  15  16  17  18  19    20  21  22  23  24  25  26  27  28  29    30  31  32  33  34  35  36  37  38  39     40  41  42  43  44  45  46  47  48  49     50  51  52
			[ 2,  7, INF, INF, INF, INF, INF, INF, INF,  3,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #10
			[INF,  2, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #11
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   11, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #12
			[INF, INF, INF,  3, INF, INF, INF,  5, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, 10, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #13
			[INF, INF, INF, INF, INF, INF, INF,  1, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #14
			[INF, INF, INF, INF, INF, INF,  1, INF, INF, INF,   INF, INF, INF, INF, INF, INF,  1,  1, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #15
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF,  1, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #16
			[INF, INF, INF, INF, INF,  7, INF, INF, INF, INF,   INF, INF, INF, INF, INF,  1, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, 11, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #17
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, 20, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #18
  			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF,  1, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #19

			# 0   1   2   3   4   5   6   7   8   9    10  11  12  13  14  15  16  17  18  19    20  21  22  23  24  25  26  27  28  29    30  31  32  33  34  35  36  37  38  39     40  41  42  43  44  45  46  47  48  49     50  51  52
			[INF, 16, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, 11, INF, INF, INF, INF, INF, INF, INF,   INF,  5, INF, INF,  7, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #20
  			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF,  1,    5, INF, INF,  1, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #21 
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, 10, INF, INF, INF, INF, 20, INF,   INF, INF, INF, INF, INF, INF, 11, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #22
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF,  1, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #23
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    7, INF, INF, INF, INF, INF, INF, INF,  7, INF,    2, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #24
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF,  9, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #25
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, 11, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #26
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF,  9, INF, INF,  5, INF,   INF, INF, INF, INF, INF, INF, INF,  7, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #27
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF,  7, INF, INF,  5, INF,  1,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #28
  			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF,  1, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #29
			
			# 0   1   2   3   4   5   6   7   8   9    10  11  12  13  14  15  16  17  18  19    20  21  22  23  24  25  26  27  28  29    30  31  32  33  34  35  36  37  38  39     40  41  42  43  44  45  46  47  48  49     50  51  52
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF,  2, INF, INF, INF, INF, INF,   INF,  6, INF, INF, INF, INF, INF, INF,  3, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #30
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    6, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #31 
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF,  6, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #32
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF,  8, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #33
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, 11, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #34
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF,  8, INF, INF,  8, INF, INF, INF,    INF, INF, INF,  3, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #35
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF,  6, INF, INF,  8, INF, INF, INF, INF,    INF, INF, INF, INF,  6, INF, INF, INF, INF, INF,    INF, INF, INF], #36
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF,  7, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF,  9,  5, INF, INF, INF, INF,    INF, INF, INF], #37
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    3, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF,  6,    INF, INF, 20], #38
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,     3, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #39

			# 0   1   2   3   4   5   6   7   8   9    10  11  12  13  14  15  16  17  18  19    20  21  22  23  24  25  26  27  28  29    30  31  32  33  34  35  36  37  38  39     40  41  42  43  44  45  46  47  48  49     50  51  52
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF,  3,    INF, 12, INF, INF, INF, INF, INF,  6, INF, INF,    INF, INF, INF], #40
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    12, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #41
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, 10, INF, INF, INF,    INF, INF, INF], #42 
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, 	3, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #43
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, 	6, 	9, INF, INF,    INF, INF, INF, INF, INF, INF,  5, INF, INF, INF,    INF, INF, INF], #44
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, 	5, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF], #45
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, 10, INF,  5, INF, INF, INF, INF, INF,    INF,  7, INF], #46
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,     6, INF, INF, INF, INF, INF, INF, INF, INF,  5,     5, INF, INF], #47
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF,  2,    INF, INF, INF], #48
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF,  6, INF,    INF, INF, INF, INF, INF, INF, INF,  5,  2, INF,    INF, INF, INF], #49

			# 0   1   2   3   4   5   6   7   8   9    10  11  12  13  14  15  16  17  18  19    20  21  22  23  24  25  26  27  28  29    30  31  32  33  34  35  36  37  38  39     40  41  42  43  44  45  46  47  48  49     50  51  52
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF, INF,  5, INF, INF,    INF, INF, INF], #50
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF, INF,  7, INF, INF, INF,    INF, INF, INF], #51
			[INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   INF, INF, INF, INF, INF, INF, INF, INF, 20, INF,    INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,    INF, INF, INF]  #52
		]

for i in range(53): 
	for j in range(53):
		if(i==j):
			graph[i][j]=0
   
# Print the solution
floydWarshall(graph)
# This code is contributed by Mythri J L


		   
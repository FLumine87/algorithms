# P-1 Consider a simple undirected graph with 5 nodes labeled A, B, C, D, and E, where 
# the edges are AB, BC, CD, DE, and EA. What is the degree of node C?

# answer:  the degrees of node C are 2.

# P-2 A tree is a special type of graph that is connected and contains no cycles. If a 
# graph has 10 nodes and is a tree, how many edges does it have?

# answer:  the tree has 9 edges.

# R-14.12 Explain why the DFS traversal runs in 𝑂(𝑛2) time on an n-vertex simple 
# graph that is represented with the adjacency matrix structure. 

# answer:  In a DFS traversal using an adjacency matrix, for each of the n vertices, we
# need to check all n entries in the corresponding row of the matrix to find adjacent

# R-14.14 A simple undirected graph is complete if it contains an edge between every 
# pair of distinct vertices. What does a depth-first search tree of a complete graph look 
# like? 

# answer:the DFS tree is a path containing all n vertices, with n-1 tree edges and a height of n-1.

# R-14.15 Recalling the definition of a complete graph from Exercise R-14.14, what 
# does a breadth-first search tree of a complete graph look like? 

# answer:  The BFS tree is always a star-shaped tree with height 2, where the root node is directly connected to all other vertices.

# R-14.16 Let G be an undirected graph whose vertices are the integers 1 through 8, and 
# let the adjacent vertices of each vertex be given by the table below: 
# vertex adjacent vertices 
# 1 - (2, 3, 4) 
# 2 - (1, 3, 4) 
# 3 - (1, 2, 4) 
# 4 - (1, 2, 3, 6) 
# 5 - (6, 7, 8) 
# 6 - (4, 5, 7) 
# 7 - (5, 6, 8) 
# 8 - (5, 7) 
# Assume that, in a traversal of G, the adjacent vertices of a given vertex are returned in 
# the same order as they are listed in the table above. 
# a. Give the sequence of vertices of G visited using a DFS traversal starting at 
# vertex 1. 

# answer: [1, 2, 3, 4, 6, 5, 7, 8]

# b. Give the sequence of vertices visited using a BFS traversal starting at vertex 1.

# answer: [1, 2, 3, 4, 6, 5, 7, 8]
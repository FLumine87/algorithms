# P1. Perform the Prim’s algorithm on the following graph, starting from vertex A. 

# answer:
# A → B (1)  
# A,B → D (3)  
# A,B,D → C (2)  
# A,B,D,C → E (2)  
# A,B,D,C,E → F (2)  
# A,B,C,D,E,F → G (6)
# The Total Weight of minimum spanning tree: 16

#  P2. Perform the Kruskal’s algorithm on the following graph. 

# answer:
# A → B (1)
# C → D (2)
# D → E (2)
# E → F (2)
# B → D (3)
# F → G (6)
# The Total Weight of minimum spanning tree: 16

# P3. Perform the Prim’s algorithm on the following graph, starting from vertex 1.

# answer:
# 1 → 5 (18)
# 1,5 → 2 (15)
# 1,2,5 → 4 (6)
# 1,2,4,5 → 3 (14)
# The Total Weight of minimum spanning tree: 53

# P4. Perform the Kruskal’s algorithm on the following graph. 

# answer:
# 4 → 5 (6)
# 4 → 3 (14)
# 2 → 5 (15)
# 1 → 5 (18)
# The Total Weight of minimum spanning tree: 53

# P5. Given the following graph, run Dijkstra’s Algorithm to find the shortest path from 
# A to H. 

# answer:
# turn 1: S = {A}; 
# A → B (1)：dist[B] = 1，prev[B] = A
# A → F (4)：dist[F] = 4，prev[F] = A
# turn 2: S = {A, B};
# B → F (2)：dist[F] = 3，prev[F] = B
# B → C (6)：dist[C] = 7，prev[C] = B
# B → H (1)：dist[H] = 2，prev[H] = B
# turn 3: S = {A, B, H};
# H → C (4)：dist[C] = 6，prev[C] = H
# H → F (2)：remains dist[F] = 3，prev[F] = B
# turn 4: S = {A, B, H, F};
# F → C (3)：dist[C] = 6，prev[C] = F
# shortest path: A → B → H (2)

# P6. Find the shortest path from A to C. 

# answer:
# A → B → F → C (6)

# P7. Given the following graph, run Dijkstra’s Algorithm to find the shortest path from 
# s to e. 

# answer:
# turn 1: S = {s};
# s → a (1)：dist[a] = 1，prev[a] = s
# s → b (5)：dist[b] = 5，prev[b] = s
# turn 2: S = {s, a};
# a → b (2)：dist[b] = 3，prev[b] = a
# a → c (2)：dist[c] = 3，prev[c] = a
# a → d (1)：dist[d] = 2，prev[d] = a
# turn 3: S = {s, a, d};
# d → e (2)：dist[e] = 4，prev[e] = d
# turn 4: S = {s, a, d, e};
# turn 5: S = {s, a, d, e, b};
# b → d (2)：remains dist[d] = 2，prev[e] = a
# turn 6: S = {s, a, d, e, b, c};
# c → e (1)：remains dist[e] = 4，prev[e] = d
# c → d (3)：remains dist[d] = 2，prev[d] = a
# shortest path: s → a → d → e (4)

# P8. Find the shortest path from s to c. 

# answer:
# s → a → c (3)
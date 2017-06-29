def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

# A function that does union of two sets of x and y
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    # Attach smaller rank tree under root of high rank tree
    # (Union by Rank)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    #If ranks are same, then make one as root and increment
    # its rank by one
    else :
        parent[yroot] = xroot
        rank[xroot] += 1

# The main function to construct MST using Kruskal's algorithm
def KruskalMST(graph, V, rev_dict):

    result =[] #This will store the resultant MST

    i = 0 # An index variable, used for sorted edges
    e = 0 # An index variable, used for result[]

    #Step 1:  Sort all the edges in non-decreasing order of their
    # weight.  If we are not allowed to change the given graph, we
    # can create a copy of graph
    graph =  sorted(graph,key=lambda item: item[2])

    parent = [] ; rank = []

    # Create V subsets with single elements
    for node in range(V):
        parent.append(node)
        rank.append(0)

    # Number of edges to be taken is equal to V-1
    while e < V -1 :

        # Step 2: Pick the smallest edge and increment the index
        # for next iteration
        u,v,w =  graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent ,v)

        if x != y:
            e = e + 1
            result.append([u,v,w])
            union(parent, rank, x, y)
        # Else discard the edge

    p1 = []
    final_result = {}
    for u,v,weight  in result:
        p1 = [(rev_dict[v],weight)]
        if rev_dict[u] not in final_result:
            final_result[rev_dict[u]] = p1
        else:
            final_result[rev_dict[u]] = final_result[rev_dict[u]].append(p1)


    return final_result

def question3(s1):
    n = len(s1)
    dict1 = {}
    rev_dict = {}
    count = 0
    u,v,w = None, None, None
    graph = []
    for i in s1:
        dict1[i] = count
        rev_dict[count] = i
        count += 1
    print dict1
    print rev_dict
    
    print type(s1)

    for i in s1:
        for j in s1[i]:
            print j[0]
            u,v,w = dict1[i], dict1[j[0]], j[1]
            graph.append([u,v,w])
    print graph

    return KruskalMST(graph, count, rev_dict)

# Main program
def main():
    s1 = {'A': [('B', 2)],
          'B': [('A', 4), ('C', 2)],
          'C': [('A', 2), ('B', 5)]}
    question3(s1)

if __name__ == '__main__':
    main()
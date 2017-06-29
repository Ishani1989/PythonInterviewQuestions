'''Question 1
Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", 
then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.'''

# function to test if str2 is an anagram of str1
def anagram(str1, str2):
    return sorted(str1) == sorted(str2)


# function to check if any anagram of s is contained in t
def Question1(s, t):
    for i in range(len(t)-len(s)+ 1):
        if anagram(t[i: i+len(s)], s):
            return True
    return False


'''Question 2
Given a string a, find the longest palindromic substring contained in a. Your function definition should look like question2(a), and return a string.'''


# check if string s is palindrome
def Palindrome(s):
    return s == s[::-1]

def question2(s):
    if s:
        x, m, n = 0, 0, 0
        for i in xrange(0, len(s)):
            for j in xrange(i + 1, len(s) + 1):
                pattern = s[i:j]
                if Palindrome(pattern) and len(pattern) > x:
                    x = len(pattern)
                    m, n = i, j
        result = s[m:n]
        return result

'''Question 3
Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
Vertices are represented as unique strings. The function definition should be question3(G)'''

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
    #print dict1
    #print rev_dict
    
    for i in s1:
        for j in s1[i]:
            u,v,w = dict1[i], dict1[j[0]], j[1]
            graph.append([u,v,w])
    print graph

    return KruskalMST(graph, count, rev_dict)

'''
Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is 
the farthest node from the root that is an ancestor of both nodes. For example, the root is a common 
ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that 
left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the 
tree itself adheres to all BST properties. The function definition should look like 
"question4(T, r, n1, n2)", where T is the tree represented as a matrix, where the index of the list is 
equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer 
representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular 
order. For example, one test case might be 
question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4), and the answer would be 3.
'''

def question4(T, r, n1, n2):
    mylist = []
    while n1 != r:
        n1 = isparent(T, n1)
        mylist.append(n1)
    if len(mylist) == 0:
        return False
    while n2 != r:
        n2 = isparent(T, n2)
        if n2 in mylist:
            return n2
    return False
    
    
def isparent(T, n):
    a = len(T)
    for i in range(a):
        if T[i][n] == 1:
            return i
    return False


print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)


'''Question 5
Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". 
You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None 

# return character at m position from end of ll
def question5(ll, m):
    list1 = ll
    position = ll

#loop through the linked list and return data at position
    for i in range(0, m):
        list1 = list1.next
    while list1 is not None:
        list1 = list1.next
        position = position.next
    return position.data


# Main program
def main():

    #call for question1
    print ('---------Question 1 output--------')

    print Question1("ad", "udacity")
    # True

    print Question1("21", "8789610789712")
    # True

    print Question1("today", "tomorrow")
    # False


    # call for question 2 :
    print ('---------Question 2 output--------')

    print question2("racecar")
     # racecar
    print question2("apple")
     # pp
    print question2("udacity")
    # u

    #call for question3

    s1 = {'A': [('B', 2)],
          'B': [('A', 4), ('C', 2)],
          'C': [('A', 2), ('B', 5)]}
    
    s2 = {'A': [('C', 5), ('B', 3)],
          'B': [('A', 2), ('C', 7)],
          'C': [('A', 1), ('B', 4)]}
    
    s3 = {'A': [('C', 5)],
          'B': [('C', 4), ('A', 2)],
          'C': [('B', 2), ('A', 3)]}
    
    print ('---------Question 3 output--------')
    print question3(s1)
    
    ''' [[0, 2, 2], [1, 0, 2], [1, 2, 5], [2, 0, 4], [2, 1, 2]]
    {'A': [('B', 2)], 'C': [('A', 2)]}'''
    
    print question3(s2)
    
    '''[[0, 1, 5], [0, 2, 3], [1, 0, 1], [1, 2, 4], [2, 0, 2], [2, 1, 7]]
    {'C': [('A', 1)], 'B': [('A', 2)]}'''
    
    print question3(s3)
    
    '''[[0, 1, 5], [1, 2, 2], [1, 0, 3], [2, 1, 4], [2, 0, 2]]
    {'C': [('B', 2)], 'B': [('A', 2)]}'''

    #call for question 4
    print ('---------Question 4 output--------')

    print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)

    # Output : 3

    print question4([[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,0,1)

    # Output : 3

    print question4([[1,0,0,0,0],[0,0,0,0,0],[1,1,0,0,0],[0,1,0,0,1],[0,0,1,1,0]],3,1,2)

    # Output : 4


    #call for question 5

    A = Node(2)
    B = Node(3)
    C = Node(8)
    D = Node(1)
    E = Node(6)
        
    A.next = B 
    B.next = C
    C.next = D 
    D.next = E

    print ('---------Question 5 output--------')
    print question5(A, 3)
    # Output :8
    print question5(D, 1)
    # Output :6
    print question5(C, 2)
    # Output :1


if __name__ == '__main__':
    main()



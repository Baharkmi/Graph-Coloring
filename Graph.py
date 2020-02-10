import random
import copy
from random import randint
from random import shuffle

number_of_nodes = 0
number_of_edges = 0
color_counter   = 1

chosen_node   = 0
chosen_color1 = 0
chosen_color2 = 0

colored_graph = []

def generator_graph():
    global num
    global graph
    global number_of_nodes
    graph =[]
    temp =[]

    num = input('Enter nodes: ')
    number_of_nodes = int(num)
    for i in range(1,int(num)+1):
        for j in range(1,randint(1,int(num)+1)):
            if((i!=j) and (j not in temp)):
                temp += [j]
        graph = graph + [temp]        
        temp = []

    #print("graph",graph)
    
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            t = graph[i][j]
            if(i+1 not in graph[t-1] and t!=i+1):
                graph[t-1] += [i+1]
    print(graph)

def new_graph():
    global graph
    global number_of_nodes
    graph  = []
    number_of_nodes = 5
    graph = [[2,5],[1,5,3],[2,4],[3,5],[1,2,4]]
"""   arr=[]
    tup = tuple()
    tup1 =tuple()
    
    for i in range(len(graph)):
            for j in graph[i]:
                #print(i+1,"=>",j)
                if(j !=''):
                    tup =(i+1,j)
                    tup1= (j,i+1)           
                    arr = arr+[tup]+[tup1]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(arr[j][0] == i+1):
                temp +=[arr[j][1]]
        fgraph +=[temp]
        temp=[]
    ffgraph=[]
    for i in range(len(fgraph)):
        if(fgraph[i]!=[]):
            ffgraph +=[fgraph[i]]
    fgraph = ffgraph
    print(color_graph_first(fgraph))



    
    #print("fgrapgh",fgraph)
    #print("ffgraph",ffgraph)  
    print("fgraph",fgraph)
    #print(arr)
    #print(graph) """



def find_delta(arr):
    global max_degree
    max_degree= 0 
    for i in range(len(arr)):
        if(len(arr[i])> max_degree):
            max_degree=len(arr[i])
    print("delta is ",int(max_degree)+1)
    return max_degree


def color_graph_first(graph):
    global color
    global color_counter
    color_counter=0
    color = []
    color = copy.deepcopy(graph)
    
    for i in range(len(color)):
        for j in range(len(color[i])) :
            color[i][j]=1
    color_counter =1
    return color


def proper_coloring(colorr):
    counter =0 
    global color_counter
    #print("arrrrrrrrrrrr",arr)
    for i in colorr :
        counter +=1
        #print("i",i)
        for j in range(len(i)) :
            #print("arr[j]",arr[j])
            for k in i[j+1:]:
                #print("k",k)
                #print(i[j],k,"i[j] , k")
                if(i[j]==k): # age 2 ta rang yki bod dor fard darim 
                    #add_color(counter)
                    return 0
    return color_counter

def if_odd_degree_make_even():
    
    global num
    global even_graph
    global ncolor
    nlist=[]
    listt =[]
    even_graph = copy.deepcopy(graph)
    ncolor = copy.deepcopy(color)
    for i in range(len(even_graph)) :
        
        if(len(even_graph[i])%2!=0):
            even_graph[i].append(len(graph)+1)
            listt+=[i+1]
            extra_vertex = len(graph)+1
            #print(i)
            
    
    if(listt!=[]):
        even_graph.append(listt)
        for i in listt:
            nlist+=[1]
        ncolor.append(nlist)            

    print("chi chiam",even_graph)
    print("fffffffffff",ncolor)
    #euleri_path=find_eulerian_tour()
    #print("1")
    #find_(even_graph)
    #print(list_tup)
    #print(find_eulerian_tour(list_tup))
    eulerian_cycle = []
    #find_eulerian_cycle(u, even_graph, eulerian_cycle)
   
#def find_(egr):
    #global list_tup
   # counter =0
   # euleri_path=[]
   # for p in egr:
   #     counter +=1
    #    for j in range(len(p)):
     #       tup3 = ((counter,int(p[j])))
      #      list_tup = list_tup+ [tup3]
    #print(list_tup)
            
    #euler_path =find_eulerian_tour(list_tup)
    #euleri_path= eulerPath(list_tup)
    #print(euleri_path)
    #add_color(euleri_path)



#def add_color(euleri_path):
#    print(euleri_path)
#    global arr
#    for i in euleri_path:
#        for j in range(len(even_gragh)):
#            if(evengraph[i][j]==i):
#                print("even_grapgh[i][j]=>",evengraph[i][j])
                #ncolor[i][j]+=1
#def find_adjac_list(even_graph):

def add_edge(u, v, e_adj_graph):

    e_adj_graph[u].append(v)
    e_adj_graph[v].append(u)

def remove_edge(u, v, e_adj_graph):
    
    for index, key in enumerate(e_adj_graph[u]):
        if(key == v):
            e_adj_graph[u].pop(index)

    for index, key in enumerate(e_adj_graph[v]):
        if (key == u):
            e_adj_graph[v].pop(index)

def DFS_count(v, visited, e_adj_graph):
    
    count = 1
    visited[v] = True

    for i in e_adj_graph[v]:
        if (visited[i] == False):
            count = count + DFS_count(i, visited, e_adj_graph)
    return count


def check_odd_cycle(two_color_graph, adj_two_color_graph):

    nodes_degrees = [0]*(number_of_nodes+1)

    for i in range(1,number_of_nodes+1):
        for j in range(1, number_of_nodes + 1):
            if (two_color_graph[i][j]==1):
                nodes_degrees[i] += 1
    nc = []

    for i in range(1, number_of_nodes + 1):
        if(nodes_degrees[i]>0):
            nc += [i]



# check if the degree of all nodes is 2 or 0
    for i in nc:
        if(nodes_degrees[i] != 2):
            return False


# check if the number of edges is odd
    if (len(nc)%2)==0:
        return False

    return  True


def is_valid_next_edge(u, v, e_adj_graph):

    if(len(e_adj_graph[u]) == 1):
        return True

    else:

        #count the vertices reachable from u
        visited = [False] * (number_of_nodes+2) #since we have added the node which number is "number_of_nodes+1"
        count_1 = DFS_count(u, visited, e_adj_graph)

        #remove edge (u, v) then count the vertices reachable from u
        remove_edge(u, v, e_adj_graph)
        visited = [False] * (number_of_nodes+2) #since we have added the node which number is "number_of_nodes+1"
        count_2 = DFS_count(u, visited, e_adj_graph)

        #Add the edge back to the graph
        add_edge(u, v, e_adj_graph)

        if count_1 > count_2:
            return False
        else:
            return True

def find_eulerian_cycle(u, e_adj_graph, eulerian_cycle):
    
    for v in e_adj_graph[u]:
        if is_valid_next_edge(u, v, e_adj_graph):
            eulerian_cycle += [(u,v)]
            remove_edge(u, v, e_adj_graph)
            find_eulerian_cycle(v, e_adj_graph, eulerian_cycle)


def find_two_color_graph(node_num, color_1, color_2):

    two_color_graph = []
    for i in range(len(graph)):
        for j in rage(len(graph[i])):
            if color[i][graph[i][j]] == color_1 or colored_graph[i][j] == color_2:
            colored_graph[i+1][color[i][j]] = 1
            
    two_color_graph = [[0] * (number_of_nodes + 1) for i in range(number_of_nodes + 1)]
    for i in range(1, number_of_nodes + 1):
        for j in range(1, number_of_nodes + 1):
            if colored_graph[i][j] == color_1 or colored_graph[i][j] == color_2:
                two_color_graph[i][j] = 1
                two_color_graph[j][i] = 1
   

    adj_two_color_graph = [[]]
    for i in range(1, number_of_nodes + 1):
        tmp = []
        for j in range(1, number_of_nodes + 1):
            if (two_color_graph[i][j] == 1):
                tmp += [j]
        adj_two_color_graph += [tmp]

    visited = [False]*(number_of_nodes+1)
    DFS_count(node_num, visited, adj_two_color_graph)
    for i in range(1, number_of_nodes + 1):
        for j in range(1, number_of_nodes + 1):
            if (visited[i]==False) or (visited[j]==False):
                two_color_graph[i][j] = 0
                two_color_graph[j][i] = 0
    return two_color_graph

def improve_node_with_colors(node_num, color_1, color_2):
    two_color_graph = find_two_color_graph(node_num, color_1, color_2)

    adj_two_color_graph = [[]]
    for i in range(1,number_of_nodes+1):
        tmp = []
        for j in range(1,number_of_nodes+1):
            if(two_color_graph[i][j]==1):
                tmp += [j]
        adj_two_color_graph += [tmp]


    is_odd_cycle = check_odd_cycle(two_color_graph, adj_two_color_graph)

    if(is_odd_cycle):
        return False



    adj_two_color_graph = adj_two_color_graph+[[]]
    is_added_node_used = False
    for i in range(1, number_of_nodes + 1):
        if (len(adj_two_color_graph[i])%2)==1:
            is_added_node_used = True
            adj_two_color_graph[i] += [number_of_nodes+1]
            adj_two_color_graph[number_of_nodes+1] += [i]


    eulerian_cycle = []
    if(is_added_node_used==True):
        find_eulerian_cycle(number_of_nodes+1, adj_two_color_graph, eulerian_cycle)
    else:
        find_eulerian_cycle(node_num, adj_two_color_graph, eulerian_cycle)


    cntr = 0
    for i,j in eulerian_cycle:
        if (i!=(number_of_nodes+1)) and (j!=(number_of_nodes+1)):
            if cntr%2==0:
                colored_graph[i][j] = color_1
                colored_graph[j][i] = color_1
            else :
                colored_graph[i][j] = color_2
                colored_graph[j][i] = color_2
        cntr += 1

    return True


def improve_node(node_num):
    global chosen_color1, chosen_color2
    global color_counter
    is_improvable = False


    colors_used_count = [0] * (color_counter + 1)
    colors_used_more_than_once = []
    colors_not_used = []

    for i in range(1,number_of_nodes+1):
        if colored_graph[node_num][i] != 0:
            colors_used_count[colored_graph[node_num][i]] += 1

    for i in range(1,color_counter+1):
        if (colors_used_count[i]>1):
            colors_used_more_than_once += [i]

        if (colors_used_count[i]==0):
            colors_not_used += [i]


    shuffle(colors_used_more_than_once)
    shuffle(colors_not_used)

    color_pairs = [(x,y) for x in colors_used_more_than_once for y in colors_not_used]

    for x,y in color_pairs:
        is_improvable = improve_node_with_colors(node_num, x, y)
        if is_improvable:
            chosen_color1 = x
            chosen_color2 = y
            break

    return is_improvable


def improve():
    global chosen_node
    nodes = range(1, number_of_nodes + 1)
    is_improved = False

    while(True):
        shuffle(nodes)

        for n in nodes:
            chosen_node = n
            is_improved = improve_node(n)
            if (is_improved):
                break

        if(is_improved==False):
            break

def make_colored_matrix(color):
    global colored_graph
    colored_graph = [[0] * (number_of_nodes+1) for i in range (number_of_nodes+1)]
    for i in range(len(graph)):
        for j in rage(len(graph[i])):
            colored_graph[i+1][graph[i][j]] = 1
        print("\n")
        
        
def start():
    global color
    global color_counter
    #generator_graph()
    new_graph()
    for i in range(10):
        color_counter = 0
        color = []
        color = color_graph_first(graph)
        make_colored_matrix(color)
        #print(colored_graph)
        while True:
            if(proper_coloring(color)==0):
                color_counter+=1
                improve()
            elif(proper_coloring(color)!=0):
                print("Colored with " , color_counter);
                break;



start()

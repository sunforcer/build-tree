# Build Tree from Array 1.0
# 11.02.2022

source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]

expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}

temp_array = []
tree_leaf = []
final_input = []

def to_tree(matrix):                        					#Main programm
    
    find_tree_leaf(matrix, "None")          					#Seach tree leaf  

    array_add(source)              								#Add tree leaf to the array
 
    result = array_to_tree(final_input)     					#Convert tree array to a dictionary
      
    print("Result:")
    print(result)                           					#Result as is

    print("Expected:")
    print(expected)                         					#Expected result

    return result


def find_tree_leaf(matrix, value):                              #Search tree leaf

    for element in matrix:        
        if str(element[0]) == value:

            find_tree_leaf(matrix, element[1])                  #Recursion
                         
            if array_search(matrix, element[1]):                #Check if elements already in array
                #print("Tree leaf found:", element[1]) 
                tree_leaf.append(element[1])                    #Add last element in tree (leaf) in array

    return 0


def find_tree_reverse(matrix, value):                           #Reverse search all tree elements from leaf to the root

    for element in matrix:        
        if str(element[1]) == value:
            find_tree_reverse(matrix, element[0])               #Recursion
            temp_array.append(element[1])                       #Append all tree elements from leaf to the root
            

    return 0    


def array_search(array, value):                                 #Search element in array

    for element in array:        
        if element[0] == value:
            
            return 0      

    return 1

def array_add(array):                                            #Add tree element from leaf to root in array as a list

    final_input.clear()

    for element in tree_leaf:        
        find_tree_reverse(array, element)
        final_input.append(list(temp_array))
        temp_array.clear()

    return 0

def array_to_tree(source):                                       #Convert array to dictionary view
    
    forest = {}

    for *path, last in source:
        node = forest
        for code in path:
            node = node.setdefault(code, {})
        node[last] = {}

    return forest
    

assert to_tree(source) == expected                              #Check result






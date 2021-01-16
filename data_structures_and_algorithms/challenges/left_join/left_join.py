from data_structures_and_algorithms.data_structures.hashtable.hashtable import *

def left_join(hash1,hash2):
    output = []

    for element in hash1.map:

        if element != None:

            for i in element:
                element_list = []
                element_list.append(i[0])
                element_list.append(i[1])
        
                if hash2.contains(i[0]):
                    element_list.append(hash2.get(i[0]))
                else:
                    element_list.append(None)
        
                output.append(element_list)
       
    return output

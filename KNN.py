matrics = set(['dot','cosine','euclidean','manhattan','hamming'])

def dot(list1,list2):
    list1 = np.array(list1)
    list2 = np.array(list2)
    if(len(list1)!=len(list2)): raise Exception("List length is not same in cosine distance function")
    else: return np.dot(list1,list2)

def cosine(list1,list2):
    list1 = np.array(list1)
    list2 = np.array(list2)
    if(len(list1)!=len(list2)): raise Exception("List length is not same in cosine distance function")
    else: return np.dot(list1,list2)/(np.linalg.norm(list1)*np.linalg.norm(list2))

def euclidean(list1,list2):
    list1 = np.array(list1)
    list2 = np.array(list2)
    if(len(list1)!=len(list2)): raise Exception("List length is not same in Euclidean distance function")
    else: return np.linalg.norm(list1-list2)

def manhattan(list1,list2):
    list1 = np.array(list1)
    list2 = np.array(list2)
    if(len(list1)!=len(list2)): raise Exception("List length is not same in manhattan distance function")
    else: return np.sum(np.abs(list2-list1))

def hamming(list1,list2):
    list3 = np.array(list1).astype(dtype=bool)
    list4 = np.array(list2).astype(dtype=bool)
    if(len(list3)!=len(list4)): raise Exception("List length is not same in hamming distance function")
    else: return np.sum(np.logical_xor(list3,list4))

def knn_predict(x,y,xtest,k_neighbour=5,matric='cosine'):
    if matric not in matrics: raise Exception("Enter Correct Matric : ",matrics)
    y_pred = list()
    rev = False
    if matric == 'cosine': 
        rev = True
    for i in range(len(xtest)):
        store_distance = dict()
        for j in range(len(x)): 
            store_distance[x[j]]=globals()[matric](xtest[i],x[j])
        count_dict = {}
        for k in dict(sorted(store_distance.items(),key=lambda x:x[1], reverse=rev))[:k_neighbour]:
            
            if k in count_dict:
                count_dict[k.keys()] += 1
            else:
                count_dict[k.keys()] = 1

    y.append(sorted(count_dict.items(),key=lambda x:x[1], reverse= True)[0])
    return y_pred
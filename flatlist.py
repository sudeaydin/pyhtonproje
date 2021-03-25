#flatten lists

def flat_list(l1):
    for i in range(len(l1)):
        if type(l1[i])!=list:
            l2.append(l1[i])
        else:
            flat_list(l1[i])
    return l2

l1=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
l2=list()
print(flat_list(l1))

#sort nested lists
def sort_list(l1):
    l1.reverse()
    for i in l1:
        if type(i)==list:
            i.reverse()
    return l1


l=[[1, 2], [3, 4], [5, 6, 7]]
print(sort_list(l))

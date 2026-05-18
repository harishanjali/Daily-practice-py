x = [[1,2,3],[4,5],[6,7],8]

def flatlist(nst_list):
    numbers = []
    if isinstance(nst_list,list):
        for sub_list in nst_list:
             numbers += flatlist(sub_list)
    elif isinstance(nst_list,int):
        numbers.append(nst_list)
    return numbers
res = flatlist(x)
print(res)
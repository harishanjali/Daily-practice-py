#remove duplicates from the nested list, keeping the original structure
# x = [1,[2,2,2],[4,[1,5,3]],6,[4,7]]
# def remove_duplicate_nested(lst):
#     res=[]
#     for sub_lst in (lst):
#         if type(sub_lst)==list:
#             res.append(remove_duplicate_nested(sub_lst))
#         else:
#             if sub_lst not in res:
#                 res.append(sub_lst)
#     return (res)

# res = remove_duplicate_nested(x)
# print(res)


def dup(a, b=[]):
    c = []

    for item in a:
        if type(item) == list:
            d = dup(item, b)

            if d != []:
                c.append(d)

        else:
            if item not in b:
                b.append(item)
                c.append(item)

    return c


data = [1, [2, 2, 2], [4, [1, 5, 3]], 6, [4, 7,1,2,3,7,7,7,7]]

output = dup(data)

print(output)
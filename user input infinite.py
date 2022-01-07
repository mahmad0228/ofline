def ghj():
    a = True
    lis = []
    fin = []
    while a:
        b = input('enter element:')
        lis.append(b)
        if b:
            a = True
        else:
            a = False
    lis.pop()
    for i in range(len(lis)):
        lis[i] = int(lis[i])
        fin.append(lis[i])
    print(fin)
ghj()


#######################
# a = True
# lis = []
# while a:
#     b = input('enter element:')
#     lis.append(b)
#     if b:
#         a = True
#     else:
#         a = False
#     lis.pop()
#     # return lis
# print(lis)



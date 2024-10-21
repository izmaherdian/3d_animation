num = 16
# Rèplica de la funció edges del Torus
for i in range(256):
    lst = []
    lst.append(i)
    for j in range(256):
        if j == (i+1)%(num*num) or j == (i-1)%(num*num) or j == (i+num)%(num*num) or j == (i-num)%(num*num):
            lst.append(j)
    print(lst)

num = 16
# Rèplica de la funció edges del Torus
for i in range(256):
    lst = []
    lst.append(i)
    for j in range(256):
        if i%16 == 0:
            if j == (i+1)%(num*num) or (j-i)%(num*num) == 15 or j == (i+num)%(num*num) or j == (i-num)%(num*num):
                lst.append(j)
        elif i%16 == 15:
            if (j+15) == i or (j+1) == i or j == (i+num)%(num*num) or j == (i-num)%(num*num):
                lst.append(j)
        else:
            if j == (i+1)%(num*num) or j == (i-1)%(num*num) or j == (i+num)%(num*num) or j == (i-num)%(num*num):
                lst.append(j)
    print(lst)

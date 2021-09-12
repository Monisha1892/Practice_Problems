string = "hello python program how are alphabet and aand allphabet heello howw you"
lst = string.split(" ")
d = []
final = []

while len(lst) > 0:
    temp = lst[0]
    flag= 1
    for i in range(1, len(lst)):
        if ord(temp[0]) < ord(lst[i][0]):
            temp = temp
        else:
            temp = lst[i]
    lst.remove(temp)
    d.append(temp)

    for j in range(0, len(lst)):
        if ord(temp[0]) == ord(lst[j][0]):
            d.append(lst[j])
    if len(d) == 1:
        flag = 0
    else:
        flag = 1

    if flag:
        lst.append(temp)
        for l in range(0, len(d)):
            for m in range(l + 1, len(d)):
                siz = min(len(d[l]), len(d[m]))
                for k in range(0, siz):
                    if d[l][k] != d[m][k]:
                        if ord(d[l][k]) > ord(d[m][k]):
                            d[l], d[m] = d[m], d[l]
                            break
                        else:
                            d[l], d[m] = d[l], d[m]
                            break
        for n in d:
            final.append(n)
            lst.remove(n)
        d = []

    else:
        final.append(temp)
        d = []

print(final)

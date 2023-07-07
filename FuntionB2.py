def countdown(x):
    mylist = []
    for i in range(x, -1, -1):
        mylist.append(i)
    return mylist
print(countdown(10))

def p_r(list):
    print(list[0])
    return list[1]
print(p_r([1,2]))

def fpl(mylist):
    return mylist[0] + len(mylist)
print(fpl([1,2,3,4]))

def value(list):
    if len(list) < 2:
        return False
    newlist = []
    for i in range(0, len(list)):
        if list[i] > list[1]:
            newlist.append(list[i])
    print(len(newlist))
    return newlist
print(value([8,5,4,3,9,7]))
print(value([3]))

def lV(x,y):
    mylist = []
    for i in range(0,x):
        mylist.append(y)
    return mylist

print(lV(4,7))
print(lV(6,2))
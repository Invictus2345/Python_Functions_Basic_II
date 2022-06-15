#1
def countdown(x):
    if x>0:
        print(x)
        countdown(x-1)
countdown(12)

#2
def printreturn(x):
    print(x[0])
    return x[1]
printreturn([1,2])

#3
def First_Plus_Length(Inputlist):
    for i in range(len(Inputlist)):
        value = len(Inputlist) + Inputlist[0]
        return value
print(First_Plus_Length([1,2,3,4,5]))

#4
def values_greater_than_second(list):
    newlist= []
    for i in range(len(list)):
        if list[i]> list[1]:
            newlist.append(list[i])
    print(len(newlist))
    if len(newlist)<= 2:
        return False
    return newlist
print(values_greater_than_second([5,2,3,2,1,4]))

#5
def This_Length_That_Value(length,value):
    newlist=[]
    for i in range(length):
        newlist.append(value)
    return newlist
print(This_Length_That_Value(4,7))

#1
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
print(x)
students[0]['last_name']='Bryant'
print(students)
sports_directory['soccer'][0]= 'Andres'
print(sports_directory)
z[0]['y']=30
print(z)

#2 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(x):
    for i in range(len(students)):
        names= "first_name - "+students[i]['first_name']+", last_name - "+students[i]['last_name']
        print(names)
    return names
iterateDictionary(students)


# bonus to get them to appear exactly as below!)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel

#3
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary2(key_list,some_list):
    for i in range(len(some_list)):
        first_name= students[i]['first_name']
        last_name= students[i]['last_name']
        if key_list == 'first_name':
            print(first_name)
        elif key_list=='last_name':
            print(last_name)
    return ''
print(iterateDictionary2('first_name',students))
print(iterateDictionary2('last_name',students))

#4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    count = 0
    count2 = 0
    L = "LOCATIONS"
    I = "INSTRUCTORS"
    for i in range(len(some_dict['locations'])):
        count += 1
        print(dojo['locations'][i])
    print("{} ".format(count)+ L)
    print("\n")
    for i in range(len(some_dict['instructors'])):
        count2 += 1
        print(dojo['instructors'][i])
    print("{} ".format(count2)+ I)
    return ''
print(printInfo(dojo))

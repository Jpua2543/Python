x = [ [5,2,3], [10,8,9] ] 
x[1][0]=15
print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students [0] ["last_name"] = "Bryant"
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory["soccer"][0] = "Andres"
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = [30]
print(z)


#v 1
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(list):
    for i in list:
        print(i['first_name']+" "+['last_name'])
iterateDictionary(students)


#v 2
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary2(keyname,list):
    for i in list:
        print(i[keyname])
iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)



# dojo ={
# 'locations':
# ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
# 'instructors':
# ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
#v1
# def printinfo(dojo):
#     for i, name in dojo.item():
#         print("---")
#         print(f"{len(name)} {i.upper()}")
#         for i in range (0, len(name)):
#             print(name(i))
# #printInfo(dojo)
#v2
# def printinfo(dojo,list):
#     for i in list:
#         print(i[dojo])
# printinfo('locations',dojo)
# printinfo('instructors',dojo)

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

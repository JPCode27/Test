d = {'mykey':345}

print(345 in d.keys())


#-------Min

mylist = [10,20,30,40,100]

print(min(mylist))
print(max(mylist))

#-------------------
 from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9]
shuffle(mylist)   # random_list = shuffle(mylist) not going to work as it does not return anything
print(mylist)

#--------------------Ggrabing random Integer

from random import randint

print(randint(0,100))

#or

mynum = randint(0,10)
print(mynum)
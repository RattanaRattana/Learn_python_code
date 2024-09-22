# learn basic python code

import numpy as np

mylist1 = [1,2,5]
mylist2 = [3,3,4]
ar1 = np.array([1,2,3])
ar2 = np.array([3,4,5])

# print("the value in mylist1 are")
# print(mylist1)
# print("the value in ar1 are")
# print(ar1)

hstack = np.hstack((mylist1,mylist1))
# print("the value in hstack are")
# print(hstack)

vstack = np.vstack((mylist1,mylist1,ar1,ar2))
# print("the value in vstack are")
# print(vstack)

item = mylist1[1]
# print("the value in item[1] is")
# print(item)

item1 = [vstack[0,0],vstack[1,1]]
# print("the value in item1 are")
# print(item1)

#size = np.size(vstack) # size is equal to total elements in vstack
size = np.size(vstack,0) # give a size on row along axis 0 is x axis
#size = np.size(vstack,1) # give a size on column along axis 1 is y axis

# print("size of vstack is")
# print(size)

shape = np.shape(vstack)
# print("shape of vstack are")
# print(shape)

len = len(vstack)
# print("length of vstack are")
# print(len)

# print("i is equal to :")
# for i in ar1:
#     print(i)

# print("5 is in ar1 or not")
# if 5 in ar1:  
#     print("yes")
# else:
#     print("no")

# print("value in mylist1 :") 
# print(mylist1)
# mylist1.append(2)
# # we only can append value to list. for array we cannot.
# print(mylist1)

i = 0
while not (i == 3): # if i equal to 3 it stop
    mylist1.append(i)
    i += 1
    
# print(mylist1)
# print(np.shape(mylist1))
## build matrix 4 by 3 (row by column)
ar3 = np.array([[1,2,3],[4,5,6],[6,7,8],[9,10,11]])
## build matrix 3 by 1
ar4 = np.array([[1],[2],[3]])
#print(ar4)
A=2
ar5 = np.matmul(ar3,ar4)
ar6 = np.dot(ar3,A)
ar7 = np.multiply(ar3,A)
ar8 = np.transpose(ar7)
#print(np.size(ar4,0))
#ma = np.zeros((4,3))
print(ar5)
print(np.shape(ar5))

print(ar6)
print(np.shape(ar6))

print(ar6)
print(np.shape(ar6))

print(ar8)
print(np.shape(ar8))
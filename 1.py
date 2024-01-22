# import numpy as np

# a=np.array([1,2,3,45,78])
# print(a)

# a=np.arange(1,7)
# print(a)
# print(a.shape)

# b=a.reshape(6,1)
# print(b)
# b=a[np.newaxis,:]
# print(b)

# a=np.array([[1,2],[3,4]])
# b=np.array([[5,6]])
# c=np.concatenate((a,b),axis=None)
# print(c)


# a=np.array([1,2,3,4])
# b=np.array([5,6,7,8])

# c=np.hstack((a,b))  #hstack,vstack
# print(c) 


# x=np.array([[1,2,3],[4,5,6],[1,2,3],[4,5,6]])
# a=np.array([1,0,1])

# y=x+a #broadcasting
# print(y)


# a=np.array([[7,8,9,10,11,12,13],[17,18,19,20,21,22,23]])
# print(a)
# print(a.sum(axis=None))
# print(a.std(axis=None)) #we can use 0,1 instead of None for column and for rows
# print(a.var(axis=None))
# print(a.mean(axis=None))

# print(np.max(a,axis=0))

#a=np.array([1,2,3])
 
# b=a
# b[0]=42
# print(a)
# print(b) #both print same important

#if we want to make copy

# c=a.copy()
# c[0]=89
# print(a)
# print(c)


# a=np.zeros([2,3])
# b=np.ones((2,3))
# print(a)
# print(b)

# a=np.full((2,3),9) #array filled with 9 
# print(a)

# a=np.eye(3)
# print(a) #identity matrix

# a=np.arange(20)
# print(a)      #print number from 1 to 19


# a=np.linspace(0,10,5)
# print(a)  #get 5 values and all numbers are equally spaced

# a=np.random.random((3,2)) #generate 0-1 random numbers
# print(a)

# a=np.random.randn(1000)
# print(a.mean(),a.var())

# a=np.array([[2,3],[5,6]])
# eigenvalues,eigenvectors=np.linalg.eig(a)
# print(eigenvalues)
# print(eigenvectors)

# b=eigenvectors[:,0]*eigenvalues[0]
# print(b)
# c=a@ eigenvectors[:,0]
# print(b)

# print(np.allclose(b,c))


# A=np.array([[1,1],[1.5,4.0]])
# b=np.array([2200,5050])

# x=np.linalg.inv(A).dot(b)
# print(x)

# x=np.linalg.solve(A,b)
# print(x)




#import data csv file

# np.loadtxt,  no.genfromtxt

# data=np.loadtxt('spambase.csv',delimiter==",",dtype=np.float32)
# print(data)



#List ffc intermediate

# mylist=[1,2,3,45,56]
# print(mylist[::1])


# list_orig=[1,2,3,4]
# list_copy=list_orig

# list_copy.append(7)
# print(list_copy)
# print(list_orig) 
#both same copy if we want to make actual copy we can do this by copy() method


# list_orig=[1,2,3,4]
# list_copy=list_orig.copy()

# list_copy.append(7)
# print(list_copy)
# print(list_orig) 

#New method to do operation on list in one line

# mylist=[1,2,3,4,5]
# b=[i*i for i in mylist]
# print(mylist)
# print(b)

#Tuples

# mytuples=('apple',) #we have to put comma for tuples for one element
# print(mytuples)

# mytuple=("maxi","apple",90,"apple")
# print(mytuple)
# mytuple[0]='banana' #this is invalid coz tuples is imutable
# print(mytuple)

# for i in mytuple:
#   print(i)

# if "apple" in mytuple:
#     print("yes")

# else:
#     print("No")

# print(mytuple.count("apple"))


# mytuple=(1,2,3,4,5,6,7,8)

# a=mytuple[2:5:2]
# print(a)


# mytuple=(1,2,3,4,5)
# i1,*i2,i3=mytuple i2 return [2,3,4]
 # print(i1)
# print(i2)
# print(i3)

#Dictionary

#mydict={"name":"max","age":18, "gender":'M'}
# print(mydict)

# mydict2=dict(name="Marry",age=41,gender='F')
# print(mydict2)

# my_set_3 = set("aaabbbcccdddeeeeeffff")  this returns different elements of the string
# print(my_set_3)

#union and intersection functions also present
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}


u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)

i = evens.intersection(primes)
print(i)





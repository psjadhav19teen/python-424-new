#set- it is collection of different data elements enclosed 
#within {,,,} and it is not sequence means unorder thats why no indexing,
#and no slicing but it is mutable

#empty set
# set1={}
# print(set1,type(set1))
# s=set()
# print(s,type(s))
# s1={12,"hello",True,None,56j,67.89}
# print(s1,type(s1))

# s2={{1,2,3},4,5,6} #set inside set not allowed
# x={1,100,2,500}
# print(x)
# y={200,3,2,3,4,44,5,6,4,5}
# print(y) #shows elements without repeatation
# print(y[0]) #TypeError: 'set' object is not subscriptable

#operators
# a={1,2,3}
# b={3,4}
# c={2,3}
# #print(a+b) #TypeError: unsupported operand type(s) for +: 'set' and 'set'
# print(a-b)# {1,2} shows a's elements which are not in b
# print(a>b) #False a is not superset of b
# print(a>c) #True a is superset of c
# print(c in a) #False
# print(3 in a) #True

#set operations method union(),intersection(),difference(),
#symmetric_difference()

m={1,2,3,4}
n={2,4,5,6}
print("m=",m)
print("n=",n)
print("union of m and n=",m.union(n))
print("union of n and m=",n.union(m))
print("union of m and n=",m|n)

print("intersection of m and n=",m.intersection(n))
print("intersection of n and m=",n.intersection(m))
print("intersection of m and n=",m&n)

print("difference of m and n=",m.difference(n))
print("difference of n and m=",n.difference(m))
print("difference of m and n=",m-n)

print("symmetric difference of m and n=",m.symmetric_difference(n))
print("symmetric difference of n and m=",n.symmetric_difference(m))
print("symmetric difference of m and n=",m^n)
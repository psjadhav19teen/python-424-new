#tuple:collection different data elements enclosed into () parenthesis
#it is sequence,index follows,ordered but it is immutable means can't do CRUD operation

#create tuple
tup=()
print(tup,type(tup)) #() <class 'tuple'>
t1=tuple()
print(t1,type(t1)) #() <class 'tuple'>

t2=(500)
print(t2,type(t2)) #500 <class 'int'>

t3=(500,100,"hello",True,5j,89.8789)
print(t3,type(t3)) # (500, 100, 'hello', True, 5j, 89.8789) <class 'tuple'>

# t4=tuple(78,89,90) #error
t4=tuple((78,89,90))
print(t4,type(t4)) #(78, 89, 90) <class 'tuple'>

my_tuple=(3,45,64,6764,34,100)
print(my_tuple)

#index
print("first element=",my_tuple[0])
print("last element=",my_tuple[-1])

#slicing
print(my_tuple[::-1]) #(100, 34, 6764, 64, 45, 3)
print(my_tuple[2:5])#(100, 34, 6764, 64, 45, 3)

#operation
tuple1=(1,2,3)
tuple2=(4,5,6)
print(tuple1+tuple2)
#print(tuple1+100) #TypeError: can only concatenate tuple (not "int") to tuple

#tuple function
tuple3=(1,5,4,2,3)
print(tuple3) #(1, 5, 4, 2, 3)
print(sorted(tuple3)) #[1, 2, 3, 4, 5]
print(sorted(tuple3)[::-1])  #[5, 4, 3, 2, 1]
print(sorted(tuple3,reverse=True))

#tuple method-index(),count()
tuple4=("hello","red","orange","green",1000,300,700)
# print(tuple4.index(3)) #if element not present then ValueError
print(tuple4.index(300)) #5
print(tuple4.count(300)) #1

#immutability
#tuple4[0]="welcome"#TypeError: 'tuple' object does not support item assignment
print(tuple4)


#traversing of tuple
my_tup=(100,200,300,400,1,2,3)
# for i in my_tup:
#     print(i)

#reverse
# for i in my_tup[::-1]:
#     print(i)

#ascending
# for i in sorted(my_tup):
#     print(i)

# #descending
# for i in sorted(my_tup)[::-1]:
#     print(i)
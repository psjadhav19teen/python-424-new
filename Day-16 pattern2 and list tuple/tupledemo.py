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

t4=tuple(78,89,90) #error
t4=tuple((78,89,90))
print(t4,type(t4)) #(78, 89, 90) <class 'tuple'>
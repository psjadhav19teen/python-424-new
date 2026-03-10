#list:collection different data elements enclosed into [] 
#it is sequence,index follows,ordered and it is mutable means it can do CRUD operation

#create list
list1=[]
print(list1,type(list1)) #[] <class 'list'>
list2=[100]
print(list2,type(list2)) #[] <class 'list'>
list3=["hello",100,True,100j,None,(100,200)]
print(list3,type(list3)) #['hello', 100, True, 100j, None, (100, 200)] <class 'list'>

#index
print(list3[0])#hello
print(list3[-1]) #(100,200)

#mutable
list3[-1]=55555
print(list3)
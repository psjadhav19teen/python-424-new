#set-issuperst(),issubset(),isdisjoint(),union(),difference(),intersection()
#symmetric_difference()

# x={6,89,45,34,90}
# print(x)

# #add elements
# # print(x[-1]) #no index follows
# x.add(100)#adds new element in anywhere
# print(x)
# x.add(90) #not added but no error because set shows without repeatation
# print(x)

# # x.add(11,22) #TypeError: set.add() takes exactly one argument (2 given)
# #x.add([11,22]) #TypeError: unhashable type: 'list'
# # x.add([11],[12]) #Error
# x.add((11,12))
# print(x)
# y={1,2}
# x.update(y)
# print(x)

# colors={"red","green","pink","orange"}
# print(colors) #{'red', 'orange', 'green', 'pink'}

# #WAP to change red color to light_red
# colors_new=list(colors)
# print(colors_new) #['red', 'orange', 'green', 'pink']
# i=colors_new.index("red")
# colors_new[i]="light_red"
# print(colors_new) #['light_red', 'orange', 'green', 'pink']
# colors_new1=set(colors_new)
# print(colors_new1) #{'light_red', 'orange', 'green', 'pink'}


#WAP to show give unique elements from below given list
# mylist=[12,12,45,23,78,45,1,1,1]
# print(mylist)
# new_list=list(set(mylist))
# print(new_list)

#OR using for loop
# new_mylist=[]
# for i in mylist:
#     if i not in new_mylist:
#         new_mylist.append(i)

# print(new_mylist)


#WAP to create myset and add number elements as entered count
# myset=set()
# print(myset,type(myset))
# count=int(input("Enter count for numbers="))
# for i in range(count):
#     number=int(input(f"enter {i+1} number="))
#     myset.add(number)
# print(myset)

#set Comprehension
#{output for iterable_variable in sequence_object if condition}
# count=int(input("Enter count for numbers="))
# myset1={int(input(f"enter {i+1} number=")) for i in range(count)}
# print(myset1)


#WAP to print 10 to 1 in set using comprehension
# print({i for i in range(10,0,-1)}) #{1,2,..10}can't follow sequence
# print([i for i in range(10,0,-1)]) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# x={12,-324,56,343,-5,35}
# WAP to show only +ve numbers from above set use comprehension
# print({i for i in x if i>0})


#WAP to show sum of elements of below list use loop
mylist=[12,3,4,5,11]
sum=0
for i in mylist:
    sum+=i
print(sum)

#WAP to show cube of above elements
print([i**3 for i in mylist])
# print({i**3 for i in mylist}) #do not use this because sequence not followed
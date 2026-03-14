#WAP to arrange below elements into ascending order
# mylist=[12,35,45,34,67,18,12]
# print(mylist)
# for i in range(len(mylist)): #0 1 2 3 4 5 6
#     for j in range(0,len(mylist)-i-1):
#         if mylist[j]>mylist[j+1]:
#             mylist[j],mylist[j+1]=mylist[j+1],mylist[j] #a,b=b,a
# print(mylist)

# #i=0
# #1) 12 >35 no change [12,35,45,34,67,18,12]
# #2) 35>45 no change[12,35,45,34,67,18,12]
# #3) 45>34 change[12,35,34,45,67,18,12]
# #4) 45>67 no change [12,35,34,45,67,18,12]
# #5) 67>18 change [12,35,34,45,18,67,12]
# #6) 67>12 change [12,35,34,45,18,12,67]
# #i=1
# # 12>35 no change [12,35,34,45,18,12,67]
# #35>34 change [12,34,35,45,18,12,67]

# #Second Highest
# print(mylist[-2]) #45

# #Second lowest
# print(mylist[1]) #12


#Q.10 Write a program to find the most frequently occurring element
# mylist=[12,35,45,34,67,18,12,18,35,35]
# print(mylist)
# newlist=[] #without duplicate
# duplicate_list=[]

# for i in mylist:
#     if i not in newlist:
#         newlist.append(i)
#     else:
#         duplicate_list.append(i)

# print(newlist) #[12, 35, 45, 34, 67, 18]
# print(duplicate_list)#[12, 18, 35, 35]
# print(duplicate_list[::-1]) #[35, 35, 18, 12]
# print(set(duplicate_list)) #{18, 35, 12}

#earlier one basic use below logic
# mylist=[12,35,45,34,67,18,12,18,35,35]
# print(mylist)
# newlist=list(set(mylist))
# print(newlist)
# most_frequent=None
# max_count=0
# for i in newlist:
#     count=mylist.count(i)
#     if count>max_count:
#         max_count=count
#         most_frequent=i

# print(f"The most frequent number is {most_frequent}, apprearing {max_count} times.")

#OR
from collections import Counter
mylist=[12,35,45,34,67,18,12,18,35,35]
print(mylist)
counts=Counter(mylist)
print(counts.most_common(1))

students=[["id","name","grade"],[1,"Ravi","O"],[2,"Mitesh","A+"]]
print(students)
# print(students[0])
# print(students[1])
# print(students[2])
# for i in students:
#     print(i)

#Find student name and grade whoes id is 2
# print("Student id 2 name is=",students[2][1])
# print("Student id 2 grade is=",students[2][2])

#Find student name and grade by entering student id
# id=int(input("enter student id to find name and grade="))
# flag=False  
# for i in students:
#     if i[0]==id:
#         flag=True
#         print("ID=",i[0])
#         print("Name=",i[1])
#         print("Grade=",i[2])

# if flag==False:
#     print("id not found. Try again!!")

#OR
id=int(input("enter student id to find name and grade="))
for i in students:
    if i[0]==id:
        print("ID=",i[0])
        print("Name=",i[1])
        print("Grade=",i[2])
        break
else:
    print("id not found. Try again!!")
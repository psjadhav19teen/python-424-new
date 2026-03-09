# for i in range(3):
#     print("*")


# for i in range(3):
#     print("*",end="")


# for i in range(3):
#     for j in range(3):
#         print("*",end="")
#     print()


# for i in range(3):
#     for j in range(3):
#         print(i,end="")
#     print()


# for i in range(3):
#     for j in range(3):
#         print(j,end="")
#     print()


# row=int(input("enter row count="))
# column=int(input("enter column count="))
# for i in range(row):
#     for j in range(column):
#         print("*",end="")
#     print()

# row=int(input("enter row count="))
# column=int(input("enter column count="))
# for i in range(row):
#     for j in range(column):
#         if i==j:
#             print("1",end="")
#         else:
#             print("0",end="")
#     print()


#Left-incremental Triangle
count=int(input("enter row count="))
for i in range(count):
    for j in range(i+1):
        print("*",end="")
    print()

count=int(input("enter row count="))
for i in range(count):
    for j in range(i+1):
        print(i,end="")
    print()

count=int(input("enter row count="))
for i in range(count):
    for j in range(i+1):
        print(j,end="")
    print()

count=int(input("enter row count="))
n=1
for i in range(count):
    for j in range(i+1):
        print(n,end="")
        n+=1
    print()
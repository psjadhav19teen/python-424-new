# Left incremental pyramid
# count=int(input("enter row count="))
# for i in range(count):
#     for j in range(i+1):
#         print("*",end="")
#     print()
"""
*
**
***
"""

# Left decremental pyramid
# count=int(input("enter row count="))
# for i in range(count):
#     for j in range(count,i,-1):
#         print("*",end="")
#     print()
"""
***
**
*
"""

# Right incremental pyramid
count=int(input("enter row count="))
for i in range(count):
    for k in range(count,i+1,-1):
        print(end=" ")

    for j in range(i+1):
        print("*",end="")
    print()

"""
  *
 **
***
"""

# Hill incremental pyramid
count=int(input("enter row count="))
for i in range(count):
    for k in range(count,i+1,-1):
        print(end=" ")

    for j in range(i+1):
        print("*",end=" ")
    print()

#Right decremental pyramid
count=int(input("enter row count=")) #3
for i in range(count): #i=0 i=1 i=2
    for k in range(i):
        print(end=" ")

    for j in range(count,i,-1):
        print("*",end="")

    print()

#Hill-decremental pyramid
count=int(input("enter row count="))
for i in range(count):
    for k in range(i):
        print(end=" ")

    for j in range(count,i,-1):
        print("*",end=" ")

    print()
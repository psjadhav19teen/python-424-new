#methods
# x={1,2,3,4}
# y={2,4,5,6}
# z={1,2}
# p={11,12}
# print(x)
# print(y)
# print(z)
# print(x.issuperset(z))#True
# print(x>z) #True
# print(z.issubset(x))#True
# print(z>x) #False
# print(x.isdisjoint(y))#False
# print(x.isdisjoint(p))#True

#traversing set
myset={13,45,243,56,12,12,13}
print(len(myset))#5 without repeatation
for i in myset:
    print(i)
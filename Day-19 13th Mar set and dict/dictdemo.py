#dict:-collection of element represented into key,value pair enclosed with {k:v}
#It follows key indexing and key order and no slicing and it is mutable

#create empty dictionary
# d={}
# print(d,type(d))
# d1=dict()
# print(d1,type(d1))

# d1={1:1000,2:2000,3:3000,4:4000}
# print(d1)

# #student details
# d2={"rollno":101,"name":"pooja","grade":"A+"}
# print(d2)
# d3={"subjects":["py","js","html","css"]}
# print(d3)
# #d4={[1,2,3]:[1,4,9]} #error
# d4={(1,2,3):[1,4,9]}
# print(d4)
# d5={(1,2,3):"rahul"}
# print(d5)

# #no operation and no slicing

# #key index
# print(d2["name"])
# print(d3["subjects"])
# print(len(d3))#1 keys
# print(len(d2))#3 keys

#CRUD operation on empty dict without using method
books={}
print(books)
books["isbn"]=1111
print(books) #{'isbn': 1111}
books["isbn"]=5555 #it update the previous isbn value
print(books) #{'isbn': 5555}
books['title']="python"
books['author']="rossom"
books["price"]=899
print(books)#{'isbn': 5555, 'title': 'python', 'author': 'rossom', 'price': 899}
books["dop","qty"]="12-04-2000",20
print(books) #{'isbn': 5555, 'title': 'python', 'author': 'rossom', 'price': 899, ('dop', 'qty'): ('12-04-2000', 20)}

#change price to 900
books["price"]=900
print(books)

#show book title and price
print(books["title"],books["price"])

#delete author
del books["author"]
print(books)
#dictionary methods
products={}
print(products,type(products))

#new element add and existing element update by using update()
# products.update({'id':1001})
# print(products)

# products.update({'name':'mobo124','category':'mobile','price':30000})
# print(products)

# products.update({'price':50000})
# print(products)
# #remove specified key-value pair
# products.pop("price")
# print(products)

# #remove last key-value pair
# products.popitem()
# print(products)

# # products.pop("price") #KeyError: 'price' if not exists
# # print(products)

# #remove key-value pair by using del
# del products["name"]
# print(products)

# products.clear() #removes all elements
# print(products)

#get(),keys(),values(),items()
students={"id":101,"name":"rohit","grade":"A+"}
print(students.keys()) #dict_keys(['id', 'name', 'grade'])
print(students.values()) #dict_values([101, 'rohit', 'A+'])
print(students.get("name"))#rohit
print(students.items()) #dict_items([('id', 101), ('name', 'rohit'), ('grade', 'A+')])


#setdefault()
sem=students.setdefault("semester",6)
print(sem)#6
print(students)#{'id': 101, 'name': 'rohit', 'grade': 'A+', 'semester': 6}
students.update({"semester":8})
print(students)#{'id': 101, 'name': 'rohit', 'grade': 'A+', 'semester': 8}
print(sem) #6

#fromkeys()
names=["dhiraj","neha","akshay","kapil"]
location="malad"
names_dict=dict.fromkeys(names,location)
print(names_dict)

student1=students.copy()
print(student1)

names_dict=students.copy()
print(names_dict)

#update(),pop(),pop_item(),clear(),copy(),
# get(),keys(),vlaues(),items(),setdeafault(),fromkeys()
fruits=["apple","grapes","banana","kiwi","watermelon"]
print(fruits)
fruits.reverse() #['watermelon', 'kiwi', 'banana', 'grapes', 'apple']
print(fruits)
fruits.sort()
print(fruits) #['apple', 'banana', 'grapes', 'kiwi', 'watermelon']

price=[200,300,100,500]
fruits.extend(price) #['apple', 'banana', 'grapes', 'kiwi', 'watermelon', 200, 300, 100, 500]
print(fruits)
print(fruits.count("apple")) #1
x=[1,2,3]
print(x) #[1, 2, 3]
x=fruits.copy()
print(x) #['apple', 'banana', 'grapes', 'kiwi', 'watermelon', 200, 300, 100, 500]
x.clear()
print(x) #[]
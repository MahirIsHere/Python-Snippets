import random
print(random.randint(3, 9))

list = ["r","a","s","n","o"]
random.shuffle(list)
print(list)

#weight highest number more probability
#k chooses number of elements
chicklist=["r","a","s","n","o"]
x=random.choices(chicklist,weights=(10,20,30,40,50),k=5)
print(x)
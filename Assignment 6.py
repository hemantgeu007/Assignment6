"""Q1"""
for i in range(0,10) :
    n = int(input("Enter an Integer: "))
    print("you entered: " , n)

"""Q2"""
while True :
    print("This is an Infinite Loop. ")

"""Q3"""
l = []
limit = int(input('Enter number of elements: '))
print("Enter the list")
for i in range(0 , limit):
    listItem = int(input())
    l.append(listItem)
print(l)
sqlist = []
for i in range(0,limit):
    sqlistitem = l[i] * l[i]
    sqlist.append(sqlistitem)
print(sqlist)

"""Q4"""
l2 = [4,'a', 'b', 'c', 1.6, 'd', 3]
intlist = [x for x in l2 if isinstance(x , int)]
strlist = [x for x in l2 if isinstance(x , str)]
floatlist = [x for x in l2 if isinstance(x , float)]
print(intlist)
print(strlist)
print(floatlist)

"""Q5"""
even = []
odd = []
for j in range(1 , 101):
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("The even list",even)
print("The odd list",odd)

"""Q6"""
for i in range(0, 4):
    for j in range(0, i + 1):
        print("* ", end="")
    print("\r")

"""Q7"""
dictionary = {'Hemant' : 20, 'Himanshu' : 20, 'Anant' : 21 , 'Nikhil' : 23}
search_age = int(input("Provide age: "))
for name, age in dictionary.items():
    if age == search_age:
        print(name)

"""Q8"""
l3 = []
limit = int(input('Enter number of elements: '))
print("Enter the list")
for i in range(0 , limit):
    listItem = input()
    l3.append(listItem)
print(l3)
check = input("Enter the item you want to search for: ")
for i in range(0 , limit):
    if check in l3:
        l3.remove(check)
print(l3)
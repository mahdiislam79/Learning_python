#Loops
count = 0
while count < 20: #while loop
    print(count)
    count +=1

#using loop to iterate a list

items = [1,2,3,4]
for item in items:
    print(f"item number{item}")
    
#using loop for a specific amount of times 
for i in range(5):
    print(i)
#using enumerate and loop to get access of a tuple containng both index and value of a list

l = ['a','b','c','d']
for a in enumerate(l):
    print(l)

#using loop to get access of index in a list 
for index, value in enumerate(l):
    print(index, value)
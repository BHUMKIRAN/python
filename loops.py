#while loop 
#for loop 

a=1;

# while (a>0 and a<100):
#     a += 1
#     print(a)

#using break to stop the loop 

while (a>0):
    a += 1
    if a==50:
        break
    print(a)

#using continue to run the other statment 

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

c=list([1,2,3,4,5,6,7,8,9,10])

for i in c:
    print(i)

for i in range(1,20):
    print(i)

fruits = tuple(("apple", "banana", "cherry", "orange", "kiwi", "mango"))

for i in fruits:
    if i=="orange":
        break
    print(i)

for i in fruits:
    if i=="orange":
        continue
    print(i)


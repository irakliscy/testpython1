import random
import math as m
n= int(input("Give a num"))
# protoi dio arithmi fabo
ar, ar2 = 0, 1
count = 0

if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(ar)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(ar)
        nth = ar + ar2
        ar = ar2
        ar2 = nth
        count += 1
p=nth
x=0
b=0
for x in range(20):
    a = random.randint(1, 1000000)
    if (a**ar2) % ar2 == a % ar2:
        b=1
    else:
        b=0


if b==1:
    print (n,"ος όρος είναι ο ",p," και είναι πρώτος.")
elif b==0:
    print (n,"ος όρος είναι ο ",p," και δεν είναι πρώτος.")


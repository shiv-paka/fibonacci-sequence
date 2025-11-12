#Fibonacci Sequence
n=int(input("Enter the number of digits of the fibonacci sequence: "))
a=0
i=1
print(a)
print(i)
for j in range(1,n-1):
    c=a+i
    a=i
    i=c
    print(c)


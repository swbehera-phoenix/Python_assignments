import math

def is_armstrong(num):
    l=len(str(num))
    sum = 0
    temp = num
    while temp>0:
        mod = temp%10
        sum = sum + math.pow(mod,l)
        temp=temp//10

    return sum == num

print("Enter a range")
n1=int(input("Start: "))
n2=int(input("End: "))

armstrong_list = []
for i in range(n1,n2+1):
    if is_armstrong(i):
        armstrong_list.append(i)

print(armstrong_list)
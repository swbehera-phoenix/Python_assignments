even_list=[]
odd_list=[]
print("Enter Start and End Range")
n1=int(input("Start: "))
n2=int(input("End: "))
for i in range(n1,n2+1):
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("List of Even Numbers: ",even_list)
print("List of Odd Numbers: ",odd_list)
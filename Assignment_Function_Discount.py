discount = 10

def display(id, name, price, quantity):
    print("Product ID: ",id )
    print("Product Name: ",name )
    print("quantity: ",quantity )

    def calculate(quantity):
        global discount
        return  (quantity*price)*(1-(discount)/100)
    
    print("Total Price:", calculate(quantity))
    return 0

i=input("Enter Product ID:")
n=input("Enter Product Name:")
q=int(input("Enter quantity: "))
p=float(input("Enter price of each: "))

display(i, n, p, q)
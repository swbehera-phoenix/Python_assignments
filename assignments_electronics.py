class Product:
    def __init__(self, name, price, brand, warranty):
        self.name = name
        self.price = price
        self.brand = brand
        self.warranty = warranty

    def display(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Brand: {self.brand}")

    def calc_price(self,count):
        self.count = count
        print(f"Total Price: {self.price*self.count}") 


class Electronics(Product):
    def __init__(self, name, price, brand, warranty, type):
        super().__init__(name, price, brand, warranty)
        self.type = type
    
    def displayAlldetails(self):
        super().display()
        print(f"Type: {self.type}")
        super().calc_price(self.count)

Fan = Electronics("Fan 1", 1500, "Khaitan", 5, "Fan")
Fan.count = 100
Fan.displayAlldetails()   
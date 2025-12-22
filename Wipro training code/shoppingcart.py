class shoppingcart(): 
    def __init__(self,cart_id): 
        self.cart_id = cart_id 
        self.products = { }             
    def add_products(self,product,price): 
        self.products[product] = price 
        print(product , "added to the cart") 
 
    def remove_products(self,product): 
         if product in self.products: 
             del self.products[product] 
             print(product,"removed from cart") 
         else: 
             print(product, "not found in cart") 
 
    def calculate_total(self): 
        total = sum(self.products.values()) 
        return total 
     
cart1 = shoppingcart(10) 
cart1.add_products("mouse",300) 
cart1.add_products("keyboard",3000) 
cart1.add_products("laptop",70000) 
 
cart1.remove_products("keyboard") 
 
total_price = cart1.calculate_total() 
print("total price of products:",total_price) 
 

products={
    {
    "name":"Apple",
    "price":50000,
    "number":5
    }
}
def get_product_by_name_or_return_none(product_name):
    global products
    for i in products:
        if i ["name"]==product_name:
            return i
        return None
        
def buy(product_name,product_number):
    global products
    if product_name in products and products[product_name]>=[product_number]:
        products[product_name]=[product_number]
        print("the number of product is enough:")
    else:
        print("the number of product is not enough:")
    pass


def delete(product_name):
    global products
    if product_name in products:
        del products[product_name]
        print("the product deleted from shop:")
    else:
        print(" the product not found:")
    pass

def add(product_name,product_number, product_price):
    global products 
    products[product_name]=[product_number]=[product_price]
    print("the product to name and price and number added in shop:")
    pass

def change(product_name, new_number, new_price):
        global products 
        if product_name in products:
            products[product_name]=[new_number]
            products[product_name]=[new_price]
            print("the product changed with new number and new price:")
            pass
        else:
            print("the product is not in the shop:")
            
def main():
            for name in range(10):
                print("add,delete,change,buy")
                direction=input("enter direction:").strip().lower()
                
                if direction=="add":
                    product_name=input("enter product name:").strip()
                    product_number=int(input("enter product number:"))
                    product_price=float(input("enter product price:")) 
                    add (product_name,product_number,product_price) 
                    
                elif direction=="delete":
                    product_name=input("enter product name:")
                    delete(product_name)
            
                elif direction=="change":
                    product_name=input("enter product name:")
                    product_price=float(input("enter new price:"))
                    product_number=int(input("enter new number:"))
                    change(product_name,product_price,product_number)
            
                
                elif direction =="buy":
                    product_name=input("enter product name:")
                    product_number=int(input("enter product number:"))
                    buy(product_name,product_number)
                else:
                    print(" the direction empty:")  
            pass    
if __name__== "__main__":
    main()
                
# Creating the class:

import tabulate

class Shoes():

    """
        The function takes in the country, code, product, cost, and quantity of an item and returns the
        value of the item
        
        :param country: The country where the order was placed
        :param code: The code of the product
        :param product: The name of the product
        :param cost: The cost of the item
        :param quantity: The number of items purchased
        """
    def __init__(self,country,code,product,cost,quantity):
        
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)

        self.value_of_item = self.cost * self.quantity

    def __repr__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"

   
    def get_country(self):
        return self.country

    def get_code(self):
        return self.code

    def get_product(self):
        return self.product

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def set_price(self,new_cost):
        self.cost = new_cost

    def set_quantity(self,new_quantity):
        self.quantity = new_quantity

    def get_value(self):
        return self.value_of_item

    # Function to read inventory.txt file and creating Shoe objects
    def read_shoes_data(self):
            
# Try-except block to handle file error
        try:

# Open file inventory.txt and read the data and create shoe object.
            infile = open("inventory.txt", 'r')

# Iterate through file and create keys variable.
            keys = next(infile).strip().split(",")
            

# Read lines in text file store within dictionary "self.products".
            for line in infile:
                self.product.append(dict(zip(keys, line.strip().split(","))))


# Error message if file does not exist. 
        except FileNotFoundError:
            print("Text file not found.")
# Function to search for shoe in shoe list using shoe code and print object. 


# Function to determine shoe with highest quantity and print shoe as "On Sale".
    def highest_qty(self):
        highest_quantity = None
        highest_product = None
        for products in self.product:
            if highest_quantity is None or int(products["Quantity"]) > highest_quantity:
                highest_quantity = int(products["Quantity"])
                highest_product = products

# If highest_product does not equal none, print to user and ask user and mark as sale.
        if highest_product != None:
            print("Code: ",(highest_product["Code"]))
            print("Product: ",(highest_product["Product"]))
            print("Quantity: ", (highest_product["Quantity"]))
            print("Cost: ", (highest_product["Cost"]))
            product_discount = input("Please choose a % to discount this item for sale: ")
            product_discount = int(product_discount) / 100
            highest_product["Cost"] = float(highest_product["Cost"]) * float(product_discount)
            print("Code: ",(highest_product["Code"]))
            print("Product: ",(highest_product["Product"]))
            print("Quantity: ", (highest_product["Quantity"]))
            print("SALE PRICE: ", round((highest_product["Cost"]), 2))
    
     
# Function to find the shoe with the lowest quantity, ask user to add quantity, update this in file.
    def re_stock(self):

# Set variables to none. 
        lowest_quantity = None
        lowest_product = None

# For loop to determine lowest product; shoe object with lowest quantity.
        for products in self.product:
            if lowest_quantity is None or int(products["Quantity"]) < lowest_quantity:
                lowest_quantity = int(products["Quantity"])
                lowest_product = products

# If lowest_product does not equal none, print to user and ask user to restock product.
        if lowest_product != None:
            print("Code: ",(lowest_product["Code"]))
            print("Product: ",(lowest_product["Product"]))
            print("Quantity: ", (lowest_product["Quantity"]))
            lowest_product["Quantity"] = input("Please input level to restock product to: ") 
            print("Code: ",(lowest_product["Code"]))
            print("Product: ",(lowest_product["Product"]))
            print("Quantity: ", (lowest_product["Quantity"]))
    
      
    

      

list_table =[["Country","Code","Product","Cost","Quantity"]]
    
shoes_list =[]

shoes_1 = Shoes("UK","SKU43242","Adidas 4",1500,20)
shoes_list.append(shoes_1)
shoes_2 = Shoes("USA","SKU76578","Nike Pro",1900,25)
shoes_list.append(shoes_2)
shoes_3 = Shoes("South Africa","SKU04332","New Balance 1",1200,15)
shoes_list.append(shoes_3)
shoes_4 = Shoes("South Africa","SKU90688","New Balance 5",1300,20)
shoes_list.append(shoes_4)
shoes_5 = Shoes("UK","SKU43244","Adidas hightop",1950,20)
shoes_list.append(shoes_5)

def search_shoe(shoes_list):
    search = input("Please input SKU: ")
    index = shoes_list[0]
    for index in shoes_list:
        
        if search == index[1]:
           print(f"""
    Shoe code:        {index[1]}
    Shoe name:        {index[2]}
    Shoe price:       {index[3]}
    Shoe quantity:    {index[4]}
    
    """)
        else:
            print("SKU does not exist")


def table_display(shoes_list):
    for shoes in shoes_list:
        country = shoes.get_country()
        code = shoes.get_code()
        product = shoes.get_product()
        cost = shoes.get_cost()
        quantity = shoes.get_quantity()
        value_of_item = shoes.get_value_of_item()
    temp_list =[country,code, product,f'R{cost}',quantity,f'{value_of_item}']
    list_table.append(temp_list)

    print(tabulate(list_table, headers= "firstrow"))
    menu()

while True:
    menu =input("""\t\t\tShoe Factory Inventory System

\t\t\tMain Menu

View\t\t - View stock on hand.
Restock\t\t - Find product with lowest stock and replenish.
Item search\t - Search for specific product.
Sale item\t - Find product with highest quantity and markdown price.
Tabulate\t - View in a table format.
Quit\t\t - Exit Inventory system.\n""").lower()

    for list in shoes_list:
        
# Call function view_all.
        if menu == "view":
            list.read_shoes_data()
        

# Call function re_stock.
        elif menu == "restock":
            list.re_stock()

# Call function search_shoe
        elif menu == "item search":
            list.search_shoe()
        
# Call function highest_qty.
        elif menu == "sale item":
            list.highest_qty()

        elif menu == "tabulate":
            list.table_display()

# Exit program.
        elif menu == "quit":
            print("Goodbye!")
            exit()

# Error message for user when input not valid.
        else:
            print("Input not recognised, Please try again.")
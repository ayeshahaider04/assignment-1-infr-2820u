# Ayesha Haider 100869659
# Assignment 1 algorithms and data structures 

# Task 1 loading and storing product_data.txt into an array and giving the products attributes:
class Product:
    def __init__(self, ID, name, price, category):
        self.ID = ID
        self.name = name
        self.price = price
        self.category = category
    def __repr__(self):
        return f"product(ID={self.ID}, name='{self.name}', price={self.price}, category='{self.category}')"

def ReadLines(file_path):
    with open(file_path, 'r') as file:
        Lines = file.readlines()
        for line in Lines:
            print(line.strip())
    return Lines

def LoadintoArray(file_path):
    products = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  
                    ID, name, price, category = line.split(',')
                    products.append(Product(int(ID), name, float(price), category))
    except Exception as e:
        print(f"Error: {e}")
    return products

file_path = r"C:\Users\ayeha\Downloads\product_data.txt"
print("File contents:")
file_lines = ReadLines(file_path)

product_list = LoadintoArray(file_path)
print("\nInitial product list:")
for product in product_list:
    print(product)

# Task 2 data manipulation operations
#array operation update and insert:
def InsertProduct(products, InsertedProduct):
    products.append(InsertedProduct)
    print("list after inserting new product:")
    for product in products:
        print(product)
InsertedProduct = Product(6, "towel", 8.40, "Home & Kitchen")
InsertProduct(product_list, InsertedProduct)

#array operation delete:
def DeleteProduct(products, ProductName):
    for product in products:
        if product.name == ProductName:
            products.remove(product)
            print(f"product '{ProductName}' has been deleted.")
            break
    else:
        print(f"product '{ProductName}' was not found.")
DeleteProduct(product_list, "towel")

# Task 3 sorting algorithm
#array sorting method bubble sort 
def BubbleSort(products):
    n = len(products)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if products[j].price > products[j + 1].price:
                products[j], products[j + 1] = products[j + 1], products[j]

BubbleSort(product_list)
print("\nUpdated product list priced lowest to highest:")
for product in product_list:
    print(product)






class Product:
    def __init__(self):
        self.id=78
        self.name="Amul"

    def display(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")

class A(Product):
    
    def __init__(self):
        super().__init__()
        self.count=50
        self.catgory="butter"

    def display(self):
        super().display()
        print(f"Count: {self.count}")
        print(f"Category: {self.catgory}")

class B(Product):
    
    def __init__(self):
        super().__init__()
        self.count=90
        self.catgory="Milk"

    def display(self):
        super().display()
        print(f"Count: {self.count}")
        print(f"Category: {self.catgory}")

class C(Product):
    
    def __init__(self):
        super().__init__()
        self.count=56
        self.catgory="choco"

    def display(self):
        super().display()
        print(f"Count: {self.count}")
        print(f"Category: {self.catgory}")

a=A()
print("Class A Inherit Product:")
a.display()

b=B()
print("\nClass B Inherit Product:")
b.display()

c=C()
print("\nClass C Inherit Product:")
c.display()


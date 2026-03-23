class Rectangle():
    def __init__(self):
        self.length=0
        self.breadth=0
     
    def input_details(self):
        self.length=int(input("Enter the length of the rectangle: "))
        self.breadth=int(input("Enter the breadth of the rectangle: "))

class Cal(Rectangle):
    def __init__(self):
        super().__init__()
        self.perimeter=0
        self.area=0

    def peri(self):
        self.perimeter=2*(self.length+self.breadth)
        print(f"The perimeter is {self.perimeter}")
    
    def a(self):
        self.area=self.length*self.breadth
        print(f"The area is {self.area}")

rect1=Cal()
rect1.input_details()
rect1.peri()
rect1.a()
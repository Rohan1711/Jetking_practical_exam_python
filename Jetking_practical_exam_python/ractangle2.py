class Rectangle():
    def __init__(self,breadth,length):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length * self.breadth
    
a= int(input("enter the length of ractangle : "))  
b= int(input("enter the breadth of ractangle : "))   
obj = Rectangle(a,b)
print("the area of the ractangle is :",obj.area())
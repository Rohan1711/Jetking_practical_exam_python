class Printstring():
    def __init__(self):
        self.string=""

    def get(self):
        self.string=input("enter the string :")

    def show(self):
        print("the string is: ",self.string)

obj=Printstring()
obj.get()        
obj.show()
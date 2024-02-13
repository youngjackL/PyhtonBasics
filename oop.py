class Fruits:
    def __init__(self,name,price) :
        self.name=name
        self.price=price
    def onyesha(self):
        print(f"My Favourite Fruit is {self.name}"
              f"and it's cost is Ksh.{self.price}"
              
              f"It is orange in colour")

myobj=Fruits("Oranges",67)
myobj.onyesha()
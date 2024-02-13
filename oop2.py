class People:
    def __init__(self,name,age,gender) :
        self.name = name
        self.age = age
        self.gender = gender
    def onyesha(self):
        print(f"My name is {self.name} "
              f" and I am {self.age}. "

              f" I am a {self.gender}")


myobj = People("Young", 20,"Male")
myobj.onyesha()
myobj = People("John", 57,"Male")
myobj.onyesha()
myobj = People("Jane", 23,"Female")
myobj.onyesha()
myobj = People("Precious", 17,"Female")
myobj.onyesha()
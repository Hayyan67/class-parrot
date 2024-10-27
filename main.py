class Parrot:
    species='bird'
    def __int__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print('Name',self.name,'Age',self.age)

p1=('loo',8)
p1.display()
p1=('blu',12)
p1.display()
class person:

    def __init__(self,name,age):
        self.name= name
        self.age=age


    def walk(self):
     print("walk")



name=person("bilal",22)
print(name.name)
print(name.age)
name.walk()


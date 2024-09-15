class House:
    def __init__(self,name,number_of_floors):
        self.name=name
        self.number_of_floors=number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name} ,количество этажей:{self.number_of_floors}"


h1=House("ЖК Эльбрус",10)
h2=House("ЖК Акация",20)
print(h1.name,h1.number_of_floors)
print(h2.name,h2.number_of_floors)
print(h1.__str__())
print(h2.__str__())
print(h1.__len__())
print(h2.__len__())
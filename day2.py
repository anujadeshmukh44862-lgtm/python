class Anuja:
    def info(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

A=Anuja()
A.info("Anuja Deshmukh", 25)
B=Anuja()
B.info("sonam", 30)
A.display()
B.display()

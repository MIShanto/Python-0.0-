class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o
    
    def do_work(self):
        if(self.occupation == "Coding"):
            print(self.name, "is a Coder")
        elif(self.occupation == "swimming"):
            print(self.name, "is a swimmer")
        else:
            print("Occupation Unknown :( \n")

mi = Human("MI Shanto", "Coding")
mi.do_work() 
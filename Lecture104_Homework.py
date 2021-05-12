class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added to",self.name,self.lastname,"'s cart")

customer01 = Customer()
customer01.name = "Mind"
customer01.lastname = "Nate"
customer01.age = 10
customer01.addCart()

customer02 = Customer()
customer02.name = "Ink"
customer02.lastname = "Ning"
customer02.age = 12
customer02.addCart()


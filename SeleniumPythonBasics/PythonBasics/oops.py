# class = map, blueprint
class goa:
    def __init__(self, drink):
        self.drink=drink
        print(f"user need drink : {self.drink}")

    def beach(self):
        print("Enjoy the breach")

    def party(self):
        print("party")

# ram, sam ticket - object creation
ram = goa("no")
ram.beach()

sam = goa("yes")
sam.party()

# parrot - name, sing, age, speak
# laptop - name, ram, price, processor
# mobile - name, ram, price, processor
# employee - name, salary, id, age, skill
# vehicle - name, speed, price, petrol/deisel
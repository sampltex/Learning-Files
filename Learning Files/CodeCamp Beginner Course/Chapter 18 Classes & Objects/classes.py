# classes are like blueprint when we create something, and with classes you can make objects

class Vehicle: # the class is capitalized and the methods are actions
    def __init__(self, make, model): # these are the properties and it is called an inititalizer function
        self.make = make
        self.model = model
    # defining a function like below creates a method that can be used on the class of objects
    def moves(self):
        print('Moves along...')
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")
my_car = Vehicle('Tesla', 'Model 3') # my_car is an object created from the class Vehicle

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Cadillac','Escalade')
your_car.get_make_model()
your_car.moves()

class Airplane(Vehicle):
    def __init__(self, make, model,faa_id):
        super().__init__(make, model) # the super function allows Airplane to inherit the two properties from the parent class
        self.faa_id = faa_id
    def moves(self): # defining the same method that could've been obtained from the previous class is overwritten
        print('Flies along...')

class Truck(Vehicle):
    def moves(self):
        print('Rumbles along...')

class GolfCart(Vehicle):
    pass # using pass makes the class inherit everything as it is

cessna = Airplane('Cessna','Skyhawk','N-12345')
mack = Truck('Mack','Pinnacle')
ezcart = GolfCart('ezcart','GC100')

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
ezcart.get_make_model()
ezcart.moves()

print('\n\n')
# this is polymorphism which is the ability to respond differently to the same input
# so these objects are going to respond differenty even though they all are taking in the same methods
for v in (my_car, your_car, cessna, mack, ezcart):
    v.get_make_model()
    v.moves()
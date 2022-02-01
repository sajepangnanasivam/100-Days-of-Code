# *ARGS
# The asterix symbol represents ALL values given in as arguments. (Tuples)
def add(*args):
    print(f"The first number given:\t {args[0]}")
    sum = 0
    for n in args:
        sum += n
    return sum


answer = add(5, 6, 7)
print(answer)


# **KWARGS (KeyWordArguments) (Dictionary)
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(f"\nKey:\t {key}")
    #     print(f"Value:\t {value}\n")
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        # Use the get method to not bring error when an argument is missing.
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.make)
print(my_car.colour)
print(my_car.seats)

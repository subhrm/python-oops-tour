class Fruit:
    # Constructor
    # every class function needs 'self' parameter
    def __init__(self, color="white", weight=0.0, name="None"):
        self.color = color
        self.weight = weight
        self.name = name

    # all __ functions are called "dunder" functions or "Magic" functions
    # Encapsulation and Overloading
    def __str__(self) -> str:
        return f"Hello form Fruit object. My name is {self.name} and I have color {self.color}, weight : {self.weight} "

    # Encapsulation and Overloading
    def __add__(self, other):
        return Fruit(color=self.color + " " + other.color, 
                     weight=self.weight + other.weight, 
                     name=self.name + " " + other.name)


if __name__ == "__main__":
    # write module unit tests 
    print("From fruit.py")
    f1 = Fruit(name="mango", color="orange", weight=5.0)
    print(f1)

    f2 = Fruit(name="bananna", color="yellow", weight=5.0)
    print(f2)

    f3 = f1 + f2
    print(f3)

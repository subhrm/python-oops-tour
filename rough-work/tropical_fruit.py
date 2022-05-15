from fruit import Fruit

# Inheritance
class TropicalFruit(Fruit):

    def __init__(self, country="India", **kwargs):
        # Initialize parent
        super().__init__(**kwargs)
        self.country = country

    # all __ functions are called "dunder" functions or "Magic" functions
    def __str__(self) -> str:
        return f"""Hello form Fruit object. 
        My name is {self.name} and I am from {self.country}
        I have color {self.color}, weight : {self.weight} """

if __name__ == "__main__":
    papaya = TropicalFruit(country="India", name="Papaya")
    print(papaya)
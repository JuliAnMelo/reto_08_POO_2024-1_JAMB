from restaurant_packages.menuitem import MenuItem 

class Appetizer(MenuItem):
    def __init__(self, double):
        self.double = double

    def calculate_total_price(self):
        total = 0
        if self.double == "Simple": total *= 1
        if self.double == "Double": total *= 1.8
        return total

class Soup(Appetizer):
    def __init__(self, double, type):
        super().__init__(double)
        self.type = type
        self.name = "Soup"

    def calculate_total_price(self):
        total = 4000
        if self.type == "Corn": total += 0
        if self.type == "Tomato": total += 200
        if self.type == "Chicken": total += 500
        if self.double == "Simple": total *= 1
        if self.double == "Double": total *= 1.8
        return total

    def get_receipt(self):
        receipt = f"{self.double} {self.type} {self.name}:\t\t\t ${int(self.get_price())}"
        return receipt

class Egg(Appetizer):
    def __init__(self, double, preparation):
        super().__init__(double)
        self.preparation = preparation
        self.name = "Egg"

    def calculate_total_price(self):
        total = 2000
        if self.preparation == "Boiled": total += 0
        if self.preparation == "Fried": total += 400
        if self.preparation == "Scrambled": total += 800
        if self.double == "Simple": total *= 1
        if self.double == "Double": total *= 1.8
        return total
    
    def get_receipt(self):
        receipt = f"{self.double} {self.preparation} {self.name}:\t\t\t ${int(self.get_price())}"
        return receipt

class Fruit(Appetizer):
    def __init__(self, double, kind):
        super().__init__(double)
        self.kind = kind
        self.name = "Fruit"

    def calculate_total_price(self):
        total = 3000
        if self.kind == "Banana": total += 0
        if self.kind == "Apple": total += 300
        if self.kind == "Strawberry": total += 700
        if self.double == "Simple": total *= 1
        if self.double == "Double": total *= 1.8
        return total
    
    def get_receipt(self):
        receipt = f"{self.double} {self.kind}:\t\t\t\t ${int(self.get_price())}"
        return receipt

class Salad(Appetizer):
    def __init__(self, double, aditive):
        super().__init__(double)
        self.aditive = aditive
        self.name = "Salad"

    def calculate_total_price(self):
        total = 4000
        if self.double == "Simple": total *= 1
        if self.double == "Double": total *= 1.8
        if self.aditive == "No Aditive": total += 0
        if self.aditive == "Vinegar": total += 100
        if self.aditive == "Vinaigrette": total += 200
        if self.aditive == "Olive Oil": total += 300
        return total

    def get_receipt(self):
        receipt = f"{self.double} {self.name} with {self.aditive}:\t\t ${int(self.get_price())}"
        return receipt
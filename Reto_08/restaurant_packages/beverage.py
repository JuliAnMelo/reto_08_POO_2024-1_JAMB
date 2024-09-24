from restaurant_packages.menuitem import MenuItem 

class Beverage(MenuItem):
    def __init__(self, size):
        self.size = size
    def calculate_total_price(self):
        total = 0
        if self.size == "Small": total *= 0.75
        if self.size == "Regular": total *= 1
        if self.size == "Large": total *= 1.5
        return total 

class Water(Beverage):
    def __init__(self, size):
        super().__init__(size)
        self.name = "Water"

    def calculate_total_price(self):
        total = 1500
        if self.size == "Small": total *= 0
        if self.size == "Regular": total *= 0
        if self.size == "Large": total *= 1
        return total  
        
    def get_receipt(self):
        receipt = f"{self.size} {self.name}:\t\t\t\t ${int(self.get_price())}"
        return receipt

class Juice(Beverage):
    def __init__(self, size, fruit):
        super().__init__(size)
        self.fruit = fruit
        self.name = "Juice"

    def calculate_total_price(self):
        total = 2000
        if self.size == "Small": total *= 0.75
        if self.size == "Regular": total *= 1
        if self.size == "Large": total *= 1.5
        if self.fruit == "Orange": total *= 1
        if self.fruit == "Blackberry": total *= 1.2
        if self.fruit == "Mango": total *= 1.4
        return total 
 
    def get_receipt(self):
        receipt = f"{self.size} {self.fruit} {self.name}:\t\t\t ${int(self.get_price())}"
        return receipt

class Soda(Beverage):
    def __init__(self, size, flavor):
        super().__init__(size)
        self.flavor = flavor
        self.name = "Soda"

    def calculate_total_price(self):
        total = 3000
        if self.size == "Small": total *= 0.75
        if self.size == "Regular": total *= 1
        if self.size == "Large": total *= 1.5
        if self.flavor == "Coke": total += 100
        if self.flavor == "Lemon": total += 200
        if self.flavor == "Grapefruit": total += 500
        return total 
    
    def get_receipt(self):
        receipt = f"{self.size} {self.flavor} {self.name}:\t\t\t ${int(self.get_price())}"
        return receipt

class Beer(Beverage):
    def __init__(self, size, brand):
        super().__init__(size)
        self.brand = brand
        self.name = "Beer"
    
    def calculate_total_price(self):
        total = 4000
        if self.brand == "Corona": total += 500
        if self.brand == "Budweiser": total += 1000
        if self.brand == "Heineken": total += 1500
        if self.size == "Small": total *= 0.75
        if self.size == "Regular": total *= 1
        if self.size == "Large": total *= 1.5
        return total

    def get_receipt(self):
        receipt = f"{self.size} {self.brand}:\t\t\t ${int(self.get_price())}"
        return receipt
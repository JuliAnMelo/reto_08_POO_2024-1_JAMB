from restaurant_packages.menuitem import MenuItem 

class Main_Course(MenuItem):
    def __init__(self, addition):
        self.addition = addition

    def calculate_total_price(self):
        total = 0
        if self.addition == "No Extra": total *= 1
        if self.addition == "Extra": total *= 1.5
        return total     

class Rice(Main_Course):
    def __init__(self, addition, color):
        super().__init__(addition)
        self.color = color
        self.name = "Rice"

    def calculate_total_price(self):
        total = 8000
        if self.addition == "No Extra": total *= 1
        if self.addition == "Extra": total *= 1.5
        if self.color == "White": total += 0
        if self.color == "Yellow": total += 100
        if self.color == "Green": total += 400
        return total

    def get_receipt(self):
        receipt = f"{self.color} {self.name} with {self.addition}:\t\t ${int(self.get_price())}"
        return receipt  

class Meat(Main_Course):
    def __init__(self, addition, vegan):
        super().__init__(addition)
        self.vegan = vegan
        self.name = "Meat"

    def calculate_total_price(self):
        total = 12000
        if self.vegan == "Animal Meat": total += 0
        if self.vegan == "Vegan Meat": total += 3000
        if self.addition == "No Extra": total *= 1
        if self.addition == "Extra": total *= 1.5
        return total 

    def get_receipt(self):
        receipt = f"{self.vegan} with {self.addition}:\t\t\t ${int(self.get_price())}"
        return receipt  

class Pasta(Main_Course):
    def __init__(self, addition, variety):
        super().__init__(addition)
        self.variety = variety
        self.name = "Pasta"

    def calculate_total_price(self):
        total = 10000
        if self.variety == "Spaghetti": total += 0
        if self.variety == "Shells": total += 700
        if self.variety == "Macaroni": total += 1500
        if self.addition == "No Extra": total *= 1
        if self.addition == "Extra": total *= 1.5
        return total    

    def get_receipt(self):
        receipt = f"{self.variety} with {self.addition}:\t\t ${int(self.get_price())}"
        return receipt  

class Vegetables(Main_Course):
    def __init__(self, addition, making):
        super().__init__(addition)
        self.making = making
        self.name = "Vegetables"

    def calculate_total_price(self):
        total = 8000
        if self.addition == "No Extra": total *= 1
        if self.addition == "Extra": total *= 1.5
        if self.making == "Boiled": total += 0
        if self.making == "Baked": total += 500
        if self.making == "Sauteed": total += 1000
        return total    

    def get_receipt(self):
        receipt = f"{self.making} {self.name} with {self.addition}:\t\t ${int(self.get_price())}"
        return receipt  
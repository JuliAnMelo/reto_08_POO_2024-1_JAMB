from restaurant_packages.beverage import Water, Juice, Soda, Beer
from restaurant_packages.appetizer import Soup, Egg, Fruit, Salad 
from restaurant_packages.main_course import Rice, Meat, Pasta, Vegetables
from restaurant_packages.payment import Card, Cash
from restaurant_packages.exceptions import IntInputError

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IntInputError as error:
            print(f"\n{error}.\n")
        except ValueError:
            print("\nInvalid input, please enter a valid number.\n")
        except KeyboardInterrupt:
            print("\n\nProcess interrupted by the user.\n\n")
    return wrapper



class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    @handle_exceptions
    def get_total_bill(self):
        total_bill = sum(item.get_price() for item in self.items)
        return int(total_bill)
        
    def iter_items(self):
        for item in self.items:
            yield item


    @handle_exceptions
    def protocol(self):
        try:
            # Main course selection
            try:
                course_ini = int(input("\tMain Course" "\n" "We offer:"  "\nRice\t\tIf you want Rice,\t write 1" 
                                    "\nMeat\t\tIf you want Meat,\t write 2" 
                                    "\nPasta\t\tIf you want Pasta,\t write 3" 
                                    "\nVegetables\tIf you want Vegetables,\t write 4" 
                                    "\nIf you don't want a Main Course,\t write 5\n"))
                if course_ini < 1 or course_ini > 5:
                    raise IntInputError("Please press a number between 1 and 5")
            except ValueError:
                raise IntInputError("Invalid input. Please enter a number.")

            if course_ini < 5:
                try:
                    var_1 = ""
                    con_1 = int(input("\nIf you want a Regular ration,\t\t write 1" 
                                    "\nIf you want an Extra ration,\t\t write 2\n"))
                    if con_1 == 1: var_1 = "No Extra"
                    elif con_1 == 2: var_1 = 'Extra'
                    else: raise IntInputError("Please press a number between 1 and 2")
                except ValueError:
                    raise IntInputError("Invalid input. Please enter a number.")

                # Courses options
                if course_ini == 1:
                    try:
                        var_2 = ""
                        con_2 = int(input("\nIf you want White Rice,\t\t\t write 1" 
                                        "\nIf you want Yellow Rice,\t\t write 2" 
                                        "\nIf you want Green Rice,\t\t\t write 3\n"))
                        if con_2 == 1: var_2 = "White"
                        elif con_2 == 2: var_2 = "Yellow"
                        elif con_2 == 3: var_2 = "Green"
                        else: raise IntInputError("Please press a number between 1 and 3")
                        self.add_item(Rice(var_1, var_2))
                    except ValueError:
                        raise IntInputError("Invalid input. Please enter a number.")

                elif course_ini == 2:
                    try:    
                        var_2 = ""
                        con_2 = int(input("\nIf you want Regular Meat,\t\t write 1" "\nIf you want Vegan Meat,\t\t\t write 2\n"))    
                        if con_2 == 1: var_2 = "Animal Meat" 
                        elif con_2 == 2: var_2 = "Vegan Meat"
                        else: raise IntInputError("Press a number between 1 and 2")
                        self.add_item(Meat(var_1, var_2))
                    except ValueError:
                        raise IntInputError("Invalid input. Please enter a number.")
                    
                elif course_ini == 3:
                    try:
                        var_2 = ""
                        con_2 = int(input("\nIf you want Spaghetti,\t\t\t write 1" "\nIf you want Shells,\t\t\t write 2" "\nIf you want Macaroni,\t\t\t write 3\n"))  
                        if con_2 == 1: var_2 = "Spaghetti"
                        elif con_2 == 2: var_2 = "Shells"
                        elif con_2 == 3: var_2 = "Macaroni"
                        else: raise IntInputError("Press a number between 1 and 3")
                        self.add_item(Pasta(var_1, var_2))
                    except ValueError:
                        raise IntInputError("Invalid input. Please enter a number.")

                elif course_ini == 4:
                    try:
                        var_2 = ""
                        con_2 = int(input("\nIf you want Boiled Vegetables,\t\t write 1" "\nIf you want Baked Vegetables,\t\t write 2" "\nIf you want Sauteed Vegetables,\t\t write 3\n"))
                        if con_2 == 1: var_2 = "Boiled"
                        elif con_2 == 2: var_2 = "Baked"
                        elif con_2 == 3: var_2 = "Sauteed"
                        else: raise IntInputError("Press a number between 1 and 3")
                        self.add_item(Vegetables(var_1, var_2))
                    except ValueError:
                        raise IntInputError("Invalid input. Please enter a number.")

            # Appetizer selection
            try:
                appeti_ini = int(input("\t\tAppetizer" "\n" "We offer:"  "\nSoup\t\tIf you want Soup,\t write 1" 
                                    "\nEgg\t\tIf you want Egg,\t write 2" 
                                    "\nFruit\t\tIf you want Fruit,\t write 3" 
                                    "\nSalad\t\tIf you want Salad,\t write 4" 
                                    "\nIf you don't want an Appetizer,\t\t write 5\n"))
                if appeti_ini < 1 or appeti_ini > 5:
                    raise IntInputError("Please press a number between 1 and 5")
            except ValueError:
                raise IntInputError("Invalid input. Please enter a number.")

            if appeti_ini < 5:
                try:
                    var_1 = ""
                    con_1 = int(input("\nIf you want a Regular ration,\t\t write 1" "\nIf you want a Double ration,\t\t write 2\n"))    
                    if con_1 == 1: var_1 = "Single"
                    elif con_1 == 2: var_1 = 'Double'
                    else: raise IntInputError("Press a number between 1 and 2")
                except ValueError:
                    raise IntInputError("Invalid input. Please enter a number.")   
                
                if appeti_ini == 1:
                    try:
                        var_2 = ""
                        con_2 = int(input("\nIf you want a Corn Soup,\t\t write 1" "\nIf you want a Tomato Soup,\t\t write 2" "\nIf you want a Chicken Soup,\t\t write 3\n"))
                        if con_2 == 1: var_2 = "Corn"
                        elif con_2 == 2: var_2 = "Tomato"
                        elif con_2 == 3: var_2 = "Chicken"
                        else: raise IntInputError("Press a number between 1 and 3")
                        self.add_item(Soup(var_1, var_2))
                    except ValueError:
                        raise IntInputError("Invalid input. Please enter a number.")

                elif appeti_ini == 2:
                    try:
                        var_2 = ""
                        con_2 = int(input("\nIf you want the Egg Boiled,\t\t write 1" "\nIf you want the Egg Fried,\t\t write 2" "\nIf you want the Egg Scrambled,\t\t write 3\n"))
                        if con_2 == 1: var_2 = "Boiled"
                        elif con_2 == 2: var_2 = "Fried"
                        elif con_2 == 3: var_2 = "Scrambled"
                        else: raise IntInputError("Press a number between 1 and 3")
                        self.add_item(Egg(var_1, var_2))
                    except ValueError:
                        raise IntInputError("Invalid input. Please enter a number.")

                elif appeti_ini == 3:
                    try:
                        var_2 = ""
                        con_2 = int(input("\nIf you want Banana,\t\t\t write 1" "\nIf you want Apple,\t\t\t write 2" "\nIf you want Strawberry,\t\t\t write 3\n"))
                        if con_2 == 1: var_2 = "Banana"
                        elif con_2 == 2: var_2 = "Apple"
                        elif con_2 == 3: var_2 = "Strawberry"
                        else: raise IntInputError("Press a number between 1 and 3")
                        self.add_item(Fruit(var_1, var_2))
                    except ValueError:
                        raise IntInputError("Invalid input. Please enter a number.")

                elif appeti_ini == 4:
                    try:
                        var_2 = ""
                        con_2 = int(input("\nIf you want No Aditive in your Salad,\t write 1" "\nIf you want Vinegar in your Salad,\t write 2" "\nIf you want Vinaigrette in your Salad,\t write 3" "\nIf you want Olive Oil in your Salad,\t write 4\n"))
                        if con_2 == 1: var_2 = "No Aditive"
                        elif con_2 == 2: var_2 = "Vinegar"
                        elif con_2 == 3: var_2 = "Vinaigrette"
                        elif con_2 == 4: var_2 = "Olive Oil"
                        else: raise IntInputError("Press a number between 1 and 4")
                        self.add_item(Salad(var_1, var_2))
                    except ValueError:
                        raise IntInputError("Invalid input. Please enter a number.")

            # Beverage selection
            try:
                bevera_ini = int(input("\t\tBeverage" "\n" "We offer:" 
                                    "\nWater\t\tIf you want Water,\t write 1" 
                                    "\nJuice\t\tIf you want Juice,\t write 2" 
                                    "\nSoda\t\tIf you want Soda,\t write 3" 
                                    "\nBeer\t\tIf you want Beer,\t write 4" 
                                    "\nIf you don't want a Beverage,\t\t write 5\n"))
                if bevera_ini < 1 or bevera_ini > 5:
                    raise IntInputError("Please press a number between 1 and 5")
            except ValueError:
                raise IntInputError("Invalid input. Please enter a number.")

            if bevera_ini < 5:
                try:
                    var_1 = ""
                    con_1 = int(input("\nIf you want a Small Drink,\t\t write 1" "\nIf you want a Regular Drink,\t\t write 2" "\nIf you want a Large Drink,\t\t write 3\n"))    
                    if con_1 == 1: var_1 = "Small"
                    elif con_1 == 2: var_1 = 'Regular'
                    elif con_1 == 3: var_1 = 'Large'
                    else: raise IntInputError("Press a number between 1 and 3")
                except ValueError:
                    raise IntInputError("Invalid input. Please enter a number.")
                
                if bevera_ini == 1:
                    self.add_item(Water(var_1))

                elif bevera_ini == 2:
                    try:
                        var_2 = ""
                        con_2 = int(input("\nIf you want Orange Juice,\t\t write 1" "\nIf you want Blackberry Juice,\t\t write 2" "\nIf you want Mango Juice,\t\t write 3\n"))
                        if con_2 == 1: var_2 = "Orange"
                        elif con_2 == 2: var_2 = "Blackberry"
                        elif con_2 == 3: var_2 = "Mango"
                        else: raise IntInputError("Press a number between 1 and 3")
                        self.add_item(Juice(var_1, var_2))
                    except ValueError:
                        raise IntInputError("Invalid input. Please enter a number.")

                elif bevera_ini == 3:
                    try:
                        var_2 = ""
                        con_2 = int(input("\nIf you want Coca-Cola,\t\t\t write 1" "\nIf you want Sprite,\t\t\t write 2" "\nIf you want Quatro,\t\t\t write 3\n"))
                        if con_2 == 1: var_2 = "Coke"
                        elif con_2 == 2: var_2 = "Lemon"
                        elif con_2 == 3: var_2 = "Grapefruit"
                        else: raise IntInputError("Press a number between 1 and 3")
                        self.add_item(Soda(var_1, var_2))
                    except ValueError:
                        raise IntInputError("Invalid input. Please enter a number.")

                elif bevera_ini == 4:
                    try:
                        var_2 = ""
                        con_2 = int(input("\nIf you want Corona,\t\t\t write 1" "\nIf you want Budweiser,\t\t\t write 2" "\nIf you want Heineken,\t\t\t write 3\n"))
                        if con_2 == 1: var_2 = "Corona"
                        elif con_2 == 2: var_2 = "Budweiser"
                        elif con_2 == 3: var_2 = "Heineken"
                        else: 
                            raise IntInputError("Press a number between 1 and 3")
                        self.add_item(Beer(var_1, var_2))
                    except ValueError:
                        raise IntInputError("Invalid input. Please enter a number.")
                       


        except IntInputError as error:
            print(f"\n{error}.\n")
        except ValueError:
            print("\nPress numbers only.\n")
        except KeyboardInterrupt:
            print("\n\nProcess interrupted by the user.\n\n")


    def get_total_receipt(self):
        print("\n""\t\t""YOUR RECEIPT""\n""\t""ITEM""\t\t\t\t""PRICE")
        sub_total = []
        for item in self.iter_items():
            print(item.get_receipt())
            sub_total.append(int(item.get_price()))
        print(f"Sub Total:\t\t\t\t ${sum(sub_total)}\n")

        rounding_dis = 0
        amount_dis = 0
        if len(sub_total) >= 6:           
            for st in sub_total:
                if st >= 2000 and st <= 5000: rounding_dis += 1000
                if st < 2000: rounding_dis += st
            print(f"Discount for Rounding:\t\t\t ${rounding_dis}")
        if len(sub_total) == 8:
            amount_dis += 2000
            print(f"Discount for Eight items:\t\t\t ${amount_dis}")
        if len(sub_total) == 12:
            amount_dis += 4000
            print(f"Discount for Twelve items:\t\t\t ${amount_dis}")
        if len(sub_total) > 12 and len(sub_total) < 20:
            amount_dis += 8000
            print(f"Discount for Big Order:\t\t\t ${amount_dis}")
        if len(sub_total) > 20:
            amount_dis += (sum(sub_total)) / 10
            print(f"Discount for Buffet Order:\t\t ${amount_dis}")
        total = sum(sub_total) - (rounding_dis + amount_dis)
        print(f"\nTotal Bill:\t\t\t\t ${total}")

        pay = int(input("\nIf you are paying with a Credit Card,\t write 1" "\nIf you are paying with Cash,\t\t write 2\n"))
        if pay == 1:
            code = input("Please write your card's number\n")
            money = int(input("Please write the amount you will pay\n$"))
            payment = Card(code, money)
            payment.to_pay(total)
        if pay == 2:
            money = int(input("Please write the amount you will pay\n$"))
            payment = Cash(money)
            payment.to_pay(total)


class Exercise(Order):
    def __init__(self, program, iterations):
        self.program = program
        self.iterations = iterations

    def execute(self):
        challenge = self.program
        for _ in range(self.iterations):
            challenge.protocol()
        return challenge.get_total_receipt()
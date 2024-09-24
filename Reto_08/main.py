from restaurant_packages.order import Order, Exercise
            
if __name__ == "__main__": 
    counter = int(input("Welcome to this establishment\nHow many people?\n"))
    order = Order()
    challenge_08 = Exercise(order, counter)
    challenge_08.execute()
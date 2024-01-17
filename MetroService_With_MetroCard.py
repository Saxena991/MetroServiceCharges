class MetroCard:
    def __init__(self, card_number, balance=0):
        self.card_number = card_number
        self.balance = balance

    def recharge(self, amount):
        # Add the specified amount to the card balance
        self.balance += amount
        print(f"Successfully recharged ${amount}. New balance: ${self.balance}")

    def deduct(self, amount):
        # Deduct the specified amount from the card balance
        if self.balance >= amount:
            self.balance -= amount
            print(f"${amount} deducted for the journey. Remaining balance: ${self.balance}")
            return True
        else:
            print("Insufficient balance. Please recharge your MetroCard.")
            return False

def choose_destination(metro_card):
    print("""Please enter:
            4 for adult
            5 for senior citizen
            6 for kids """)
                    
    passenger_type = input("Enter your Passenger Type (4, 5, 6): ")

    if passenger_type == "4":
        return 200
    elif passenger_type == "5":
        return 100
    elif passenger_type == "6":
        return 50
    else:
        print("Invalid passenger type. Defaulting to adult fare.")
        return 200

def metro_journey(metro_card):
    print("Welcome to the Non-stop Metro Train!")

    while True:
        print("\n1. Central Station to Airport")
        print("2. Airport to Central Station")
        print("3. Return journey")
        print("4. Exit")

        destination = input("Enter your destination Type (1, 2, 3, 4): ")

        if destination == "1":
            print("Boarding the non-stop train from Central Station to Airport.")
            print("Arrived at the Airport.")
            journey_cost = choose_destination(metro_card)
            if not metro_card.deduct(journey_cost):
                recharge_amount = journey_cost + journey_cost * 0.02  
                metro_card.recharge(recharge_amount)
        
        elif destination == "2":
            print("Boarding the non-stop train from Airport to Central Station.")
            print("Arrived at the Central Station.")
            journey_cost = 50  
            if not metro_card.deduct(journey_cost):
                recharge_amount = journey_cost + journey_cost * 0.02  
                metro_card.recharge(recharge_amount)

        elif destination == "3":
            print("Initiating return journey.")
            return_cost = choose_destination(metro_card) / 2
            if not metro_card.deduct(return_cost):
                recharge_amount = return_cost + return_cost * 0.02  
                metro_card.recharge(recharge_amount)
        
        elif destination == "4":
            print("Exiting the Non-stop Metro Train system. Have a great day!")
            break

metro_card_number = input("Enter your MetroCard number: ")
metro_card = MetroCard(metro_card_number)


metro_journey(metro_card)

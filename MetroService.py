def choose_detstination():
            print("""please enter 
                        4 for adult
                        5 for senior_sitizen
                        6 for kids """)
                    
            Passenger_Type = input("Enter your Passenger Type (4, 5, 6): ")

            if Passenger_Type == "4":
                func = 200
                print("you paying:", func)

            elif Passenger_Type == "5":
                func = 100
                print("you paying:", func)

            elif Passenger_Type == "6":
                func = 50
                print("you paying:", func)
            return func


def metro_journey():
    print("Welcome to the Non-stop Metro Train!")
    while True:
        
        print("\n1. Central Station to Airport")
        print("2. Airport to Central Station")
        print("3. retutn journey")
        print("4. Exit")

        
        destination = input("Enter your destination Type (1, 2, 3, 4): ")

        if destination == "1":
            print("Boarding the non-stop train from Central Station to Airport.")
            print("Arrived at the Airport.")
            print("Thank you for using the Non-stop Metro Train!")
        
        elif destination == "2":
            print("Boarding the non-stop train from Airport to Central Station.")
            print("Arrived at the Centrals Station.")
            print("Thank you for using the Non-stop Metro Train!")

        
        elif destination == "3":
            return_cost = choose_detstination() / 2
            print("You are paying half the cost for the return journey:", return_cost)
        

        elif destination == "4":
            print("Exiting the Non-stop Metro Train system. Have a great day!")
            break

        choose_detstination()
    
metro_journey()








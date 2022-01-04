"""
Practical 8, Question 4
taxi_simulator.py
"""

from silver_service_taxi import Taxi, SilverServiceTaxi

BORDER = "—" * 150
SENTINEL = -1
MENU = "Menu:\n(C) Choose\n(D) Drive\n(Q) Quit"
OPTIONS = ["C", "D", "Q"]


def main():
    """ Taxi Simulator. """
    print(BORDER)
    print("Practical 8, Question 4\ntaxi_simulator.py")
    print(BORDER)
    # necessary variables
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi_number = None
    total_trip_cost = 0
    run = 0
    print("Let's Drive!")
    print(BORDER)
    while run != SENTINEL:
        # menu
        print(MENU)
        print(BORDER)
        # options
        option = select_option("Select option: ")
        print(BORDER)
        # choose
        if option == "C":
            print(f"Taxis available:")
            # taxi list
            display_taxis(taxis)
            # taxi number
            current_taxi_number = choose_taxi(taxis)
            # reset if a previous fare was done
            if taxis[current_taxi_number].current_fare_distance != 0:
                taxis[current_taxi_number].current_fare_distance = 0
            # current bill
            print(f"Current bill: ${total_trip_cost:.2f}")
        # drive
        elif option == "D":
            if current_taxi_number in [i for i in range(len(taxis))]:
                # update taxi
                drive_taxi(taxis[current_taxi_number])
                current_taxi = taxis[current_taxi_number]
                # fare
                print(f"Your {current_taxi.name} trip costs you ${current_taxi.get_fare():.2f}")
                # update bill
                total_trip_cost += current_taxi.get_fare()
                # reset
                current_taxi_number = None
            else:
                # alert to choose a taxi
                print("You need to choose a taxi, first!")
            # current bill
            print(f"Current bill: ${total_trip_cost:.2f}")
        # quit
        else:
            # final status (bill and taxi list)
            print(f"Total trip cost: ${total_trip_cost:.2f}")
            print(f"Final status of the taxis:")
            display_taxis(taxis)
            # exit program
            run = SENTINEL
        print(BORDER)


def select_option(prompt):
    """ Choose an option from the menu. """
    option = input(prompt).upper()
    while option not in OPTIONS:
        print("Invalid option!")
        option = input(prompt).upper()
    return option


def display_taxis(taxi_list):
    """ Display the list of taxis. """
    for i, taxi in enumerate(taxi_list):
        print(f"{i} – {taxi}")


def choose_taxi(taxi_list):
    """ Choose a taxi from the list of taxis. """
    run = 0
    while run != SENTINEL:
        try:
            choice_number = int(input("Choose taxi: "))
            if choice_number in [i for i in range(len(taxi_list))]:
                print(f"Chosen taxi {choice_number}!")
                return choice_number
            else:
                print("Invalid taxi choice!")
        except ValueError:
            print("Invalid value!")


def drive_taxi(taxi):
    """ Drive the current taxi """
    run = 0
    while run != SENTINEL:
        try:
            distance = float(input("How far will the drive be?: "))
            if distance >= 0:
                taxi.drive(distance)
                run = SENTINEL
            else:
                print("Invalid distance!")
        except ValueError:
            print("Invalid value!")


if __name__ == '__main__':
    main()

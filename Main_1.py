import Delay
import Flight_Trends
import Edit_passenger
import Search_Passenger
import Add_Passenger
import Flight_details
import ticket_available as ticket_available
import Ticket_booking as Ticket_booking


def main_menu():
    print("==========Welcome to AeroHub===========")

    main_choice = int(input("Please choose a profile: \n1.Admin \n2.User\n"))
    
    if (main_choice == 1):
        
        print("What do we wish to do?...")
        admin_choice = int(input("\n1.Add Passenger \n2.Search Passenger \n3.Edit Passenger\n4.Flight Delay\n5.Ticket Booking\n"))
        
        if (admin_choice == 1):
            Add_Passenger.add_passenger()
        elif (admin_choice == 2):
            Search_Passenger.search_Passenger()
        elif (admin_choice == 3):
            Edit_passenger.to_edit()
        elif (admin_choice == 4):
            Delay.Delay()
        else:
            print("Enter a valid input")

    elif (main_choice == 2):
        print("How can we help you today?...")
        user_choice = int(input("1.Flight Details \n2.Flight Price Trends \n3.See your details\n4.Ticket Availablity\n5.Book Ticket\n"))

        if (user_choice == 1):
            Flight_details.timing()
        elif (user_choice == 2):
            Flight_Trends.plot_trends()
        elif (user_choice == 3):
            Search_Passenger.search_Passenger()
        elif (user_choice == 4):
            ticket_available.ticket_available()
        elif (user_choice == 5):
            Ticket_booking.book_ticket()
        else:
            print("Enter a valid input")


main_menu()

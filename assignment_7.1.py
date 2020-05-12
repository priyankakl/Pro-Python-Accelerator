import time

class ParkingLot:
    """
    This class helps us book slots, unbook slots and generates bill based on the duration.
    book_slot() method : 
    Required parameters = 1) vehicle_type i.e. 2 wheeler or 4 wheeler
                          2) vehicle_number i.e. unique identification number of the vehicle
    unbook_slot() method :
    Required parameters = 1) vehicle_number

    """ 
    # to initialize the variables with values while creating an intance of object
    def __init__(self, two_wheeler_slots, four_wheeler_slots):

        self.two_wheeler_slots = two_wheeler_slots
        self.four_wheeler_slots = four_wheeler_slots
        self.vehicle_details = {}

    # to book a slot for a vehicle and to start the time for calculating duration later
    def book_slot(self, vehicle_type, vehicle_number):
        if vehicle_type == "1":
            if self.two_wheeler_slots >= 1:
                self.two_wheeler_slots = self.two_wheeler_slots - 1
            else:
                print("sorry we have no slots for your vehicle!")
        elif vehicle_type == "2":
            if self.four_wheeler_slots >= 1:
                self.four_wheeler_slots = self.four_wheeler_slots -1
            else:
                print("sorry we have no slots for your vehicle!")
        start = time.time()
        self.vehicle_details[vehicle_number] = [vehicle_type, start]
        total_slots = self.two_wheeler_slots + self.four_wheeler_slots
        print("Total slots left:\t" ,total_slots)

    # To unbook the slot and and generate the bill based on duration
    def unbook_slot(self, vehicle_number):
        if vehicle_number in self.vehicle_details.keys(): 
            if self.vehicle_details[vehicle_number][0] == "1":
                self.two_wheeler_slots = self.two_wheeler_slots + 1
            if self.vehicle_details[vehicle_number][0] == "2":
                self.four_wheeler_slots = self.four_wheeler_slots + 1
            end = time.time()
            duration = int(end - self.vehicle_details[vehicle_number][1])
            print("your bill is:\t", duration*5 )
            total_slots = self.two_wheeler_slots + self.four_wheeler_slots
            print("Total slots left:\t" ,total_slots)
            del self.vehicle_details[vehicle_number]
        else:
            print("Enter valid vehicle number")
 
# To take input from the user and calling the function based on input
def main():
    parking1 = ParkingLot(10,10)
    while True:  
        print("\t\n\nWhich of the following would you like to choose?\n \t 1.Book a slot \t 2.Unbook a slot\n")
        option = input()
        if option == "1":
            vehicle_type = input(" Please select the type of your vehicle\n \t 1. 2 wheeler \t 2. 4 wheeler\n")
            vehicle_number = input(" Please enter your vehicle number\n")
            parking1.book_slot(vehicle_type, vehicle_number) 
        elif option == "2":
            vehicle_number = input(" Please enter your vehicle number\n")
            parking1.unbook_slot(vehicle_number)          
        else:
            print("Enter valid option")
            break



if __name__=="__main__": 
    main()

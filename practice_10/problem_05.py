# Write a class Train which has methods to Book a ticket, get the status(no. of seats), get fare information of the train running under Pakistan Railways.

class Train:
    def __init__(self,available_seats,fare):
        self.available_seats = available_seats
        self.fare = fare
        with open("train.txt", "r") as f:
            data = f.read()
            self.available_seats = int(data)
    def book_ticket(self):
        if self.available_seats > 0:
            self.available_seats -= 1
            print("Ticket booked successfully.")
        else:
            print("No seats available.")
        with open ("train.txt", "w") as f:
            f.write(str(self.available_seats))
    def get_status(self):
        print(f"Available seats: {self.available_seats}")
    def get_fare_info(self):
        print(f"Fare per ticket: {self.fare}")
train = Train(100, 1500)
train.get_status()
train.book_ticket()
train.get_status()
train.get_fare_info()

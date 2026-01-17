#HOTEL BOOKING SYSTEM USING OOP
class Room:
    def __init__(self, Room_Number, Room_Type, Price_Per_Night, AVAILABILITY=True):
        self.Room_Number = Room_Number
        self.Price_Per_Night = Price_Per_Night
        self.Room_Type = Room_Type
        self.AVAILABILITY = AVAILABILITY
    def __str__(self):
        Status = "AVAILABLE" if self.AVAILABILITY else "BOOKED"
        return f"Room Number: {self.Room_Number} ({self.Room_Type}) - {self.Price_Per_Night} [{Status}]"
    def Book(self):
        if self.AVAILABILITY:
            self.AVAILABILITY = False
            return True
        return False
class Hotel1:
    def __init__(self, Name):
        self.Name = Name
        self.Rooms = []
    def Add_Room(self, Room):
        self.Rooms.append(Room)
    def Show_Rooms(self):
        print(f"\n{self.Name} Rooms")
        for Room in self.Rooms:
            print(Room)
    def Book_Room(self, Room_Number):
        for Room in self.Rooms:
            if Room.Room_Number == Room_Number:
                if Room.Book():
                    print(f"Room {Room_Number} has been booked.")
                else:
                    print(f"Room {Room_Number} is already booked.")
                return
        print(f"Room {Room_Number} not found.")
hotel = Hotel1("MyHotel")
hotel.Add_Room(Room("101", "NORMAL", 1800))
hotel.Add_Room(Room("102", "NORMAL", 1800))
hotel.Add_Room(Room("103", "NORMAL", 1800))
hotel.Add_Room(Room("202", "DELUXE", 2500))
hotel.Add_Room(Room("203", "DELUXE", 2500))
hotel.Add_Room(Room("301", "EXECUTIVE", 3200))
hotel.Add_Room(Room("302", "EXECUTIVE", 3200))
hotel.Add_Room(Room("303", "EXECUTIVE", 3200))
hotel.Add_Room(Room("304", "EXECUTIVE", 3200))
hotel.Add_Room(Room("305", "EXECUTIVE", 3200))
hotel.Add_Room(Room("405", "SPECIAL EXC", 4500))
hotel.Add_Room(Room("406", "SPECIAL EXC", 4500))
hotel.Add_Room(Room("407", "SPECIAL EXC", 4500))   
hotel.Add_Room(Room("500", "CLASS SUITE", 7000))
hotel.Add_Room(Room("501", "CLASS SUITE", 7000))
hotel.Add_Room(Room("502", "CLASS SUITE", 7000))
hotel.Add_Room(Room("600", "GUEST HOUSE", 10000))

hotel.Show_Rooms()
hotel.Book_Room("303")
hotel.Book_Room("301")
hotel.Show_Rooms()
hotel.Book_Room("103")
hotel.Show_Rooms()
hotel.Book_Room("500")
hotel.Show_Rooms()
hotel.Book_Room("500")
hotel.Book_Room("501")

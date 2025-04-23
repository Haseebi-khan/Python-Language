


class Room:
    def __init__(self, r_no: str, windows: int, shelf: int ):
        self.r_no = r_no[:4]
        self.windows = windows
        self.shelf = shelf


    def display(self):
        print("Room no: ",self.r_no)
        print("Windows: ", self.windows)
        print("Shelf: ", self.shelf)
        

room = []

room.append(Room("021332", 2,3))
room.append(Room("5656", 1,2))

room[0].display()
print("------------------------------")
room[1].display()
print("------------------------------")

del room[1]

# room[1].display()



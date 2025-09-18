# class Room:
#     def __init__(self, r_no: str, windows: int, shelf: int ):
#         self.r_no = r_no[:4]
#         self.windows = windows
#         self.shelf = shelf


#     def display(self):
#         print("Room no: ",self.r_no)
#         print("Windows: ", self.windows)
#         print("Shelf: ", self.shelf)
        

# room = []

# room.append(Room("021332", 2,3))
# room.append(Room("5656", 1,2))

# room[0].display()
# print("------------------------------")
# room[1].display()
# print("------------------------------")

# del room[1]

# room[1].display()



class Employee:
    'Common base class for all empoylee'
    empCount = 0
    
    def __init__(self, name, salary):
        
        self.name = name
        self.salary = salary
        Employee.empCount += 1


    def displayCount(self):
        print("Total Employee %d", Employee.empCount)
    
    def display(self):
        print("Name: ", self.name, ", Salary: ", self.salary)
        

emp1 = Employee("Haseeb", 100)

emp1.display()



import keyboard

class Speaker:
    volumeValue = 100
    # volummErrorBuz = (2/100) * volummValue
    
    connectedBlutoot = False
    Input1 = False
    Input2 = False
    
    preConnectDeviceCount = 0 

    def __dict__(self):
        "just for checking."
    
    def __init__(self, speakerVolume1:int = 50, speakerVolume2:int = 50, input1:bool=False, input2:bool=False):
        
        if input1 and input2:
            self.Input1 = input1
            self.Input2 = input2

            self.speakerVolume1 = speakerVolume1
            self.speakerVolume2 = speakerVolume2
            
            if (speakerVolume1 > speakerVolume2 ): 
                volummError = speakerVolume1 - speakerVolume2
                self.balanceVolumm =  speakerVolume1 - volummError
            else:
                volummError = speakerVolume2 - speakerVolume1
                self.balanceVolumm =  speakerVolume2 - volummError

            print("Balance Volume: ", self.balanceVolumm)

        elif input1:
            self.Input1 = input1
            self.speakerVolume1 = speakerVolume1
            self.balanceVolumm = 100
            
            print("Balance Volume: ", self.balanceVolumm)
            
            print("Error in input Red")
        else:
            self.Input2 = input2
            self.speakerVolume2 = speakerVolume2
            self.balanceVolumm = 100
            
            print("Balance Volume: ", self.balanceVolumm)            
            
            print("Error in input Green")                        
        
    def showVolume(self):
        print("Volumne: ", self.volumeValue)
        
    def showBalance(self):
        print("Balance: ", self.balanceVolumm )
    
    def highLowVolume(self):        
        if keyboard.is_pressed("up"):
            if self.volumeValue >= 100:
                print("Volume Full")
            else:
                self.volumeValue += 5
                print("Volume:", self.volumeValue)
        elif keyboard.is_pressed("down"):
            if self.volumeValue <= 0:
                print("Mute")
            else:
                self.volumeValue -= 5
                print("Volume:", self.volumeValue)

s1 = Speaker(65, 88, True, True)
s1.showBalance()
s1.showVolume()

setattr(s1, 'preConnectDeviceCount',55)
print("preConnectedDeviceCount: ",s1.preConnectDeviceCount)
delattr(s1, 'preConnectDeviceCount')
print("preConnectedDeviceCount: ",s1.preConnectDeviceCount)

print("Volume Input:  (press  esc close.): ")
while True:
    key = keyboard.read_key()
    if key == "esc":
        print("ESC pressed. Exiting...")
        break
    s1.highLowVolume()
   
stra = s1.__dict__
print(stra)





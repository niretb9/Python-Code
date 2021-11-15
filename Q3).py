Biology = float(input("Please enter Biology marks: "))
AnalogElectronics = float(input("Please enter Analog Electronics marks: "))
Cprogramming = float(input("Please enter C programming marks: "))
DataStructures = float(input("Please enter Data structures marks: "))
OperatingSystem = float(input("Please enter Operating system marks: "))

total = Biology + AnalogElectronics + Cprogramming + DataStructures + OperatingSystem 
perc = (total / 500) *  100

if(perc>=90):
  print("Grade: O")
elif(perc>=80 and perc<90):
   print("Grade: E")
elif(perc>=70 and perc<80):
   print("Grade: A")
elif(perc>=60 and perc<70):
   print("Grade: B")
elif(perc>=40 and perc<60):
   print("Grade: C")
elif(perc<40):
   print("Grade: D")





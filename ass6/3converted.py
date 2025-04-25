class Converter:
    CONVERSIONS = {'inches': 0.0254,'feet': 0.3048,    'yards': 0.9144,   'miles': 1609.34, 'kilometers': 1000,'meters': 1, 'centimeters': 0.01, 'millimeters': 0.001}
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit.lower()
        self.length_in_meters = self.length * self.CONVERSIONS[self.unit]

    def inches(self):
        return self.length_in_meters / self.CONVERSIONS['inches']
    
    def feet(self):
        return self.length_in_meters / self.CONVERSIONS['feet']
    
    def yards(self):
        return self.length_in_meters / self.CONVERSIONS['yards']
    
    def miles(self):
        return self.length_in_meters / self.CONVERSIONS['miles']
    
    def kilometers(self):
        return self.length_in_meters / self.CONVERSIONS['kilometers']
    
    def meters(self):
        return self.length_in_meters
    
    def centimeters(self):
        return self.length_in_meters / self.CONVERSIONS['centimeters']
    
    def millimeters(self):
        return self.length_in_meters / self.CONVERSIONS['millimeters']

length = int(input("Enter the length : "))
unit = input("Enter the unit (inches, feet, yards, miles, kilometers, meters, centimeters, millimeters): ").lower()

c = Converter(length , unit)

print("\nEnter\n1.inches\n2.feet\n3.yards\n4.miles\n5.kilometers\n6.meters\n7.centimeters\n8.milimeters")
choice = int(input("Enter your choice(1-8) : "))

match choice:
    case 1:
        print("Inches : ", c.inches())
    case 2:
        print("Feet : ", c.feet())
    case 3:
        print("Yards : ", c.yards())
    case 4:
        print("miles : ", c.miles())
    case 5:
        print("Kilometers : ", c.kilometers())
    case 6:
        print("Meters : ", c.meters())
    case 7:
        print("Centimeters : ", c.centimeters())
    case 8:
        print("Milimeters : ", c.millimeters())
    case _:
        print("Invalid choice.")
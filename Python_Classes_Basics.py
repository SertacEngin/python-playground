"""Python Classes Basics"""


# Base class
class Vehicle:
    "Class-level attribute (shared by all instances)"
    wheels = 0

    def __init__(self, make, model, year):
        # Instance-level attributes (unique to each instance)
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Default value for new vehicles

    def describe_vehicle(self):
        "Method to describe the vehicle"
        print(f"{self.year} {self.make} {self.model}")

    def drive(self, miles):
        "Method to update the odometer reading"
        self.odometer_reading += miles
        print(f"{self.make} {self.model} has driven {
              miles} miles. Odometer: {self.odometer_reading} miles")

    def read_odometer(self):
        "Method to show the odometer reading"
        print(f"{self.make} {self.model} Odometer: {
              self.odometer_reading} miles")

# Derived class (Inheritance)


class Car(Vehicle):
    "Additional class-level attribute specific to Car"
    wheels = 4

    def __init__(self, make, model, year, fuel_type):
        # Call to the base class constructor
        super().__init__(make, model, year)
        self.fuel_type = fuel_type  # New instance attribute specific to Car

    # Overriding the describe_vehicle method to add fuel_type
    def describe_vehicle(self):
        super().describe_vehicle()  # Call the parent method
        print(f"Fuel Type: {self.fuel_type}")

# Another Derived Class (Inheritance)


class Motorcycle(Vehicle):
    "Additional class-level attribute specific to Motorcycle"
    wheels = 2

    def __init__(self, make, model, year, helmet_required):
        # Call to the base class constructor
        super().__init__(make, model, year)
        # New instance attribute specific to Motorcycle
        self.helmet_required = helmet_required

    # Overriding the describe_vehicle method to add helmet information
    def describe_vehicle(self):
        super().describe_vehicle()  # Call the parent method
        print(f"Helmet Required: {self.helmet_required}")


# Create instances of different vehicles
my_car = Car("Toyota", "Corolla", 2020, "Gasoline")
my_motorcycle = Motorcycle("Yamaha", "R1", 2021, True)

# Accessing class-level attributes
print(f"A car has {my_car.wheels} wheels.")  # Class-level attribute of Car
# Class-level attribute of Motorcycle
print(f"A motorcycle has {my_motorcycle.wheels} wheels.")

# Calling instance methods
my_car.describe_vehicle()  # Method for Car
my_car.drive(150)  # Method for Car
my_car.read_odometer()  # Method for Car

my_motorcycle.describe_vehicle()  # Method for Motorcycle
my_motorcycle.drive(120)  # Method for Motorcycle
my_motorcycle.read_odometer()  # Method for Motorcycle

# Modifying instance attributes directly
my_car.odometer_reading = 500  # Directly changing the instance attribute
my_motorcycle.odometer_reading = 300  # Directly changing the instance attribute

# Calling methods after modifying the odometer reading
my_car.read_odometer()  # Updated value
my_motorcycle.read_odometer()  # Updated value

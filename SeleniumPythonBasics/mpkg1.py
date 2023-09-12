import vehicle
# from <pkg_folder_name> import <files>


# print(vehicle.user) # access variavle initiate in __init__.py
from vehicle import classcar, cycle, car

car.sportscar()
cycle.motorcycle()

#<filename>.function_name/variable
obj=classcar.car() # initiate the class car constructor
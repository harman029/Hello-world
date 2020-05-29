# Daily travelling kilometers
travelling_km = float(input("Enter the kilometers you travel in a day > "))
 
# Diesel cost
diesel_cost = float(input("Enter the cost of Petrol/Diesel > "))
 
# Vehicle fuel average
vehicle_fuel_avg = float(input("Enter the Vehicle Average > "))
 
# Fuel you want during travelling
fuel_consumption = (travelling_km/vehicle_fuel_avg)
print("Fuel Consumed in a day = " + str(round(fuel_consumption,2)) + " Litre" )
 

# cost of driving per day to office
cost_per_day = (diesel_cost*fuel_consumption)
print ("Cost of driving per day to office is :"+str(round(cost_per_day,2))+" INR")
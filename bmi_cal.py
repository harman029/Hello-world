# User weight
weight = float(input("Enter your weight in kilograms >"))

# User height 
height = float(input("Enter your height in meters >"))

# BMI Formula
BMI_value = (weight/height)/height

print ("BMI value is :" + str(round(BMI_value,2)))

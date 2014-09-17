print("this program will convert your heigth in centimeters into inches, and your weigth in stones to kilograms")
print("first we will convert your heigth in inches to centimeters")
height_inch=int(input("write your height in inches"))

height_centi=height_inch*2.54

print("this is your height in centimeters {0}".format(height_centi))

print("now we will convert your weight in stones to kilograms")
weight_stone=int(input("write your weight in stones"))

weight_kilo=weight_stone*6.364

print("this is your weight in kilograms: {0}".format(weight_kilo))

print("thank you for using this program")

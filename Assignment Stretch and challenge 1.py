# Jeeson Baktha
# 18 September 2014
# Stretch and Challenge Excercise 1

print ( " This program will calculate the cost of turfing a lawn with a 1 meter border " )

lawn_width = float ( input ( " Please enter the width of your lawn including the border in meters : " )) - 2
lawn_length = float ( input ( " Please enter the length of your lawn including the border in meters : " )) - 2

area_lawn = lawn_width * lawn_length
cost_lawn = 10 * area_lawn

print ( " The total area of your lawn is : {0}m² " .format ( area_lawn))

print ( " The total cost of turfing your lawn is : £{0:.2f}p " .format (cost_lawn))

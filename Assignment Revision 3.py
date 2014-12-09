print("this program will work out how much space there is in a lift once a fridge is put inside")
lift_height=int(input("write the height of the lift:"))
lift_width=int(input("write the width of the lift:"))
lift_length=int(input("write the length of the lift:"))

lift_vol=lift_height*lift_width*lift_length

print("this is the total volume of the lift: {0}".format(lift_vol))

print("now we will work out the volume of the fridge")
fridge_height=int(input("write the height of the fridge:"))
fridge_width=int(input("write the width of the fridge:"))
fridge_length=int(input("write the length of the fridge:"))

fridge_vol=fridge_height*fridge_width*fridge_length

print("this is the total volume of the fridge: {0}".format(fridge_vol))

space_remain=lift_vol-fridge_vol

print("this is amount of space remaining in the lift once the fridge is inside: {0}".format(space_remain))


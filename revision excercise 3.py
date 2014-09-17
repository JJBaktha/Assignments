print("this program will divide 2 numbers and show the answer with the remainder")
num_1=int(input("write your first number:"))
num_2=int(input("write your second number:"))

total_num=num_1//num_2
total_numremainder=num_1%num_2

print("this is the total number of times the second number goes into the first: {0}".format(total_num))
print("this is the remainder left from the calculation: {0}".format(total_numremainder))

DenaryValue = int(input("Enter a denary number"))
BinaryString = ""
while DenaryValue > 0:
    BinaryString = str(DenaryValue%2)+BinaryString
    DenaryValue = DenaryValue//2
print("The binary equivalent is{0}".format(BinaryString))

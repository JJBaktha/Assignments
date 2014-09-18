# Jeeson Baktha
# 18 September 2014
# Development Excercise 4

print ( " This program will calculate the volume of water required to fill a swimming pool with a deep and shallow end " )
pool_length = float ( input ( " Please enter the length of your pool : " ))
pool_width = float ( input ( " Please enter the width of your pool : " ))
deep_depth = float ( input ( " Please enter the depth of your pool at the deep end : " ))
shallow_depth = float ( input ( " Please enter the depth of your pool at the shallow end : " ))

shallow_poolvol = pool_length * pool_width * shallow_depth

deep_length = deep_depth - shallow_depth

deep_poolvol = ( deep_length * pool_width * pool_length ) / 2



total_poolvol = deep_poolvol + shallow_poolvol

print ( " This is the total volume of the pool and the total volume of water needed to fill the pool {0}m³ " .format (total_poolvol))
print ( " Thank you for using this program! " )

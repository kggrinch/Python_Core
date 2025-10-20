import math
# Formate_Specifiers - {:flags} formate a value based on what flags are inserted


price1 = 3000.1415
price2 = -9870.65
price3 = 1292.34

# decimal pointer
# .(number)f = round to that many decimal places (fixed point)
print(f"Price 1 is ${price1:.1f}") # first decimal point
print(f"Price 2 is ${price2:.2f}") # second decimal point
print(f"Price 3 is ${price3:.3f}") # third decimal point

# padding spaces
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
print("")
print(f"Price 3 is ${price3:10}") # adds padding to left
print(f"Price 2 is ${price2:-10}") # same as positive
print(f"Price 1 is ${price1:010}") # adds padding but adds 0s where the padding should be

# justify align value 
# Note: must specify padding after for it to work
# :< = left justify
# :> = right justify
# :^ = center align
print("")
print(f"Price 3 is ${price3:<10}") # left justify
print(f"Price 2 is ${price2:>10}") # right justify
print(f"Price 1 is ${price1:^10}") # center align

# sign before values
# :+ = use a plus sign to indicate positive value or negative value
# : = insert a space before positive numbers 
print("")
print(f"Price 3 is ${price3:+}") # left justify
print(f"Price 2 is ${price2:+}") # right justify
print(f"Price 1 is ${price1:+}") # center align
print(f"Price 3 is ${price3: }") # left justify
print(f"Price 2 is ${price2: }") # right justify
print(f"Price 1 is ${price1: }") # center align

# :, = comma separator
print("")
print(f"Price 3 is ${price3:,}") 
print(f"Price 2 is ${price2:,.2f}") # can mix and match formatting options
print(f"Price 1 is ${price1:+,.2f}")
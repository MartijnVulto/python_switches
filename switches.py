# Turns any negative value of x into -1 and any 0 or positive value into 1.
try:
  switch = x / abs(x)
except:
  switch = 1

# Turns any odd value of x into -1 and any even value into 1.
switch = (-2) * (x % 2 - 0.5)



# Adds or subtracts b to/from a based on switch.
result = a + switch * b

# Multiplies a by b if switch is +1, divides a by b if switch is -1.
result = a * b ** switch

# For a given q results in b if switch is +1 or in (q - b) if switch is -1.
result = (-0.5) * (switch - 1) * q + switch * b

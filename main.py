"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
base = 35.00 # Charge for this sign.
numChar = int(input("How many characters are there: ")) # Number of characters.
woodType = input("Wood type (oak/pine): ") # Type of wood.
color = input("Letter color (black/white/gold): ") # Color of characters.

# Write assignment and if statements here as appropriate.


if(numChar > 5):
    extraChar = (numChar - 5) * 4
else:
    extraChar = 0.00
if(woodType == "oak"):
    woodCharge = 20.0  
else:
    woodCharge = 0.0
if(color == "gold"):
    colorCharge = 15.0
else:
    colorCharge = 0.0

charge = base + woodCharge + colorCharge + extraChar
# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))

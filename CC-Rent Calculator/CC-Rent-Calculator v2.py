import click

#Variables
flat = 100 # Flat rate for services.
distf = 1 # Distance factor multiplier
distfmin = 10 # Distance factor minimum distance
block2 = 2 # Area cost multiplier (price per block^2)
curvew = 100 # Charge for having a curved window
lshape = 100 # Charge for an L-Shaped room
ushape = 150 # Charge for a U-Shaped room
parking = 100 # Charge for parking
extraRcost = "total/4 * extrap"
wall = 200
floor = 200
decoration = 750
movein = 500
secdep = 1000 # Security Deposit


roomnum = str(input("What is the room number? "))
name = str(input("Who is the primary resident? "))

f = open(roomnum + ".txt", "a+")
f.truncate(0)
f.write("Room Number: " + roomnum)
f.write("\nPrimary Resident: " + name)

areacost = int(input("What is the area of the room? ")) * block2
f.write("\nRoom area")



f.write("\n\nAdditional Charges:")

if click.confirm('Should this room have a distance factor? (Below 10 = No) ', default=False):
    dist = int(input("What is the distance value? ")) - distfmin
    dist = distf * dist
    if dist < distfmin:
        dist = 0
    else:
        f.write("\nDistance factor charge: $" + str(dist))
else: 
    dist = 0


if click.confirm('Does the room have a curved window? ', default=False):
    f.write("\nCurved Window: Yes, $" + str(curvew))
else: 
    curvew = 0

if click.confirm('Is the room an L-Shape? ', default=False):
    f.write("\nL-Shape: Yes, $" + str(lshape))
else: 
    lshape = 0
    if click.confirm('Is the room a U-Shape? ', default=False):
        f.write("\nU-Shape: Yes, $" + str(ushape))
    else: 
        ushape = 0



if click.confirm('Will the resident have parking? ', default=True):
    f.write("\nParking: Yes, $" + str(parking))
else: 
    parking = 0

if click.confirm('Will there be additional residents? ', default=False):
    RCount = int(input("How many additional residents? ")) + 1
    extraR = True
else: 
    extraR = False


f.write("\n\nUpfront costs:")
if click.confirm('Does the resident wish to have a customised wall? ', default=False):
    f.write("\nCustomised Wall: Yes, $" + str(wall))
else: 
    wall = 0

if click.confirm('Does the resident wish to have a customised floor? ', default=False):
        f.write("\nCustomised floor: Yes, $" + str(floor))
else: 
    floor = 0

if click.confirm('Does the resident wish to have the decoration service? ', default=False):
        f.write("\nDecoration Service: Yes, $" + str(decoration))
else: 
    decoration = 0

f.write("\nMove in fee: $" + str(movein))
f.write("\nSecurity deposit: $" + str(secdep))

subtotalmonthly = areacost + dist + curvew + lshape + ushape + parking

f.write("\n\nSubtotal Monthly Cost: $" + str(subtotalmonthly))

if extraR == True:
    extraR = subtotalmonthly/4 * RCount
    f.write("\nExtra Residents charge: $" + str(extraR))
else:
    extraR = 0
    f.write("\nNo Extra Residents")

totalmonthly = subtotalmonthly + extraR + flat
if totalmonthly < 1000:
    totalmonthly = 1000



upfront = wall + floor + decoration + movein + secdep
f.write("\nTotal rent: $" + str(totalmonthly))
f.write("\nUpfront costs: $" + str(upfront))
f.write("\nTotal to pay now: $" + str(upfront + totalmonthly))

f.close()
print("\nData written to", roomnum + ".txt")
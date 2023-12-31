# flat = 100
# distf = 1
# block2 = 2
# curvew = 100
# lshape = 100
# ushape = 150
# parking = 100
# extraRcost = total/4 * extrap
# wall = 200
# floor = 200
# decoration = 750
import click

roomnum = str(input("What is the room number?"))
name = str(input("Who is the primary resident?"))

areacost = int(input("What is the area of the room?")) * 2

if click.confirm('Should this room have a distance factor? (Below 10 = No)', default=False):
    distf = int(input("What is the distance value?")) - 10
    if distf < 10:
        distf = 0
else: 
    distf = 0

print("\nAdditional Charges:")
if click.confirm('Does the room have a curved window?', default=False):
    curvew = 100
else: 
    curvew = 0

if click.confirm('Is the room an L-Shape?', default=False):
    lshape = 100
else: 
    lshape = 0

if click.confirm('Is the room a U-Shape?', default=False):
    ushape = 150
else: 
    ushape = 0

if click.confirm('Will there be additional residents?', default=False):
    RCount = int(input("How many additional residents?"))
    extraR = True
else: 
    extraR = False


print("\nUpfront costs:")
if click.confirm('Does the resident wish to have a customised wall?', default=False):
    wall = 100
else: 
    wall = 0

if click.confirm('Does the resident wish to have a customised floor?', default=False):
    floor = 100
else: 
    floor = 0

if click.confirm('Does the resident wish to have the decoration service?', default=False):
    decoration = 750
else: 
    decoration = 0

print("\nMoving in fee: 500")
movein = 500
print("Security Deposit: 1000")
secdep = 1000

subtotalmonthly = areacost + distf

if extraR == True:
    extraR = subtotalmonthly/4 * RCount
else:
    extraR = 0

totalmonthly = subtotalmonthly + extraR
if totalmonthly < 1000:
    totalmonthly = 1000

upfront = wall + floor + decoration + movein + secdep
print("\nTotal rent:", totalmonthly)
print("Upfront costs:", upfront)
print("Total to pay now:", upfront + totalmonthly)
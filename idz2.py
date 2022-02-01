x = float(input("Enter X: "))
y = float(input("Enter Y: "))
if (x * x + y * y <= 1) and (x * x + y * y >= 0.25):
    print("It belongs")
else:
    print("It doesn't belong")
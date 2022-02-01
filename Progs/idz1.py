import sys

m = int(input("Enter the number of season: "))
if m < 1 or m > 4:
    print("Illegal value of m", file=sys.stderr)
    exit(1)
if m == 1:
    print("Winter: December, January, February")
elif m == 2:
    print("Spring: March, April, May")
elif m == 3:
    print("Summer: June, July, August")
else:
    print("Autumn: September, October, November")

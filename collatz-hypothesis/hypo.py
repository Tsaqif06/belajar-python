c0 = int(input("Enter any non-negative and non-zero integer number: "))
counter = 0

while c0 != 1 :
    counter += 1
    if c0 % 2 != 0 :
        c0 = 3 * c0 + 1
        print(int(c0))
    else :
        c0 /= 2
        print(int(c0))

print(f"steps = {counter}")
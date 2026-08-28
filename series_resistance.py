print("Series Resistance Calculator")

n = int(input("Enter the number of resistors: "))

total = 0

for i in range(1, n + 1):
    r = float(input(f"Enter resistance R{i} (ohms): "))
    total += r

print(f"Total Resistance = {total} ohms")

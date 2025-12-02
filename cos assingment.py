print("PHYSICS FORMULAS")
print("1. Force")
print("2. Voltage")
print("3. Accelaration")
print("4. Velocity")
print("5. pressure")

choice = input("Enter your choice (1-5): ")

if choice == "1":
    mass = float(input("Enter mass : "))
    acceleration = float(input("Enter acceleration : "))
    result = mass * acceleration
    print("Force =", result)

elif choice == "2":
    distance = float(input("Enter distance: "))
    time = float(input("Enter time : "))
    result = distance / time
    print("speed =", result)

elif choice == "3":
    vf = float(input("Enter final velocity:  : "))
    vi = float(input("Enter final acceleration:  : "))
    result = (vf - vi) / time
    print("acceleration =", result)

elif choice == "4":
    mass = float(input("Enter mass: "))
    volume = float(input("Enter volume: "))
    result = mass / volume
    print("density =", result)

elif choice == "5":
    force = float(input("Enter force: "))
    area = float(input("Enter area: "))
    result = force / area
    print("pressure =", result)

else:
    print("Invalid choice")
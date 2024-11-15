import random

def initialize_cargo_locations():
    return random.sample(range(1, 8), 3)  

def check_cargo_locations(user_input, cargo_locations):
    found_cargo = [location for location in user_input if location in cargo_locations]
    return sum([cargo_weights.get(location, 0) for location in found_cargo])

cargo_weights = {1: 213, 2: 300, 3: 250, 4: 200, 5: 350, 6: 163, 7: 213}  
cargo_locations = initialize_cargo_locations()

print("Enter the kilometer marks where you think the cargo is buried (1-7 km):")

while True:
    try:
        user_input = [int(input(f"Enter location {i+1}: ")) for i in range(3)]
        if not all(1 <= location <= 7 for location in user_input):
            print("Input out of range. Please enter locations between 1 and 7.")
            continue
    except ValueError:
        print("Invalid input, please enter numbers only.")
        continue

    total_weight = check_cargo_locations(user_input, cargo_locations)

    if total_weight == 713:
        print("Congratulations! You have found all the cargo.")
        break
    else:
        print("Not all cargo found, the boxes have moved. Try again.")
        cargo_locations = initialize_cargo_locations()





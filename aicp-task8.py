BOAT_COUNT = 10
OPENING_TIME = 10
CLOSING_TIME = 17
HOURLY_RATE = 20
HALF_HOUR_RATE = 12

boats = [{'boat_id': i + 1, 'is_available': True, 'return_time': OPENING_TIME, 'hours_hired': 0} for i in range(BOAT_COUNT)]

def calculate_money_for_one_boat(boat):
    print(f"\nBoat {boat['boat_id']}:")

    hire_start_time = int(input(f"Enter the hiring time for Boat {boat['boat_id']} (between {OPENING_TIME} and {CLOSING_TIME}): "))
    hire_duration = float(input("Enter the hiring duration in hours (0.5 for half an hour, 1 for one hour): "))

    if OPENING_TIME <= hire_start_time < CLOSING_TIME and hire_start_time + hire_duration <= CLOSING_TIME:
        boat['is_available'] = False
        boat['return_time'] = hire_start_time + hire_duration
        boat['hours_hired'] += hire_duration

        if hire_duration == 0.5:
            payment = HALF_HOUR_RATE
        else:
            payment = HOURLY_RATE

        print(f"Money taken: ${payment}\n")
        return payment
    else:
        print("Error: Invalid hiring time or duration. Boat not hired.\n")
        return 0

total_money_taken = 0
total_hours_hired = 0

for boat in boats:
    total_money_taken += calculate_money_for_one_boat(boat)
    total_hours_hired += boat['hours_hired']

print(f"Total money taken for the day: ${total_money_taken}")
print(f"Total hours hired for the day: {total_hours_hired} hours")

current_time = float(input("Enter the current time to find available boats: "))

available_boats = [boat['boat_id'] for boat in boats if boat['is_available'] and current_time >= boat['return_time']]
if available_boats:
    print(f"Available boats: {', '.join(map(str, available_boats))}")
else:
    earliest_return_time = min(boat['return_time'] for boat in boats)
    print(f"No boats available. Earliest available time: {earliest_return_time}")

unused_boats = [boat['boat_id'] for boat in boats if boat['is_available']]
most_used_boat = max(boats, key=lambda x: x['hours_hired'])

print(f"\nEnd of Day Report:")
print(f"Total money taken for all boats: ${total_money_taken}")
print(f"Total hours hired for all boats: {total_hours_hired} hours")
print(f"Boats not used today: {', '.join(map(str, unused_boats))}")
print(f"Boat used the most: Boat {most_used_boat['boat_id']} with {most_used_boat['hours_hired']} hours")

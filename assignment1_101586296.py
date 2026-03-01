"""
Author: Kamand Rostami
Assignment: #1
"""

# Step b: Create 4 variables

gym_member = "Alex Alliton"            # str
preferred_weight_kg = 20.5             # float
highest_reps = 25                      # int
membership_active = True               # bool

print("Step b: Variables ")
print("gym_member:", gym_member)
print("preferred_weight_kg:", preferred_weight_kg)
print("highest_reps:", highest_reps)
print("membership_active:", membership_active)
print()

# Step c: Create a dictionary named workout_stats

# Dictionary Tuple where values are tuples (yoga, running, weightlifting)
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (25, 35, 40),
    "Taylor": (40, 30, 25),
    "Morgan": (20, 50, 30)
}

print(" Step c: workout_stats (original) ")
print(workout_stats)
print()

# A list of friend names 
friends = list(workout_stats.keys())

# Step d: Calculate total workout minutes and add to dictionary

for friend in friends:
    yoga, running, weightlifting = workout_stats[friend]
    total_minutes = yoga + running + weightlifting
    workout_stats[friend + "_Total"] = total_minutes

print("Step d: workout_stats (with totals added) ")
print(workout_stats)
print()


# Step e: Create a 2D nested list workout_list


# workout_list is a 2D list: 
workout_list = []
for friend in friends:
    yoga, running, weightlifting = workout_stats[friend]
    workout_list.append([yoga, running, weightlifting])

print(" Step e: workout_list (2D list) ")
print(workout_list)
print()


# Step f: Slice the workout_list


print(" Step f: Slicing")

# 1) Extract and print the minutes for yoga and running for all friends
yoga_and_running_all = [row[:2] for row in workout_list]
print("Yoga + Running (all friends):", yoga_and_running_all)

# 2) Extract and print the minutes for weightlifting for the last two friends
weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting (last two friends):", weightlifting_last_two)
print()


# Step g: Check if any friend's total >= 120


print(" Step g: Total >= 120 check ")
for friend in friends:
    total = workout_stats[friend + "_Total"]
    if total >= 120:
        print(f"Great job staying active, {friend}!")
print()


# Step h: User input to look up a friend


print("Step h: Friend lookup ")
name_input = input("Enter a friend's name (example: Alex): ").strip()

if name_input in workout_stats and name_input in friends:
    yoga, running, weightlifting = workout_stats[name_input]
    total = workout_stats[name_input + "_Total"]

    print(f"\nWorkout minutes for {name_input}:")
    print("  Yoga:", yoga)
    print("  Running:", running)
    print("  Weightlifting:", weightlifting)
    print("  Total:", total)
else:
    print(f"Friend {name_input} not found in the records.")
print()


# Step i: Highest and lowest total workout minutes


print("Step i: Highest / Lowest Totals ")

# Build a simple totals dictionary for just friends
totals_by_friend = {}
for friend in friends:
    totals_by_friend[friend] = workout_stats[friend + "_Total"]

highest_friend = max(totals_by_friend, key=totals_by_friend.get)
lowest_friend = min(totals_by_friend, key=totals_by_friend.get)

print(f"Friend with highest total workout minutes: {highest_friend} ({totals_by_friend[highest_friend]} minutes)")
print(f"Friend with lowest total workout minutes: {lowest_friend} ({totals_by_friend[lowest_friend]} minutes)")
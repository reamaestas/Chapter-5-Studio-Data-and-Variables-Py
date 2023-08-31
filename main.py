# FORK this starter file and save it to your own Repl.it account.
# Declare and initialize the 12 variables here:
date = "Monday 2019-03-18"
time = "10:05:34 AM"
user_input_astronaut_count = input("Enter the number of astronauts to print report:")
astronaut_status = "ready"
average_astronaut_mass_kg = 80.7
crew_mass_kg = int(user_input_astronaut_count) * average_astronaut_mass_kg
fuel_mass_kg = 760000
shuttle_mass_kg = 74842.31
total_mass_kg = crew_mass_kg + fuel_mass_kg + shuttle_mass_kg
fuel_temp_celsius = -225
fuel_level_percent= 100
weather_status = "clear"

# Write code to generate the LC04 report here:
print("-------------------------------------")
print("> LC04 - LAUNCH CHECKLIST")
print("-------------------------------------")
print("Date:", date, "\nTime:", time, "\n\n")

print("-------------------------------------")
print(">ASTRONAUT INFO")
print("-------------------------------------")
print("* count:", int(user_input_astronaut_count), "\n* status:", astronaut_status, '\n\n')
print("-------------------------------------")
print('>FUEL DATA')
print("-------------------------------------")
print('* Fuel temp celsius: ', fuel_temp_celsius, "C", "\n* Fuel level: ", fuel_level_percent, "%\n\n")
#there is a space btw the 100 and %
print("-------------------------------------")
print('> MASS DATA')
print("-------------------------------------")
print("* Crew mass:", crew_mass_kg, "kg","\n* Fuel mass:", fuel_mass_kg, "kg", "\n* Shuttle mass:", shuttle_mass_kg, "kg", "\n* Total mass:", total_mass_kg, "kg\n\n")
print("-------------------------------------")
print("> FLIGHT PLAN")
print("-------------------------------------")
print("* weather:", weather_status, "\n\n")
print("-------------------------------------")
print("> OVERALL STATUS")
print("-------------------------------------")
print('* Clear for takeoff: YES')




# When done, have your TA check your code.




# BONUS: Use input to prompt the user to enter the number of astronauts going on the mission.
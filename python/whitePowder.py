# a car can have multiple speeds, according to the speed you need to display a different color and if the gas will run out too fast
# if a car is going below 20 display yellow for it being too slow
# if a car is going above 20 but below 60 display green for it being in the limit
# if it's going above 60 display red for going above

# Depending on the speed the gas will run out in stages, a stage is a mile
# if the car is going below the limit the gas gets subtracted by 1
# if the car is going in the limit the gas gets subtracted by 3
# if the car is going above the limit the gas gets subtracted by 5
# display how many miles the car will go


speed=int(input("Enter speed: "))

gas=20
gas_usage = 0
miles=0

if speed<int(20):
    print("Yellow, the dirty fellow! You are going too slow!")
    gas_usage = 1
elif speed>int(60):
    print("Brilliant, yet Red. You are going too fast!")
    gas_usage = 5
elif speed>20 and speed<60:
    print("Useless green. You are going the speed limit!")
    gas_usage = 3

while gas_usage <= gas:
    gas -= gas_usage
    miles += 1

print(miles)


# pascal case
# GasUsage

# camel case
# gasUsage

# kebab case
# gas-usage

# snake case
# gas_usage
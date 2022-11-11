# List compresion example


# Create a list of n^2 from the list number and print it
numbers = [1,2,3,4,5]
# Solving it using a loop

number_power_2 = []
for n in numbers:
    number_power_2.append(n**2)

print(number_power_2)

# Solving it using list compression

number_power_2_new = [n**2 for n in numbers]
print(number_power_2_new)

# solving it using lambda function

number_power_2_new_2 = list(map(lambda a: a**2, numbers))
print(number_power_2_new_2)
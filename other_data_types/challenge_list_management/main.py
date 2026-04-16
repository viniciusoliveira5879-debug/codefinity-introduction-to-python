# Home list
meat     = ["Ham" , 3.99, 50, "Sliced"]
cheese    = ["Cheddar", 5.99, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

# 2. Main list
deli_dept =[meat, cheese, condiment]
print("Initial Deli List:" , deli_dept)

# 3. Restoc
if"Ham" in meat and meat[2] < 100:
    meat[2] = 100

#4. Seasonal meat
seasonal_meat = ["Turkey" , 4.50, 100, "Sliced" ]
deli_dept. append(seasonal_meat)

# 5. Remove condiment
deli_dept.remove(condiment)

# 6. Sond and print
deli_dept.sort()
print("Updated Deli List:", deli_dept)
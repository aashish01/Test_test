#Colors
colors = ["Blue", "Red", "Purple", "Yellow","Black","Pink","White"]
print(colors)
#Replacing color values
colors[1:3] = ["Lavender","Navy Blue"]
print(colors)
#Inserting another color
colors.insert(1, "Green")
print(colors)
#Extending the color list
pastels = ["Ocean Blue", "Mint", "Light pink"]
colors.extend(pastels)
print(colors)
colors.pop(3)
print(colors)
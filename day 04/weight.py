# Lambda functions
ton_to_kg = lambda t: t * 1000
kg_to_g = lambda kg: kg * 1000
g_to_mg = lambda g: g * 1000
mg_to_lb = lambda mg: mg * 0.00000220462

# User input
ton = float(input("Enter weight in tonnes: "))

# Conversions
kg = ton_to_kg(ton)
g = kg_to_g(kg)
mg = g_to_mg(g)
lb = mg_to_lb(mg)

# Output
print("Kilograms:", kg)
print("Grams:", g)
print("Milligrams:", mg)
print("Pounds:", lb)
# Lambda conversion functions
km_to_m = lambda x: x * 1000
m_to_cm = lambda x: x * 100
cm_to_mm = lambda x: x * 10
ft_to_in = lambda x: x * 12
in_to_cm = lambda x: x * 2.54

# Function to perform conversion
def distance_converter(distance, name, func):
    print(name, "=", func(distance))

# User input
d = float(input("Enter distance: "))

# All conversions
distance_converter(d, "km to m", km_to_m)
distance_converter(d, "m to cm", m_to_cm)
distance_converter(d, "cm to mm", cm_to_mm)
distance_converter(d, "feet to inches", ft_to_in)
distance_converter(d, "inches to cm", in_to_cm)
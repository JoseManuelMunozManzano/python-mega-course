# Create a function that converts liters to cubic meters knowing that 1000 liters make 1 cubic meter.

def to_cubic_meters (liters):
    cubic_meters = liters / 1000.0
    return cubic_meters


print(to_cubic_meters(1000))
print(to_cubic_meters(2000))
print(to_cubic_meters(800))

# Exercise 01 — Delivery coordinates
#
# The delivery system stores each location in a tuple and needs to separate its coordinates to announce the start of a delivery.
# Given coordinates = (-23.5505, -46.6333), use unpacking to extract the values into latitude and longitude.
# Display: "Starting delivery.
# Latitude: [value], Longitude: [value]".

# Your solution:
coordinates = (-23.5505, -46.6333)
latitude, longitude = coordinates
print(f"Starting delivery\nLatitude: {latitude}, Longitude: {longitude}")

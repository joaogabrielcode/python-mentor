# Exercise 03 — Cargo distribution
#
# A shipping company is planning to transport boxes in small trucks.
# Determine the number of full loads and the boxes left for another trip.
# Distribute 1,250 boxes among trucks that each hold 12 boxes.
# Use // to calculate how many trucks will be completely full and % to calculate how many boxes
# remain for a final smaller trip.

# Your solution:


boxes = 1250
truck_capacity = 12
full_trucks = boxes // truck_capacity
remaining_boxes = boxes % truck_capacity
print(f"FULL TRUCKS: {full_trucks}")
print(f"Remaining boxes: {remaining_boxes}")

# Exercise 05 — Support ticket summary
#
# The support team needs to summarize the day's response times and highlight the longest wait among the tickets.
# Create ticket_summary, which receives a list of response times in minutes and returns the number of tickets and the maximum wait time.
# Test with times = [15, 45, 10, 120, 30] and unpack the results.
# Display a formatted message alerting about the maximum time found.

# Your solution:

times = [15, 45, 10, 120, 30]

def ticket_summary(items):
  quantity = len(items)
  items.sort()
  maximum_time = items[-1]
  return quantity, maximum_time

quantity, maximum_time = ticket_summary(times)
print(f"The number of tickets was: {quantity} and the longest wait was {maximum_time} minutes")

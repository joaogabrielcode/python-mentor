# Exercise 05 — Email routing
#
# Customer support needs to route complaints to departments based on words in each email
# subject.
# Ask for the email subject.
# If it contains "payment" or "invoice", display "Forwarded to Finance".
# If it contains "delivery" or "delay", display "Forwarded to Logistics".
# Otherwise, display "Forwarded to General Support".

# Your solution:

email_subject = input('What is the email subject?').lower().strip()

if 'payment' in email_subject or 'invoice' in email_subject:
  print('Forwarded to Finance')
elif 'delivery' in email_subject or 'delay' in email_subject:
  print('Forwarded to Logistics')
else:
  print('Forwarded to General Support')

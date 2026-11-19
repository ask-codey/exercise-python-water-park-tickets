# Splash Valley Water Park: prices every ticket for a group, then the group's total.
# Run it with: python tickets.py
#
# The ticket prices:
#   under 3:      free ($0)
#   3 to 12:      $18
#   13 to 64:     $30
#   65 and over:  $20
# On a Saturday or a Sunday, every ticket that isn't free costs $6 more.
# A group is 1 to 8 people.

day = input("What day is your visit? ").strip().lower()
group_size = int(input("How many people are in your group? "))

# Your code goes here, in four steps.
#
# Step 1. While group_size is less than 1 or more than 8, print this line:
#             Groups are 1 to 8 people.
#         and ask again with the same question:
#             group_size = int(input("How many people are in your group? "))
#
# Step 2. Work out whether the visit is at the weekend: day is "saturday" or "sunday".
#
# Step 3. For each person, numbered from 1 to group_size, ask their age with
#             age = int(input(f"How old is person {person}? "))
#         then work out their ticket's price, print the ticket's line, and add the price to the group's total.
#
# Step 4. After every ticket, print the group's total. Its line's number is one more than the group size.
#
# For a Saturday visit by three people aged 35, 8 and 2, the lines are:
# 1) Ticket for age 35: $36
# 2) Ticket for age 8: $24
# 3) Ticket for age 2: $0
# 4) Group total: $60

# Beginning: create variables
sun_points = 0
moon_points = 0


# Middle: ask questions
# question 1:
answer = input ("On a hot sunny day would you rather A) Go to the beach and sun tan, or B) stay in a air-conditioned home?") 
if answer == "A":
    sun_points += 1
elif answer == "B":
    moon_points += 1


# question 2 
answer = input ("Would you rather listen to A) R&B music, or B) rock music?") 
if answer == "A":
    sun_points += 1
elif answer == "B":
    moon_points += 1


# question 3
answer = input ("Would rather wear A) Yellow, or B) Blue?") 
if answer == "A":
    sun_points += 1
elif answer == "B":
    moon_points += 1


# question 4
answer = input ("Would you rather eat A) Waffles, or B) Pancakes?") 
if answer == "A":
    sun_points += 1
elif answer == "B":
    moon_points += 1


# question 5
answer = input ("would you rather wear A) lip gloss, or B) lipstick?") 
if answer == "A":
    sun_points += 1
elif answer == "B":
    moon_points += 1


# End: give results
if sun_points > moon_points:
    print("you are a sun person")
if moon_points > sun_points:
    print("you are a moon person")
    
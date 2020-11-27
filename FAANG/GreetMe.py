name = input() # take only input as this is string

time = int(input()) # take input and convert it to integer

if time >= 0 and time <= 11: # simple if else statements based on problem statement
    print("Good Morning " + name + " sir.")
elif time >= 12 and time <= 15:
    print("Good Afternoon " + name + " sir.")
elif time >= 16 and time <= 23:
    print("Good Evening " + name + " sir.")


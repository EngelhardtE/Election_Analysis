print("Hello World")
x = 10
y = 20
x * y


parents = ["Henry", "Maragret"]
    #Parents[0] or Print(Parents[0]) to get Henry
parents[-1]
parents[:1]


voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})


# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

x = 0
while x <= 5:
    print(x)
    x = x + 1

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)


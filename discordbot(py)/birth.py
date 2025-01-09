# Define birthdays
birthdays = {
    'mama': 'June 11',
    'papa': 'April 22',
    'Ayda_tati': 'November 3',
    'Nina_Tati': 'July 11'
}
months = ['january,','february,','march,','april,','may,','june,','july,','august,','september,','october,','november,','december,']
# Get user input
bd = input("Whose birthday do you want to know? ")

# Check if the input matches any keys in the dictionary
if bd in birthdays:
    print(f"{bd}'s birthday is on {birthdays[bd]}.")
elif bd == 'months':
    print(months)
else:
    print("Sorry, I don't have the birthday information for that person.")


import csv
import sys


# Check if the user entered the right number of arguments or not
if len(sys.argv) != 2:
    raise Exception('You have to enter the file name and only the filename 😃😃')

f = sys.argv[1]
try:
    csv_file = csv.DictReader(open(f, "r"), delimiter=",")
except FileNotFoundError:
    raise Exception('There is no file with this name')

# Prompting the user for the search paramter that he wanna search upon it
user_search_param = input(
    'Please enter your search parameter:(id, title, overview, release_date, popularity, vote_average,vote_count): ')

# Prompting the use for the value he wanna to search for it
user_value = input('Please enter the value: ')


def search_in_csv(file, search_param, value):
    found = False
    for row in file:
        try:
            if value in row[search_param]:
                print(row)
                found = True
        except KeyError:
            return 'The search parameter you entered was invalid.'
    if found:
        return 'Done 👍👍'
    return 'This movie does not exist 🤷‍♀️🤷‍♀️'


print(search_in_csv(csv_file, user_search_param, user_value))

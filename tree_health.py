import csv

#Create a counter dictionary. I will use this to get information on specific columns and their totals.
total_counter = {}

with open('2015StreetTreesCensus_TREES.csv', 'r') as trees_file:
	parsed_csv = csv.reader(trees_file)

	for a_row in parsed_csv:

		#Create a variable for borough names.
		borough_name = a_row[30]

		#This will skip the 'boroname' field so it does not show up in print statement.
		if borough_name == 'boroname':
			continue

		#Here I will use 'pass' to have the counter do nothing and also prevent an error from occuring.
		if borough_name in total_counter:
			pass
		else: 
			# Here I create another dictionary so that I can get the names of all boroughs within another dictionary.
			total_counter[borough_name] = {}

#The below print statement is used to test my code to see if it worked correctly.
# print(total_counter)

		#Create a variable for tree health i.e. "Good" and "Poor".
		tree_health = a_row[8]

		#This will skip the "health" field so it does not show up in print statement.
		if tree_health == 'health':
			continue


		#This will increase the tree health and borough name by 1 for every instance that it occurs.
		if tree_health in total_counter[borough_name]:
			total_counter[borough_name][tree_health] = total_counter[borough_name][tree_health] + 1


		else:
			total_counter[borough_name][tree_health] = 1

# Print total count for borough name and tree health combined.
	print (total_counter)


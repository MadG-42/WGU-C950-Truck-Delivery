import csv
from HashTable import HashMap

with open('Packages.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    insert_into_hash_table = HashMap()  # Calls the HashTable class to create an object of HashTable
    first_truck = []  # list for the first truck
    second_truck = [] # list for the second truck
    third_truck = [] # list for the third truck, which is the first truck out for the second delivery load

# Reads the CSV File 'packages.csv and creates key-value pairs 
# Space-time complexity             O(N)
    for row in readCSV:
        package_ID_value = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip_value = row[4]
        delivery = row[5]
        size = row[6]
        note = row[7]
        delivery_start = ''
        address_location = ''
        delivery_status = 'At hub'
        iterate_value = [package_ID_value, address_location, address, city, state,
                         zip_value, delivery, size, note, delivery_start,
                         delivery_status]

        key = package_ID_value
        value = iterate_value
	    # Sort and enter the list for each truck
        if value[6] != 'EOD':
            if 'Must' in value[8] or 'None' in value[8]:
                first_truck.append(value) 
        #Added 'can only be' and 'delayed' pacakges to the second truck 
        if 'Can only be' in value[8]:
            second_truck.append(value)
        if 'Delayed' in value[8]:
            second_truck.append(value)
        # Change the wrong address package to the correct address
        if '84104' in value[5] and '10:30' not in value[6]:
            third_truck.append(value)
        if 'Wrong address listed' in value[8]:
            value[2] = '410 S State St'
            value[5] = '84111'
            third_truck.append(value)
    # A catch-all to make sure that there are not any packages that were missed from the above.
        if value not in first_truck and value not in second_truck and value not in third_truck:
            if len(second_truck) > len(third_truck):
                third_truck.append(value)
            else:
                second_truck.append(value)
        insert_into_hash_table.insert(key, value)

# Get the full list of values at the beginning of the day
    def get_hash_map():
        return insert_into_hash_table

# Gets the full list for each truck
    def check_first_truck():
        return first_truck

    def check_second_truck():
        return second_truck

    def check_third_truck():
        return third_truck
 
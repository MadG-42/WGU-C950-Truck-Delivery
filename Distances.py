import csv
import datetime

#Opening files ***********************************************************************************
#Reads the CSV file with the names of all the delivery locations
with open('Addresses.csv') as csv_name_file:
    readCSV_name = csv.reader(csv_name_file, delimiter=',')
    readCSV_name = list(name_readCSV_name)

# Reads the CSV file with the map and distances between the delivery locations
with open('Distances.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    readCSV = list(readCSV)

#Time Object for Package.py **********************************************************************
    def check_address():
        return readCSV_name

#Times Trucks Leave the Hub **********************************************************************
#This tells the trucks what time to leave the hub in the morning
    first_truck_time = ['8:00:00']
    second_truck_time = ['9:10:00']
    third_truck_time = ['11:00:00']
	
#List for Each Truck *****************************************************************************
#The creates an empty list for truck for the next part of the program to fill in the correct order 
    first_truck_final= []
    first_truck_final_index_list = []
    second_truck_final = []
    second_truck_final_index_list = []
    third_truck_final = []
    third_truck_final_index_list = []

#Function to Check Distance  - Returns sum *******************************************************
#This function checks the distnaces between two locations
    def check_distances(row_value, column_value, sum_of_distances):
        distances = readCSV[row_value][column_value]
        if distances is '':
            distances = readCSV[column_value][row_value]

        sum_of_distances += float(distances)
        return sum_of_distances

#Function to Check Distance - Reutrns Current Distance *******************************************
    def check_current_distances(row_value, column_value):
        distances = readCSV[row_value][column_value]
        if distances is '':
            distances = readCSV[column_value][row_value]
        return float(distances)

#Checking the time for each Truck ***************************************************************
#This fuction generates the total distance for the first truck
    def check_first_truck_time(distance):
        time_new = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(time_new * 60, 60))
        time_final = distance_in_minutes + ':00'
        first_truck_list.append(time_final)
        truck_distance_sum = datetime.timedelta()
        for i in first_truck_list:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            truck_distance_sum  += d
        return truck_distance_sum 
#This fuction generates the total distance for the second  truck
    def check_second_truck_time(distance):
        time_new = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(time_new * 60, 60))
        time_final = distance_in_minutes + ':00'
        second_truck_list.append(time_final)
        truck_distance_sum = datetime.timedelta()
        for i in first_truck_list:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            truck_distance_sum  += d
        return truck_distance_sum 
#This fuction generates the total distance for the third truck
    def check_third_truck_time(distance):
        time_new = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(time_new * 60, 60))
        time_final = distance_in_minutes + ':00'
        third_truck_list.append(time_final)
        truck_distance_sum = datetime.timedelta()
        for i in first_truck_list:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            truck_distance_sum  += d
        return truck_distance_sum 
		

#Greedy Algorithm **********************************************************************************
#This function finds the shortest distance to travel with the packages in a given truck
#Space-Time Complexity O(N^2)

    def find_shortest_path(truck_distance_list, truck_number, current_location): 
        if len(truck_distance_list) == 0:  
            return truck_distance_list
        else: 
            try:
                lowest_value = 50.0
                next_location = 0
                for index in truck_distance_list:
                    if check_current_distances(current_location, int(index[1])) <= lowest_value:
                        lowest_value = check_current_distancs(current_location, int(index[1]))  
                        next_location = int(index[1])
                for index in truck_distance_list: 
                    if check_current_distances(current_location, int(index[1])) == lowest_value:
#For Truck 1 ********************************
					    if truck_number == 1:
                            first_truck_final.append(index)
                            first_truck_final_index_list.append(index[1])
                            pop_value = truck_distance_list.index(index)
                            truck_distance_list.pop(pop_value)
                            current_location = next_location
#For Truck 2 ********************************
						elif truck_number == 2:
                            second_truck_final.append(index)
                            second_truck_final_index_list.append(index[1])
                            pop_value = truck_distance_list.index(index)
                            truck_distance_list.pop(pop_value)
                            current_location = next_location
                            find_shortest_path(truck_distance_list, 2, current_location)
#For Truck 3 ********************************
                        elif truck_number == 3:
                            third_truck_final.append(index)
                            third_truck_final_index_list.append(index[1])
                            pop_value = truck_distance_list.index(index)
                            truck_distance_list.pop(pop_value)
                            current_location = next_location
                            find_shortest_path(truck_distance_list, 3, current_location)
            except IndexError:
                pass

# Truck 1 ***************************
    first_truck_final_index_list.insert(0, '0')

    def first_truck_final_index():
        return first_truck_final_index_list

    def first_truck_final_list():
        return first_truck_final
#Truck 2 ***************************
    second_truck_final_index_list.insert(0, '0')

    def second_truck_final_index():
        return second_truck_final_index_list

    def second_truck_final_list():
        return second_truck_final
#Truck 3 ***************************
    third_truck_final_index_list.insert(0, '0')

    def third_truck_final_index():
        return third_truck_final_index_list

    def third_truck_final_list():
        return third_truck_final

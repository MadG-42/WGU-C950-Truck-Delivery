from Distances import check_distances
from Distances import check_current_distances
from Distances import check_first_truck_time
from Distances import check_second_truck_time
from Distances import check_third_truck_time
from Distances import find_shortest_path
from Distances import first_truck_final_index
from Distances import first_truck_final_list
from Distances import second_truck_final_index
from Distances import second_truck_final_list
from Distances import third_truck_final_index
from Distances import third_truck_final_list

from ReadCSV import check_first_truck
from ReadCSV import check_second_truck
from ReadCSV import check_third_truck
from ReadCSV import get_hash_map

import datetime
import Distances

#List for each truck 
#Truck 1 ***********
first_truck_delivery_list = []
first_truck_distance_list = []
#Truck 2 ***********
second_truck_delivery_list = []
second_truck_distance_list = []
#Truck 3 **********
third_truck_delivery_list = []
third_truck_distance_list = []


#Times Trucks Leave the Hub ****************************************************************
#This tells the trucks what time to leave the hub in the morning
    first_truck_time = ['8:00:00']
    second_truck_time = ['9:10:00']
    third_truck_time = ['11:00:00']

# the operations below convert the string time into a datetime.timedelta
(h, m, s) = first_truck_time.split(':')
convert_first_truck_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
(h, m, s) = second_truck_time.split(':')
convert_second_truck_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
(h, m, s) = third_truck_time.split(':')
convert_third_truck_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

#Updating Delivery Status *****************************************************************
#This updates the delivery status for each package
#Truck 1 ***********
i = 0  
for value in check_first_truck():
    check_first_truck()[i][9] = first_truck_time
    first_truck_delivery_list.append(check_first_truck()[i])
    i += 1
#Truck 2 ***********
i = 0  
for value in check_second_truck():
    check_second_truck()[i][9] = second_truck_time
    second_truck_delivery_list.append(check_second_truck()[i])
    i += 1
#Truck 3 ***********
i = 0
for value in check_third_truck():
    check_third_truck()[i][9] = third_truck_time
    third_truck_delivery_list.append(check_third_truck()[i])
    i += 1
#Adding Address to List **************************************************************	
# Adds the address to the list
#Truck 1 ***********
try:
    first_truck_count = 0
    for k in first_truck_delivery_list:
        for j in Distances.check_address():
            if k[2] == j[2]:
                first_truck_distance_list.append(j[0])
                first_truck_delivery_list[first_variable_count][1] = j[0]
        first_variable_count += 1
except IndexError:
    pass
#Truck 2 ***********
try:
    second_truck_count = 0
    for k in second_truck_delivery_list:
        for j in Distances.check_address():
            if k[2] == j[2]:
                second_truck_distance_list.append(j[0])
                second_truck_delivery_list[second_variable_count][1] = j[0]
        second_variable_count += 1
except IndexError:
    pass

#Truck 3 ***********
try:
    third_truck_count = 0
    for k in third_truck_delivery_list:
        for j in Distances.check_address():
            if k[2] == j[2]:
                third_truck_distance_list.append(j[0])
                third_truck_delivery_list[third_variable_count][1] = j[0]
        third_variable_count += 1
except IndexError:
    pass
	
#Sorting Packages *************************************************************************
#This uses the greed algorithm to sort the packages into the best order for each truck
#Truck 1  ***********
find_shortest_path(first_truck_delivery_list, 1, 0)
first_truck_total_distance = 0

#Truck 2  ***********
find_shortest_path(second_truck_delivery_list, 2, 0)
second_truck_total_distance = 0

#Truck 3  ***********
find_shortest_path(third_truck_delivery_list, 3, 0)
third_truck_total_distance = 0

#Value through distance function ********************************************************
#Takes the value through distance function 
#Truck 1 ***********
first_truck_package_id = 0
for index in range(len(first_optimized_truck_index())):
    try:
        first_truck_total_distance = check_distances(int( first_truck_final_index()[index]), int( first_truck_final_indexx()[index + 1]), first_truck_total_distance)
        deliver_package = check_first_truck_time(check_current_distances(int(first_truck_final_index()[index]), int(first_truck_final_index()[index + 1])))
        first_truck_final_index()[first_truck_package_id][10] = (str(deliver_package))
        get_hash_map().update(int( first_truck_final_list()[first_truck_package_id][0]), first_truck_delivery_list)
        first_truck_package_id += 1
    except IndexError:
        pass
#Truck 2 ***********
second_truck_package_id = 0
for index in range(len(second_optimized_truck_index())):
    try:
        second_truck_total_distance = check_distances(int(second_truck_final_index()[index]), int(second_truck_final_index()[index + 1]), second_truck_total_distance)
        deliver_package = check_second_truck_time(check_current_distances(int(second_truck_final_index()[index]), int(second_truck_final_index()[index + 1])))
        second_truck_final_list()[second_truck_package_id][10] = (str(deliver_package))
        get_hash_map().update(int(second_truck_final_list()[second_truck_package_id][0]), second_delivery)
        second_truck_package_id += 1
    except IndexError:
        pass
#Truck 3 ***********
third_truck_package_id = 0
for index in range(len(third_optimized_truck_index())):
    try:
        third_truck_total_distance = check_distances(int(third_truck_final_index()[index]), int(third_truck_final_index()[index + 1]), third_truck_total_distance)
        deliver_package = check_third_truck_time(check_current_distances(int( third_truck_final_index()[index]), int( third_truck_final_index()[index + 1])))
        second_truck_final_list()[third_truck_package_id][10] = (str(deliver_package))
        get_hash_map().update(int(second_truck_final_list()[third_truck_package_id][0]), third_delivery)
        third_truck_package_id += 1
    except IndexError:
        pass

#Total Distance ******************************************************************************
#Outputs the total distance for all 3 trucks
def total_distance():
    total_distance = first_truck_total_distance + second_truck_total_distance + third_truck_total_distance
    return total_distance
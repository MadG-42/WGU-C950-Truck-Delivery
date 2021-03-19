# Author: Madison Gish
# Student ID: 00745675
#Title: WGU-UPS

from Packages import total_distances
#Change get_hash_map and carry throughout program "get_hash_table"************ ************* **************** **********
from ReadCSV import get_hash_map
import datetime

class Main:
# User Interface *****************************************************************************************
# when the program is first ran, the user will see this message, and be given different options
    print('Welcome to the WGUPS Package Tracking System! ')
    print('The current route was done in', "{0:.2f}".format(total_distance(), 2), 'miles.')
    choice = input("Here are your options:" 
                  "1 - Track an Individual Package"
				  "2 - Veiw Delivery Status at a Given Time "
				  "3 - Exit the program"
				  "Type the number you selected: ")
# Options ************************************************************************************************ 
# Space Time Complexity      O(N)
    while choice is not '3':
# Options -  1 - Track *********************************************************************************
# If the user selects option 1 , they will be promted to provide the package ID, and a time. The program will 
#output the information for that package at that time
        elif choice == '1':
            try:
                package_ID = input(' Please enter the package ID: ')
                time_one = get_hash_map().get(str(count))[9]
                time_two = get_hash_map().get(str(count))[10]
                time_entered = input('and enter a  time (HH:MM:SS): ')
                (h, m, s) = first_time.split(':')
                convert_time_one = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h, m, s) = second_time.split(':')
                convert_time_two = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
				(h, m, s) = package_status_time.split(':')
                convert_time_entered = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
# First checks if the package has left the hub yet
                if convert_time_one >= convert_time_entered:
                    get_hash_map().get(str(count))[10] = 'At Hub'
                    get_hash_map().get(str(count))[9] = 'Leaving the hub at ' + time_one
                    print('Package ID:', get_hash_map().get(str(count))[0], '   Address:',
                          get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                          get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                          '  Required delivery time:', get_hash_map().get(str(count))[6],
                          ' Package weight (kilos):', get_hash_map().get(str(count))[7], '  Truck status:',
                          get_hash_map().get(str(count))[9], '  Delivery status:',
                          get_hash_map().get(str(count))[10])
                elif convert_first_time <= convert_user_time:
# Then checks if the package has left the hub but has not been delivered yet
                    if convert_time_entered < convert_time_two:
                        get_hash_map().get(str(count))[10] = 'En Route'
                        get_hash_map().get(str(count))[9] = 'Left the hub at ' + time_one
                        print('Package ID:', get_hash_map().get(str(count))[0], '   Address:',
                              get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                              get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                              '  Delivery Deadline::', get_hash_map().get(str(count))[6],
                              ' Package weight (kilos):', get_hash_map().get(str(count))[7], '  Truck status:',
                              get_hash_map().get(str(count))[9], '  Delivery status:',
                              get_hash_map().get(str(count))[10])
# If the package has already been delivered than it displays the time
                    else:
                        get_hash_map().get(str(count))[10] = 'Delivered to location at ' + time_two
                        get_hash_map().get(str(count))[9] = 'Left at ' + time_one
                        print('Package ID:', get_hash_map().get(str(count))[0], '   Address:',
                              get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                              get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                              '  Delivery Deadline:', get_hash_map().get(str(count))[6],
                              ' Package weight (kilos):', get_hash_map().get(str(count))[7], '  Truck status:',
                              get_hash_map().get(str(count))[9], '  Delivery status:',
                              get_hash_map().get(str(count))[10])
#If the user inputs an incorrect value
            except ValueError:
                print('Invalid')
                exit()
# Options -  2 - Time ***********************************************************************************
# If the user selects option 2 , they will be promted to provide a time. The program will output all the packages 
# during the time given. 
        if choice == '2':
            try:
                time_options = input('Please enter a time (HH:MM:SS) : ')
                (h, m, s) = options_time.split(':')
                convert_time_options = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
			    for count in range(1,41):
                    try:
                        time_one = get_hash_map().get(str(count))[9]
                        time_two = get_hash_map().get(str(count))[10]
                        (h, m, s) = first_time.split(':')
                        convert_time_one = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        (h, m, s) = second_time.split(':')
                        convert_time_two = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    except ValueError:
                        pass
# Check which packages are at the hub 
                    if convert_time_one >= convert_time_options:
                        get_hash_map().get(str(count))[10] = 'At Hub'
                        get_hash_map().get(str(count))[9] = 'Leaves at ' + time_one
                        print('Package ID:', get_hash_map().get(str(count))[0], '   Address:',
                              get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                              get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                              '  Delivery Deadline:', get_hash_map().get(str(count))[6],
                              ' Package Weight (kilos):', get_hash_map().get(str(count))[7], '  Truck status:',
                              get_hash_map().get(str(count))[9], '  Delivery status:',
                              get_hash_map().get(str(count))[10])
                    elif convert_time_one <= convert_options_time:
# Check which packages are out but not delivered 
                        if convert_time_options < convert_time_two:
                            get_hash_map().get(str(count))[10] = 'En Route'
                            get_hash_map().get(str(count))[9] = 'Left at ' + time_one
                            print('Package ID:', get_hash_map().get(str(count))[0], '   Address:',
                                  get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                                  get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                                  '  Delivery Deadline:', get_hash_map().get(str(count))[6],
                                  ' Package Weight (kilos):', get_hash_map().get(str(count))[7], '  Truck status:',
                                  get_hash_map().get(str(count))[9], '  Delivery status:',
                                  get_hash_map().get(str(count))[10])
#Check packages that have been delivered and give the delivery info
                        else:
                            get_hash_map().get(str(count))[10] = 'Delivered at ' + time_two
                            get_hash_map().get(str(count))[9] = 'Left at ' + time_one
                            print('Package ID:', get_hash_map().get(str(count))[0], '   Address:',
                                  get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                                  get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                                  '  Delivery Deadline:', get_hash_map().get(str(count))[6],
                                  ' Package Weight (kilos):', get_hash_map().get(str(count))[7],'  Truck status:',
                                  get_hash_map().get(str(count))[9],'  Delivery status:',
                                  get_hash_map().get(str(count))[10])
            except IndexError:
                print(IndexError)
                exit()
#If the user inputs an incorrect value
            except ValueError:
                print('Invalid entry!')
                exit()


# Options - 3 - Exit Program ********************************************************************
        elif choice == '3':
            exit()
        else:
            print('Invalid')
            exit()
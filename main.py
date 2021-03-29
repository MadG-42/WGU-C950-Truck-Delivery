#Author: Madison Gish
#Student ID: 00745675
#Title: WGU-UPS

from ReadCSV import get_hash_map
from Packages import total_distances
import datetime

class Main:
#User Interface *****************************************************************************************
#when the program is first ran, the user will see this message, and be given different options
    print ('Welcome to the WGUPS Package Tracking System! ')
    print ('The current route was done in',
    "{0:.2f}".format (total_distances(), 2), 'miles.') 
#Options ************************************************************************************************ 
#Space Time Complexity      O(N)
    choice = input ("Here are your options:" 
 "\n 1 - Track an Individual Package" 
       "\n 2 - Veiw Delivery Status at a Given Time " 
 "\n 3 - Exit the program" 
       "\n Type the number you selected: ") 
    while choice is not '3':
#Options -  2 - Time ***********************************************************************************
#If the user selects option 2 , they will be promted to provide a time. The program will output all the packages 
#during the time given.    
        if choice == '2': 
            try:
                time_entered = input ('Please enter a time (HH:MM:SS) : ') 
                (h, m, s) =  time_entered.split (':') 
                convert_time_options = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                for count in range (1, 41):
                    try:
                        time_one = get_hash_map ().get (str (count))[9] 
                        time_two = get_hash_map ().get (str (count))[10] 
                        (h, m, s) = time_one.split (':')
                        convert_time_one = datetime.timedelta (hours = int (h), minutes = int (m), seconds = int (s)) 
                        (h, m, s) = time_two.split (':') 
                        convert_time_two = datetime.timedelta (hours = int (h), minutes =int (m), seconds = int (s)) 
                    except ValueError:
                        pass 
        #Check which packages are at the hub 
                    if convert_time_one >= convert_time_options:
                        get_hash_map (). get (str(count))[10] = 'At Hub' 
                        get_hash_map ().get (str(count))[9] = '\nLeaves at ' + time_one 
                        print (' Package ID:', get_hash_map ().get (str (count))[0], '\nAddress:', 
                            get_hash_map ().get (str(count))[2], get_hash_map ().get (str (count))[3],
                            get_hash_map ().get (str(count))[4], get_hash_map ().get (str (count))[5], 
                            '  Delivery Deadline:', get_hash_map ().get (str (count))[6], 
                            '\nPackage Weight (kilos):', get_hash_map ().get (str (count))[7], '\nTruck status:', 
                            get_hash_map ().get (str (count))[9], '\nDelivery status:', 
                            get_hash_map ().get (str (count))[10]) 
        #Check which packages are out but not delivered    
                    elif convert_time_one <= convert_time_options:
                        if convert_time_options <convert_time_two:
                            get_hash_map ().get (str (count))[10] = 'En Route' 
                            get_hash_map ().get (str (count))[9] = '\nLeft at ' + time_one 
                            print (' Package ID:', get_hash_map ().get (str (count))[0], '\nAddress:',
                                get_hash_map ().get (str (count))[2], get_hash_map ().get (str (count))[3],
                                get_hash_map ().get (str (count))[4], get_hash_map ().get (str (count))[5],
                                '  Delivery Deadline:', get_hash_map ().get (str (count))[6], '\nPackage Weight (kilos):',
                                get_hash_map ().get (str (count))[7],'  Truck status:', get_hash_map ().get (str (count))[9],
                                '\nDelivery status:', get_hash_map ().get (str (count))[10]) 
        #Check packages that have been delivered and give the delivery info
                        else: 
                            get_hash_map ().get (str (count))[10] = 'Delivered at ' + time_two 
                            get_hash_map ().get (str (count))[9] = 'Left at ' + time_one 
                            print (' Package ID:', get_hash_map ().get (str (count))[0], '\n   Address:', 
                                get_hash_map ().get (str (count))[2], get_hash_map ().get (str (count))[3], 
                                get_hash_map ().get (str (count))[4], get_hash_map ().get (str (count))[5], 
                                '  Delivery Deadline:', get_hash_map ().get (str (count))[6], 
                                '\n Package Weight (kilos):', get_hash_map ().get (str (count))[7], '\nTruck status:', 
                                get_hash_map ().get (str (count))[9], '\n  Delivery status:', 
                                get_hash_map ().get (str (count))[10]) 
            except IndexError:
                print (IndexError) 
                exit ()
        #If the user inputs an incorrect value
            except ValueError:
                print ('Invalid Time') 
                exit () 
                
#Options -  1 - Track *********************************************************************************
#If the user selects option 1 , they will be promted to provide the package ID, and a time. The program will 
#output the information for that package at that time
        elif choice == '1':
            try:
                count = input('Please enter a package ID to lookup: ')
                first_time = get_hash_map().get(str(count))[9]
                second_time = get_hash_map().get(str(count))[10]
                package_status_time = input('Please enter a time in the HH:MM:SS format: ')
                (h, m, s) = package_status_time.split(':')
                convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h, m, s) = first_time.split(':')
                convert_first_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h, m, s) = second_time.split(':')
                convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                # First checks if the package has left the hub yet
                if convert_first_time >= convert_user_time:

                    get_hash_map().get(str(count))[10] = 'At Hub'
                    get_hash_map().get(str(count))[9] = '\nLeaves at ' + first_time
                    print('Package ID:', get_hash_map().get(str(count))[0], '\nStreet address:',
                          get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                          get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                          '  Required delivery time:', get_hash_map().get(str(count))[6],
                          '\nPackage weight:', get_hash_map().get(str(count))[7], '\nTruck status:',
                          get_hash_map().get(str(count))[9], '\nDelivery status:',
                          get_hash_map().get(str(count))[10])
                elif convert_first_time <= convert_user_time:
                    # Then checks if the package has left the hub but has not been delivered yet
                    if convert_user_time < convert_second_time:
                        get_hash_map().get(str(count))[10] = 'In transit'
                        get_hash_map().get(str(count))[9] = '\nLeft at ' + first_time
                        print('Package ID:', get_hash_map().get(str(count))[0], '\nStreet address:',
                              get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                              get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                              ' Required delivery time:', get_hash_map().get(str(count))[6],
                              '\nPackage weight:', get_hash_map().get(str(count))[7], '\nTruck status:',
                              get_hash_map().get(str(count))[9], '  Delivery status:',
                              get_hash_map().get(str(count))[10])
                    # If the package has already been delivered than it displays the time
                    else:
                        get_hash_map().get(str(count))[10] = 'Delivered at ' + second_time
                        get_hash_map().get(str(count))[9] = '\nLeft at ' + first_time
                        print('Package ID:', get_hash_map().get(str(count))[0], '\nStreet address:',
                              get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                              get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                              '  Required delivery time:', get_hash_map().get(str(count))[6],
                              '\nPackage weight:', get_hash_map().get(str(count))[7], '\nTruck status:',
                              get_hash_map().get(str(count))[9], '\nDelivery status:',
                              get_hash_map().get(str(count))[10])
            except ValueError:
                print('Invalid Look Up Entry')
                exit()
#Options - 3 - Exit Program ********************************************************************
        if choice == '3':
            exit () 
        else:
                exit ()

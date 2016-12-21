'''
Created on Dec 20, 2016

@author: Jay
'''

from collections import Counter

employees = {}

def get_powerball_numbers():
    """
    Calculates the final Powerball numbers by counting duplicates.
    """
    count_duplicates = [Counter([numbers[i] for numbers in employees.values()]) for i in xrange(6)]
    powerball_numbers = [duplicates.most_common(1)[0][0] for duplicates in count_duplicates]
    return powerball_numbers


def start_powerball():
    """
    Play Powerball game.
    """
    while True:

        """
        Print the options for Powerball.
        """
        print "1. Create an entry"
        print "2. Display all entries"
        print "3. Display the final Powerball number"
        print "4. Exit"
        try:
            option = int(raw_input("Select an option: "))
        except:
            print "Please enter a valid option. Try again.\n"
            continue

        if option == 1:
            first_name = raw_input("Enter your first name: ")
            last_name = raw_input("Enter your last name: ")
            fullname = first_name+" "+last_name
            if fullname in employees.keys():
                print "Employee with same name exits. Try again.\n"
                continue
            try:
                suffixes = ["th", "st", "nd", "rd", ] + ["th"] * 16 
                five_number = []
                for i in xrange(1,6):
                    suffixed_num = str(i) + suffixes[i % 100]
                    if i == 1:
                        five_number.append(int(raw_input("Select "+suffixed_num+" number (1 thru 69): ")))
                    else:
                        five_number.append(int(raw_input("Select "+suffixed_num+" number "+"(1 thru 69 excluding("+ str(five_number).strip('[]') +"): ")))
                powerball_num = int(raw_input("Enter Powerball number (1 thru 26): "))
                for num in five_number:
                    assert(num in xrange(1, 70))
                assert(len(five_number) == len(set(five_number)))  
                assert(powerball_num in xrange(1, 27)) 
            except:
                print "Please enter a valid input. Try again.\n"
                continue
            numbers = five_number + [powerball_num]
            employees[fullname] = numbers

        elif option == 2:
            if not employees:
                print "Please create an entry.\n"
            else:
                print "Powerball entries are: "
                for fullname, numbers in employees.iteritems():
                    print fullname + " " +'{} Powerball: {}'.format(str(numbers[0:5]).strip('[]'),numbers[5])
                print ""

        elif option == 3:
            final_powerball_numbers = get_powerball_numbers()
            print "The final Powerball numbers are: \n\n" +'{} Powerball: {}'.format(str(final_powerball_numbers[0:5]).strip('[]'),final_powerball_numbers[5])
            print ""

        elif option == 4:
            exit(0)

        else:
            print "Please enter a valid option. Try again.\n"
            continue


if __name__ == "__main__":
    try:
        start_powerball()
    except KeyboardInterrupt:
        exit(0)
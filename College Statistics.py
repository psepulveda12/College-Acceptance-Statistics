# Peter Sepulveda - 1/23/2019
# User enters in College name and high school graduation year, and will be shown the number of applicants,
# the number of students accepted, the number enrolled, and the acceptance and enrollment rates.


def college_matcher(name: str, actual: str):
    """
    Goes through different functions to see if there is a match
    :param name: str
    :param actual: str
    :return: match : bool
    """
    if name.lower() == actual.lower():
        return True
    elif acronym(name, actual):
        return True
    elif univ(name, actual):
        return True
    elif tech(name, actual):
        return True
    elif special(name, actual):
        return True
    else:
        return False


def acronym(name: str, actual: str):
    """
    Gets uppercase letters to determine acronym of college
    :param name: User entered name of college
    :param actual: Full name of college from csv files
    :return: match : bool; True if user entered name matches name in csv
    """
    college: str = ""
    for letter in actual:
        if letter.isupper():
            college += letter
    if college.lower() == name.lower():
        return True
    return False


def univ(name: str, actual: str):
    """
    Handles colleges with 'University' in the name
    :param name: User entered name of college
    :param actual: Full name of college from csv files
    :return: match : bool; True if user entered name matches name in csv
    """
    if "University of " in actual:
        short: str = actual[14:]
        if short.lower() == name.lower():
            return True
    if " University" in actual:
        short: str = actual[:-11]
        if short.lower() == name.lower():
            return True
    return False


def tech(name: str, actual: str):
    """
    Handles colleges with technical names
    :param name: User entered name of college
    :param actual: Full name of college from csv files
    :return: match : bool; True if user entered name matches name in csv
    """
    if actual[0:10].lower() == "california":
        actual = "Cal" + actual[10:]
    if " Institute of Technology" in actual:
        short: str = actual[:-23] + " Tech"
        if short.lower() == name.lower():
            return True
    if " Polytechnic Institute and State University":
        short: str = actual[:-43]
        if (short + " Poly").lower() == name.lower():
            return True
        if (short + " Tech").lower() == name.lower() or acronym(name, (short + " Tech")):
            return True
    return False


def special(name: str, actual: str):
    """
    Handles special cases tht cannot be accounted for in above cases
    :param name: User entered name of college
    :param actual: Full name of college from csv files
    :return: match : bool; True if user entered name matches name in csv
    """
    if name.lower() == "nova" and acronym("NVCC", actual):
        return True
    if name.lower() == "uva" and univ("Virginia", actual):
        return True
    if name.lower() == "pitt" and univ("Pittsburg", actual):
        return True
    return False


# Obtain name of college and HS graduation year
college_name: str = str(input("Enter name of College or University: "))
year: str = input("Enter High School Graduation Year (2015-2018): ")

# Sets initial parameters
match: bool = False
found: bool = False
full_name: str = ""
applicants: int = 0
accepted: int = 0
enrolled: int = 0
acceptance_rate: int = 0
enrollment_rate: int = 0

# File names all in format of 'Acceptance 201#.csv'
fileName: str = "Acceptance " + year + ".csv"

# Exception handling if incorrect/unavailable year inputted
try:
    # Opens and reads file
    file = open(fileName, 'r')
    # Year is valid and opens a CSV
    found = True
    # Each line has data for one college
    for line in file:
        # Format is: college, applied, accepted, enrolled
        data = line.split(',')
        # CSV file uses full college name
        full_name = data[0]
        # Calls match function to determine whether user input matches one of the colleges in the csv file
        match = college_matcher(college_name, full_name)
        if match:
            # CSV all string so need to convert to int for future calculations
            applicants = int(data[1])
            accepted = int(data[2])
            enrolled = int(data[3])
            # Cannot have divide by zero
            if accepted != 0:
                acceptance_rate = round(accepted / applicants * 100, 2)
                enrollment_rate = round(enrolled / accepted * 100, 2)
            # Adds extra space for display purposes
            print('\n\n\n\n\n\n')
            # Program prints college statistics of user input
            print(full_name + ' (' + year + "):\n" + "Applicants: " + str(applicants) + "\n" + "Accepted: " + str(
                accepted) + "  |  " + str(acceptance_rate) + "%\n" + "Enrolled: " + str(enrolled) + "  |  " + str(
                enrollment_rate) + "%")
            # Exit for loop after match has been found
            break
# Exception caused by incorrect user input for year due to lack of CSV info
except FileNotFoundError:
    print('\nEnter year between 2015-2018')

# Either user entered college name is not in list or system cannot process custom school name
if not match and found:
    print('\nEither not enough data for college, or college incorrectly entered into system')

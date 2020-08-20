# Importing json module to load the input .json file
import json
# Importing the re module to use regular expressions to detect integers in strings
import re


def test_string(value):
    """ Check if the input string type is clean according to our requirements
    
    :param value: Input string type value to be checked
    :return: 
    """

    # Checking if the string is an empty string
    assert len(value) > 0
    # Checking if there is any other character in input string other than integers
    assert not re.findall(r'[-+]?[0-9]+', value)


def test_integer(value):
    """ Check if the input integer type is clean (not a 0)
    
    :param value: Input integer value to be checked
    :return: 
    """
    
    # Checking if the integer is a 0
    assert value != 0


def test_list(lst):
    """ Check if the input list type is clean according to our requirements
    
    :param lst: Input list to be checked
    :return: 
    """

    # Checking if the list is empty
    assert len(lst) > 0
    # Expanding all the items in the list
    for value in lst:
        # Checking the integer/float type values using test_integer(value)
        if type(value) in [float, int]:
            test_integer(value)
        # Checking the string type values using test_string(value)
        elif type(value) == str:
            test_string(value)
        # Checking the list type values using test_list(value)
        elif isinstance(value, list):
            test_list(value)
        # Checking the dictionary type values using test_dict(value)
        elif isinstance(value, dict):
            test_dic(value)


def test_dic(dic):
    """ Check if the input dictionary type is clean according to our requirements
    
    :param dic: Input dictionary to be checked
    :return: 
    """

    # Checking if the dictionary is empty
    assert len(dic) > 0
    # Parsing through all the dictionary values
    for value in dic.values():
        # Checking the integer/float type values using test_integer(value)
        if type(value) in [float, int]:
            test_integer(value)
        # Checking the string type values using test_string(value)
        elif type(value) == str:
            test_string(value)
        # Checking the list type values using test_list(value)
        elif isinstance(value, list):
            test_list(value)
        # Checking the dictionary type values using test_dict(value)
        elif isinstance(value, dict):
            test_dic(value)


def main():
    # Opening the out.json file for reading
    with open('result.json', 'r') as f:
        # Read JSON encoded data from a file and convert it into Python dictionary.
        test_dic(json.load(f))
        # Print the success message if all values are clean 
        print(u'\u2705 Test Ran Successfully')


# Starting the program from main()   
if __name__ == "__main__":
    main()
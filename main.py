# Importing json module to load the input JSON file
import json
# Importing the re module to use regular expressions to detect integers in strings
import re
# Importing the pprint module to print the output on stdout in a JSON format
import pprint 
# Importing sys module to read the input JSON file from stdin
import sys

def process_string(string_value):
    """ Processes the input string type value 
    
    :param value: Input string type value to be processed
    :return: returns the most extreme integer component in input string
    """

    # Extracting all the integers from the input string 'value'
    result = re.findall(r'[-+]?[0-9]+', string_value)
    
    # If there are integers present in our input string, then return the maximum amongst all those integers
    if result:
        # Returning the most extreme integer component of input string
        return max([int(x) for x in result])
    
    # If there is no integer component present in the input string, then return the original input string
    return string_value


def process_list(lst):
    """ Processes the input list
    
    :param lst: Input list to be processed
    :return: returns processed list
    """

    # creating a new list to store processed list
    ret = []

# Expanding the items in list (i->index of item), (value->list item)
    for i, value in enumerate(lst):
        # If value is of type integer or float and is equal to 0, then pop it from the list
        # If value is an empty Array, empty Object, empty string, then pop it from the list
        if (type(value) in [int, float] and value == 0) or not value:
            continue
        # If the value is of type string, make a call to process_string(value) to clean the string and append the cleaned string in our return list
        elif isinstance(value, str):
            ret.append(process_string(value))
        # If the value is of type list, make a recursive call to process_list(lst)
        elif isinstance(value, list):
            processed_list = process_list(value)
            # If the processed_list is not empty, then append it to our return list
            if processed_list:
                ret.append(processed_list)
        # If the value is of type dictionary, make a call to process_dictionary(dic) to process the dictionary
        elif isinstance(value, dict):
            processed_dictionary = process_dictionary(value)
            # If the processed dictionary is not empty, append it to our return list
            if processed_dictionary:
                ret.append(processed_dictionary)
        # Add the element to the return list otherwise, as it needs no cleaning
        else:
            ret.append(value)
    
    # Return the list holding the processes/cleaned input values
    return ret


def process_dictionary(dic):
    """
    :param dic: Input dictionary to be processed
    :return: returns processed dictionary
    """

    # Used list here, because size changes during executing as dictionary is modified in place
    for key, value in list(dic.items()):
        # If value in interger or float and is equal to 0 -> pop
        # OR Empty Array, Empty Object, empty string -> pop
        if (type(value) in [int, float] and value == 0) or not value:
            dic.pop(key)
        # If the value is of type dictionary, make a recursive call to process_dictionary(dic)
        elif isinstance(value, dict):
            process_dictionary(value)
        # If the value is of type string, make a  call to process_string(value) to clean the string
        elif isinstance(value, str):
            dic[key] = process_string(value)
        # If the value is of type list, make a  call to process_list(lst) to parse the list and clean the values
        elif isinstance(value, list):
            processed_list = process_list(value)
            # Update the original dictionary with the processed list if the processed list is not empty and therefore has some key/value pairs
            if processed_list:
                dic[key] = processed_list
            # If the list after processing is empty, then remove the key corresponding to that original list value
            else:
                dic.pop(key)
    
    # Returning final processed output
    return dic


def main():
    # Opening the sample_input.json file for reading
    # with open('sample_input.json', 'r') as f:
        # Read JSON encoded data from a file and convert it into Python dictionary.
        # dic = json.load(f)

        # Read the json file from stdin       
        dic = json.load(sys.stdin)
        # Process the python dictionary containing .json data 
        processed_dict = process_dictionary(dic) 
        # Print the modified JSON to stdout in a nice format using pprint module
        pprint.pprint(processed_dict, indent=4, sort_dicts=False)
    
        # Uncomment lines 115, 117 to create a result.json in project directory containing proccessed JSON 
        # Opening a result.json file for writing
        # with open('result.json', 'w') as fp:
            # Convert the processed python dictionary to a JSON file
            # json.dump(processed_dict, fp, indent=2)


# Starting the program from main()   
if __name__ == "__main__":
    main()
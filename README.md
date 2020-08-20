# JSON-Data-Cleaner

This program reads a valid JSON file, modifies it as follows and prints the resulting JSON to stdout:
- Keys with a value of 0 or "", empty arrays, and empty objects are removed such that the final result is free of these items.
- For only the value part of each key:value pair (keys should not be changed):
If a string contains one or more embedded integer components, replace that string with a number consisting of the most extreme integer component.

# Notes/Assumptions

- The entire JSON data structure consists only of objects, arrays, numbers and strings
- Strings do not have any mathematical significance and may contain any values ("cbgva + 5" = 5)
- Commas should not be treated as part of integer components (" 1,234 " = 234)
- Decimal should not be treated as part of integer components (" 1.234 " = 234)
- Integer components within strings may be negative ("-1" = -1)
- The comparison is done based on the signed integers inside a string ("-1.2" = 2)


# Requirements:
![npm package](https://img.shields.io/badge/Python-3.8-brightgreen.svg)
The program will only run in python version 3.8 or latest. 

# Running
- Open/Unzip the folder containing all the files
- Open terminal in project directory and run

```sh
$ python main.py < sample_input.json
```
The processed/cleaned JSON is displayed on stdout

# Testing
If you want to create a processed/clean JSON file in the project directory, uncomment the line 115, 117 in main.py. Uncommenting those two lines would create a result.json file in the project directory. Run the following commands in terminal:

```sh
$ python main.py < sample_input.json
$ python test.py
```
If all the test cases pass, the message ' Test Ran Sucessfully' will be displayed.

# Summary
The program reads the JSON file from stdin and converts it into a python dictionary and processes all the key:value pairs and cleans the values according to the following criteria:

- Keys with a value of 0 or "", empty arrays, and empty objects are removed such that the final result is free of these items.
- For only the value part of each key:value pair (keys should not be changed):
If a string contains one or more embedded integer components, replace that string with a number consisting of the most extreme integer component.

Since the json file consists only of objects, arrays, numbers and strings, this programs handles the each data type in a separate function. 

- If the value is an integer/float, then we check if it is 0, if yes remove that key:value pair. If not, then we can keep that value as it is and process the next key:value pair. 

- If the string is an empty string, the program removes the specific key:value pair. If the value is a non-empty string, we pass it to a helper function responsible for processing string types. We find all the integers embedded inside that string using regular expressions and select the largest amongst all. And if no integers are found inside that string, we simply return that string.

- If the value is a list type, we pass it to a helper function responsible for processing list types. We expand the list items and determine the data type of each list item and pass it to other helper functions accordingly depending on their data type. If the list is a nested list, we make the recursive call to our function for processing list types.
 
- If the value is a dictionary type, we pass it to a helper function responsbile for processing  dictionary types. We expand the dictionary key:value pairs and determine the data type of each dictionary value and pass it to other helper functions accordingly depending on their data type. If the dictionary is a nested dictionary, we make the recursive call to our function for processing dictionary types.

The program explicity checks the return from helper functions and if at any point finds an empty value, we delete that specific key:value pair. 


For the test file (test.py), the program reads the result.json file from our project directory and processes all the key:values pairs and checks if they do not meet our criteria. So if we have any keys with a value of 0 or "", empty arrays, empty objects, strings containing integers, then the program throws an error. If not the program displays the message 'Test Ran Successfully'

# Alternative Method 
The other alternative approach to this problem could have been cleaning the string values by iterating over the individual characters of a string type value and extracting all the integers and then selecting the maximum integer amongst all. But we used regular expressions to solve that problem. 

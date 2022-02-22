with open('/Users/tony.ruppert/Documents/GitHub/python-projects/Files_and_Exceptions/pi-digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())
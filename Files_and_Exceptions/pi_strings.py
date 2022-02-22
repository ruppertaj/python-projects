filename = '/Users/tony.ruppert/Documents/GitHub/python-projects/Files_and_Exceptions/pi-digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
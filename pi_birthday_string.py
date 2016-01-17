filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string[:52] + "...")
print(len(pi_string))

birthday = raw_input("Enter your birhtday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
    index = pi_string.index(birthday)
    print ("Starting at position: " + str(index))
#    print (pi_string[index:index+6])
else:
    print("Your birthday does not appear in the first million digits of pi.")

#teller = 1

#print(teller, len(pi_string))

#while birthday in pi_string[teller:]:
#    teller = pi_string[teller:].index(birthday)
#    print(teller)
#    if teller == 0:
#        break

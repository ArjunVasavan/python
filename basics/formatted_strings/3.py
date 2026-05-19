course = 'Hi this is Arjun How Are you'
print(len(course))

print(course.upper())  # changes everything to upper case 

print(course.lower())  # this is an method which changes everything to lower 

print(course)  # course variable will be still on its original form 

if ( course[0].isupper() ) :
    print("0th index it upper")

print(course.find('Are'))  # show staring index 

print(course.find('z'))  # shows -1 if not present 

print(course.replace('Arjun','Vasavan'))

print(course)  # old is still there 

  # if string contains word python check 

print('Arjun' in course)  # prints boolian true 
print('Ammu' in course)  # prints boolian false 

general_len  = len(course)
print(general_len)

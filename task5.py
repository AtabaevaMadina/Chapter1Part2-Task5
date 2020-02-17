import math


students1 = int(input('students in classroom-A '))
students2 = int(input('students in classroom-B '))
students3 = int(input('students in classroom-c '))
desks1 = students1/2
desks2 = students2/2
desks3 = students3/2
total = desks2 + desks1 + desks3
print(math.ceil(total))


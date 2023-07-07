import datetime
from math import *

start_time = datetime.datetime.now()

code = """
import datetime
from math import *

start_time = datetime.datetime.now()

def calculate(y, x):
    I = (2.33*(log(1 + cos(y**0.5)))/exp(y)+sin(y)**2)
    return round(I, 4)

y = eval(input('у-шамасының мәні: '))
x = eval(input('х-шамасының мәні: '))

result = calculate(y, x)

# Write the result to a file
with open('output.txt', 'w') as file:
    file.write('Your answer is: ' + str(result))

# Read the result from the file
with open('output.txt', 'r') as file:
    contents = file.read()

print(contents)
print(datetime.datetime.now() - start_time)
"""

# Write the code to a file named "yerasyl.py"
with open('yerasyl.py', 'w') as file:
    file.write(code)

# Read the code from the file and execute it
with open('yerasyl.py', 'r') as file:
    exec(file.read())

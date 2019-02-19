firstNumber = 26
someString = 'Text goes here.'
print("Foo" + "Bar")
computed_num = 3*7+22-8
some_list = []
some_list.append("Test data")
my_dict = {}
my_dict['appendage001'] = 'leg'
my_dict['appendage002'] = 'arm'
print(my_dict['appendage001'])
type(my_dict)
type(5)
type('Testing')

for q in range(10):
    print(q)

numberCollection = [4, 5, 6]
for counter in numberCollection:
    print(counter)

whileCounter = 8
while whileCounter > 0:
    print(whileCounter)
    whileCounter -= 1

ctr03 = 8
while True:
    print(ctr03)
    if ctr03 <= 0:
        break
    ctr03 -= 1

ctr04 = 4
while ctr04 > 0:
    if ctr04 > 1:
        print('Greater than 1')
    elif ctr04 > 3:
        print('Greater than 3')
    else:
        print('Less than 1')
    ctr04 -= 1

ctr05 = 20
while ctr05 > 0:
    if ctr05 > 15:
        print('GT 15')
    else:
        print('Less than 20')
    if ctr05 == 12:
        break
    ctr05 -= 1


def my_function():
    i = 8
    if i > 0:
        print("i is greater than zero")
    elif i < 4:
        print("i is between 0 and 4")
    else:
        print("i is greater than or equal to four")


def new_function(a, b):
    return a+b


print(new_function(9, 3))


def subtraction_function(num1, num2):
    return num1 - num2


num3 = 50
while num3 > 0:
    print(num3)
    num3 = subtraction_function(num3, 1)



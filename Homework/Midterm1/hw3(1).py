# input

number = int(input())
list_number = list()
numberprint = str()

# add to 4 numbers
if 100 <= number < 1000:
    number = number * 10
elif 10 <= number < 100:
    number = number * 100
elif number < 10:
    number = number * 1000

# to take 6174 into account
if number == 6174:
    numberprint = 6174

# calculate
while number != 6174:

    # add to 4 numbers
    if 100 <= number < 1000:
        number = number * 10
    elif 10 <= number < 100:
        number = number * 100
    elif number < 10:
        number = number * 1000

    # seperate each number
    one = number // 1000
    two = number % 1000 // 100
    three = number % 100 // 10
    four = number % 10

    # seperate each number and storage them in a list
    list_number = [one, two, three, four]

    # sort numbers from min to max
    list_sort = sorted(list_number)

    # calculate min number and max number
    min_num = int(list_sort[0]) * 1000 + int(list_sort[1]) * 100 + int(list_sort[2]) * 10 + int(list_sort[3]) * 1
    max_num = int(list_sort[3]) * 1000 + int(list_sort[2]) * 100 + int(list_sort[1]) * 10 + int(list_sort[0]) * 1

    # calculate the number
    number = max_num - min_num

    # result
    if number != 6174:
        numberprint = numberprint + str(number) + ","
    elif number == 6174:
        numberprint = numberprint + str(number)

print(numberprint)
# 1.split
'''every string has a method called split, and the split methodallows us to generate a list from 
string by spliting the string at a specific character
numbers = "5,12,45,1,9"   # '5,12,45,1,9'
numbers.split(",")  #["5","12","45","1","9"]

# 2.List Comprehension:
number_user= "1,2,3,4,5,6"
numbers = number_user.split(",") 
print(numbers)

user_numbers_as_int = []
for number in numbers:
    user_numbers_as_int.append(number)
print(user_numbers_as_int)

a = [number for number in numbers] # i'm going to put in this list number where number is each element
#in numbers
print(a)
b = [int(number) * int(number) for number in numbers]
print(b)
'''
# 3.Set : like a list but without order and duplicate

### the ex2 ###
# User can pick 6 number
# Lottery calculate 6 rtandom numbers(between 1 and 20)
# Then we match the user numbers to the lottery numbers
# Calculate the winings based on how many numbers the user matched

# 1. User can pick 6 number
import random

def menu():
    # Ask player for a number
    user_numbers = get_player_numbers()
    # Calculate lottery number
    lottery_numbers = create_lottery_numbers()
    # Print out the winnings
    matched_numbers = user_numbers.intersection(lottery_numbers)
    print('You won ${}!'.format(100 ** len(matched_numbers)))
    
    

def get_player_numbers():
    number_csv = input('Enter your 6 numbers, seperated by commas: ') # csv: comma seperate value
    numbers_list = number_csv.split(',')
    integer_set = {int(number) for number in numbers_list}
    return integer_set

# 2. Lottery calculate 6 random numbers(between 1 and 20)

def create_lottery_numbers():
    values = set()
    # we must run it untill we have 6 number in the set , so we will use the while loop not the for
    while len(values) < 6:
        values.add(random.randint(1, 20))
    return values
#print(create_lottery_numbers())    
#print(get_player_numbers())
menu()    


















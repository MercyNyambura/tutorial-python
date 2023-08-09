"""calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    
def validate_and_execute():
 # try and except
        try:
            user_input_number = int(num_of_days_element)
            if user_input_number > 0:
                calculated_value = days_to_units(user_input_number)
                print(calculated_value)
            elif user_input_number == 0:
                  print("You entered a 0, please put a valid positive number!")
            
            else:
                print("you entered a negative number, no conversion for you!")
               
        except ValueError:
            print("Your input is not a number. Don't ruin my program!")
# while loop
user_input = ''
while user_input != "exit":
    user_input = input("Hey user, enter a number of days and i will convert into hours!\n")
    list_of_days = user_input.split(", ")

    # for loop
    for num_of_days_element in set(user_input.split(", ")):  
        validate_and_execute()

validate_and_execute()
days_to_units()"""



"""a = 4
def polynomial(a,b,c,x):
    return a*x**2 + b*x + c

b = a
b *= a
c = 1
result = polynomial(a, b, c, 0)
a += 3
a = 0
print(a, b, c)"""

#.startswith


"""num = {'one': 1, 'two': 3}
print(num)

num['two'] = 2 
print(num)"""


"""a = ['a', 'b', 'c'] == ['c', 'a', 'b']
print(a)"""

"""colors = []
colors.append('red')
colors.append('green')
colors.append('yellow')
print(colors)"""

"""if 'bar' in{'foo': 1, 'bar': 2, 'baz': 3}:
    print(1)
    print(2)
    if 'a' in 'qux':
        print(3)
print(4)"""


"""d = {'a': 0, 'b': 1, 'c': 0}

if d['a'] > 0:
    print('yeah!')
elif d['b'] > 0:
    print('yeah!')
elif d['c'] > 0:
    print('ok')

elif d['d'] > 0:
    print('ok')

else:
    print('not ok')"""

"""a = ['foo', 'bar', 'baz', 'qux', 'corge']

while a:
    if len(a) < 3:
        break
    print(a.pop())

print('done.')"""

#import numpy as np
"""import random


def generate_lottery_tickets(N):
    lottery_tickets = set()
    
    while len(lottery_tickets) < N:
        ticket_number = random.randint(0, 999)
        lottery_tickets.add(ticket_number)
    
    return lottery_tickets

# Generate 10 unique lottery tickets
tickets = generate_lottery_tickets(10)
print(tickets)"""



'''import random

num_experiments = 5
num_total_throws = 10000
num_subsample_throws = 1000

m_total = 0
n_total = 0

for _ in range(num_experiments):
    six_count = 0
    four_count = 0

    # Simulate throwing a normally-balanced die 10,000 times
    throws = [random.randint(1, 6) for _ in range(num_total_throws)]

    # Select a random subsample of 1,000 throws
    subsample = random.sample(throws, num_subsample_throws)

    # Count the occurrences of six and four in the total throws and subsample
    six_count = throws.count(6)
    four_count = subsample.count(4)

    m_total += six_count
    n_total += four_count

# Calculate the average values of m and n over the experiments
m_avg = m_total / num_experiments
n_avg = n_total / num_experiments

print("Average number of times six appears in 10,000 throws (m):", m_avg)
print("Average number of times four appears in 1,000-subsample (n):", n_avg)'''


def func(a):
    a += 10
    return a
func(a)
def main():
    x=5
    y=func(x)
    x+=y
    print(x)
main()















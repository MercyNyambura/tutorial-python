"""from datetime import date
import csv

dt = date.today()
#dt = dt.strftime("%d/%m/%y")

filename = "test.csv"

with open(filename, 'w', newline = "") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow([dt])
    file.close()


my_list = ["January", "February", "March"]
print(my_list)
my_list.extend(["april", "may","june"])
print(my_list)"""




#time till deadline

from datetime import datetime

user_input = input("Enter your goal with a deadline separated by a colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%")

print(input_list)
from datetime import datetime


lines = [line.rstrip('\n') for line in open('deadline.txt')]

date_obj = []
for i in lines:
    date_obj.append(datetime.strptime(i, '%b %d %Y %I:%M%p'))

input_date = input("Input DeadLine of Task in the format Month(Words) day Year hour:MinutesAM/PM: ")
input_date = datetime.strptime(input_date, '%b %d %Y %I:%M%p')
deadline = 0
for i in date_obj:
    if i > input_date:
        deadline=deadline+1

print("Students who were Overdue the deadline were " + str(deadline))
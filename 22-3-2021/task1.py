from datetime import datetime

mydict = {}
lines = []

lines = [line.rstrip('\n') for line in open('timetable.txt')]

j=0
z = []
list = []
i=0

while i <= len(lines)-1:
    list = []
    if not lines[i][0].isnumeric():
        if j < len(lines)-1:
            j = j + 1
        while lines[j][0].isnumeric() and j < len(lines):
            list.append(lines[j])
            if j < len(lines)-1:
                j = j + 1
            else:
                break
        mydict[lines[i].strip(':')] = [x for x in list]
    i = i + 1

print("A) Time Spent in Class per week is: " + str(sum(map(len, mydict.values()))*1.5) + " Hours")

correct = True

word = input("Entered Day you want: ")
original = word

if word.lower() == "monday":
    word = "Mon"
elif word.lower() == "tuesday":
    word = "Tue"
elif word.lower() == "wednesday":
    word = "Tue"
elif word.lower() == "thursday":
    word = "Tue"
elif word.lower() == "friday":
    word = "Tue"
else:
    correct = False

if correct:
    print("Time Spent in Class on " + original + " is " + str(len(mydict[word])*1.5) + " Hours")
elif original.lower() == "saturday" or original.lower() == "sunday":
    print("No classes on weekends!")
else:
    print("You Entered an invalid Day")


# for x in mylist:

mylist = []
for key in mydict.keys():
    mylist.append(mydict[key])

list = [item for sublist in mylist for item in sublist]
subject = input("Enter Subject: ")
count = 0

for x in list:
    if (x[12:].lower() == subject.lower()):
        count = count + 1


print("You Spend " + str(count*1.5) + " Hours on " + subject)


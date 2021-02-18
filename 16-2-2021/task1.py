# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



sum = 0
all = []
answer = 0

while True:
    num = input("Enter number: ")
    sum += float(num)
    all.append(int(num))

    if sum == 0:
        for i in all:
            answer += i ** 2
        print(answer)
        break

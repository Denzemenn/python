# x = ["Matthew", "Anthony", "John"]
# x.append("Jack")
# x.append("Josh")
# if len(x) == 3:
#     print(3)
# elif len(x) == 4:
#     print("Did you add anything here?")
# else:
#     print("There is neither 3 or 4")
# month = int(input("Enter number of the month: "))
# if month <= 1 month <= 12
#     if month <= 3 month <= 5:
#         print("Spring")
#     elif month <= 6 month <= 8:
#         print("Summer")
#     elif month <= 9 month <= 11:
#         print("Autumn")
#     else:
#         print("Winter")
# else:
# print("This month is unexistent do from 1 to 12")

# h = int(input("Hours: "))
# m = int(input("Minutes: "))
# s = int(input("Seconds: "))
# if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
#     print("Format is right")
# else:
#     print("Format isn't right")
#     if h < 0 or h > 23:
#         print("Hours aren't right [from 0 to 23]")
#     if m < 0 or m > 59:
#         print("Minutes aren't right [from 0 to 59]")
#     if s < 0 or s > 59:
#         print("Seconds aren't right [from 0 to 59]")

count = 0
q1 = input("Какая по счёту планета Земля от солнца \n"
               "a) 2, b) 3, c) 4, d)5\n"
               "--> ")
if q1 == "b":
    count = count + 1
else:
    print("Wrong:(")
    print("You got 0 points")
    quit()
q2 = input("Сколько позвонков у человека?\n"
           "a) 8, b) 10, c) 12, d) 14\n"
           "--> ")
if q2 == "d":
    count = count + 1
else:
    print("Wrong:(")
    print("You got 1 point")
    quit()
q3 = input("Сколько персонажей в Dota 2?\n"
            "a) 95, b) 107, c) 124, d) 121\n"
            "--> ")
if q3 == "d":
    count = count + 1
else:
    print("Wrong:(")
    print("You got 2 points")
    quit()








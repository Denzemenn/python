# # # # # #
# # # # # #
# # # # # # if x >= 10: and x == 0 or x == 666:
# # # # # #     print("нет")
# # # # # # else:
# # # # # #     print("я тоже")
# # # # # # #
# # # # # # # phrase = "я карта"
# # # # # # # if phrase == "ya karta":
# # # # # # #     print("ы карты")
# # # # # # #
# # # # # # # game = "dota2"
# # # # # # # if game = "brawl stars":
# # # # # # #     pr
# # # # #
# # # # # number = int(input("введите число: "))
# # # # # if number >0:
# # # # #    print("пщложительное")
# # # # # elif number == 0:
# # # # #     print("0")
# # # # # else:
# # # # #     print("Отрицательное")
# # # # year = int(input("введите год: "))
# # # # if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
# # # #     print("високосненько")
# # # # else:
# # # #     print("не високосненько :(")
# # # number_1 = int(input("введите первое число:"))
# # # operation = input("введите операцию(-,+,*,/):")
# # # number_2= int(input("введите второе число:"))
# # # lst = ["-" , "+", "*","/"]
# # #
# # # if operation in lst:
# # #     if operation == "-":
# # #         print(number_1 - number_2)
# # #     elif operation == "+":
# # #         print(number_1 + number_2)
# # #     elif operation == "*":
# # #         print(number_1 * number_2)
# # #     else:
# # #         print( number_1 / number)
# # # else:
# # #     print("Ne to")"= int(input(
# #
# # number_1 = int(input("введите первое число:"))
# # number_2= int(input("введите второе исло:"))
# # number_3= int(input("введите третие число:"))
# # if numbr_2
#  number_1 = int(input("введите первое число:"))
#  number_2= int(input("введите второе исло:"))
#  number_3= int(input("введите третие число:"))
#
# lst = [nuumber_1, number_2, number_3]
#
# maxi = max(lst)
# mini = min(lst)

ticket = input("введите номер билета(6 знаков):")
if len(ticket) == 6:
    first_half = ticket[:3]
    last_half = ticket[-3:]

    first_sum =  first_half[0] + first_half[1] + first_half[2]
    fast_sum =  first_half[0] + first_half[1] + first_half[2]

    if first_sum == last_sum:
        print("счастливый билет")
    else:
        print("не повезло")
else:
    print("ведите правельно")
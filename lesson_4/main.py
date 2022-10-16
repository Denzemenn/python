x = "C:Python3/python.exe"

print("имя: ", x[11:22])
print("имя: ", x[-10:])
print("расширение: ", x[-3:])
print("имя каталога:", x[3:10])
print("полный путь к каталогу: ", x[0:10])
print("полный путь к каталогу: ", x[:10])

x1 = x.split("\\")
print(x1)
print("имя: ", x1[2])
chapter_1 = input("Chapter 1: ")
page_1 = input("Page: ")
chapter_2 = input("Chapter 2: ")
page_2 = input("Page: ")
chapter_3 = input("Chapter 3: ")
page_3 = input("Page: ")

print(chapter_1.ljust + page_1.rjust(15))
print(chapter_2.ljust + page_2.rjust(15))
print(chapter_3.ljust + page_3.rjust(15))
temp = text.split("'")
print(temp)
temp2 = temp[0] + temp[1] + temp[2]
print(temp2)
number = int(temp2)
text = "12'345'678"
temp = text[:2] + text[3:6] + text[7]
number = int(temp)
print(temp)
temp = text.replace("'", "")
number = int(temp)
print(number)

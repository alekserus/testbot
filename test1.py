# Калькулятор
#
from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

what = input( "Что будем делать? (+,-, *): " )

print(Back.GREEN)
print(Fore.BLACK)

a = float ( input("Введи первое число: ") )

print(Back.CYAN)

b = float ( input("Введи Второе число: ") )

print(Back.YELLOW)

if what == "+":
	c = a + b
	print("Результат " + str(c))
elif what == "-":
	c = a - b
	print("Результат " + str(c))
elif what == "*":
	c = a * b
	print("Результат " + str(c))
else:
	print("Выбрана неверная оппереция!")


	


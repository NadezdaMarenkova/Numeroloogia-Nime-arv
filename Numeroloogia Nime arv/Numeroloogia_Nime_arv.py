from tkinter import *
from tkinter.messagebox import *
from functions import *

"""
Чтение текстовых файлов: 
letters.txt, numbers.txt, one.txt, ... nine.txt, 
в которых содержится информация, используемая в расчетах числа имени.
"""
letters = readFromFile("letters.txt")
numbers = readFromFile("numbers.txt")
one = readFromFile("one.txt")
two = readFromFile("two.txt")                                         
three = readFromFile("three.txt")
four = readFromFile("four.txt")
five = readFromFile("five.txt")
six = readFromFile("six.txt")
seven = readFromFile("seven.txt")
eight = readFromFile("eight.txt")
nine = readFromFile("nine.txt")

"""
Далее создаем главное окно программы, 
устанавливаем его свойства и задается фон.
"""
window = Tk()
window.title("Нумерология")
window.geometry("1700x1000+10+105") #(ширина окна, высота окна, x - на сколько в право открывать окно, y - на сколько вниз открывать окно )
window.resizable(width=False, height=False) #нельзя изменять размер окна
window.configure(bg="thistle") 


# Затем создаем виджеты (элементы интерфейса):

L0 = Label (window, height= 2, width = 10, bg = "thistle") # пустой лейбл для добавления отступа
l1 = Label (window, width = 40, text ="Хочешь узнать число своего имени? \nВведи имя: ", font = "Arial 20", fg = "black", bg="thistle") # лейбл с текстом
e = Entry (window, font = "Arial 30", fg = "black", bg = "khaki") # поле ввода для имени
b = Button (window, height= 2, width = 10, text ="Узнать!", font = "Arial 18", fg = "black", bg = "khaki", command = lambda:nameNamber(letters,numbers,e.get().lower(),l3)) 
# кнопка, при нажатии на которую происходит вызов функции nameNamber с передачей аргументов letters, numbers, e.get().lower(), l3;
l2 = Label (window, width = 30, text ="Число твоего имени: ", font = "Coral 20", fg = "black", bg="thistle")
l3 = Label (window, font = "Coral 12", bg = "thistle", fg = "black") # лейбл, куда будет выводиться результат расчета числа имени
l5 = Label (window, height= 1, width = 20, bg = "thistle")
l6 = Label (window, height= 1, width = 20, bg = "thistle")
l8 = Label (window, height= 1, width = 20, bg = "thistle")
l9 = Label (window, height= 1, width = 20, bg = "thistle")
l10 = Label (window, height= 1, width = 20, bg = "thistle")
l11 = Label (window, height= 1, width = 20, bg = "thistle")
l12 = Label (window, height= 1, width = 20, bg = "thistle")
l13 = Label (window, height= 1, width = 20, bg = "thistle")

"""
Далее происходят операции по позиционированию созданных элементов на окне 
с помощью метода grid, который позволяет задать расположение элементов в 
таблице с заданным числом строк и столбцов.
"""
L0.grid(row = 1, column = 1)
l1.grid(row = 2, column = 1)
e.grid(row = 4, column = 1)
b.grid(row = 6, column = 1)
l2.grid(row = 2, column = 2)
l3.grid(row = 7, column = 2)
l5.grid(row = 3, column = 1 )
l6.grid(row = 5, column = 1 )
l8.grid(row = 7, column = 1 )
l9.grid(row = 1, column = 2 )
l10.grid(row = 3, column = 2 )
l11.grid(row = 4, column = 2 )
l12.grid(row = 5, column = 2 )
l13.grid(row = 6, column = 2 )

"""
И, наконец, запускается бесконечный цикл обработки событий окна с помощью метода mainloop. 
Этот метод перехватывает все события, происходящие в окне (например, нажатия на кнопки) и 
передает их для обработки.
"""

window.mainloop()
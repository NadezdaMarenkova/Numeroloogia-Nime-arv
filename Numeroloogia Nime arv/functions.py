
# Функция readFromFile читает текст из файла и возвращает его в виде списка.

def readFromFile (file:str)->list:
    file = open (file, "r", encoding="UTF-8-sig")
    mas = [] 
    for line in file:
        mas.append(line.strip())
    file.close()
    return mas  

"""
 Функция nameNamber принимает в качестве аргументов список букв и 
 соответствующих им цифр, строку с именем и объект метки tkinter. 
"""


def nameNamber (l:list, n:list, name:str, lbl3):
    name = list (name) 
    numbersIndex = int() 

    """
    Вычисляем «число имени», складывая числа, связанные с каждой буквой в имени. 
    Если это число меньше 10, оно возвращается как есть. 
    Если оно больше или равно 10, цифры складываются, чтобы получить новое число, 
    и это число возвращается.
    """

    for i in name:                  
        lettersIndex = l.index(i)
        numbersIndex += int (n[lettersIndex])
    if numbersIndex <10:
        text = f"Твоё число имени - {numbersIndex}"
    elif numbersIndex >=10:
        first = numbersIndex//10
        second = numbersIndex%10
        numbersIndex = first + second 
        text = f"Твоё число имени - {numbersIndex}"
    if numbersIndex >=10:
        first = numbersIndex//10
        second = numbersIndex%10
        numbersIndex = first + second
        text = f"Твоё число имени - {numbersIndex}"
        """
        В зависимости от значения «nameNamber» функция открывает файл с соответствующим именем 
        (например, «one.txt» для числа 1) и считывает его содержимое. Затем содержимое 
        отображается в метке tkinter, переданной в качестве аргумента.
        """
    if numbersIndex == 1:
        file = open ("one.txt", 'r', encoding="UTF-8-sig")
        f = file.read()
    elif numbersIndex == 2:
        file = open ("two.txt", 'r', encoding="UTF-8-sig")
        f = file.read()
    elif numbersIndex == 3:
        file = open ("three.txt", 'r', encoding="UTF-8-sig")
        f = file.read() 
    elif numbersIndex == 4:
        file = open ("four.txt", 'r', encoding="UTF-8-sig")
        f = file.read()
    elif numbersIndex == 5:
        file = open ("five.txt", 'r', encoding="UTF-8-sig")
        f = file.read()
    elif numbersIndex == 6:
        file = open ("six.txt", 'r', encoding="UTF-8-sig")
        f = file.read()
    elif numbersIndex == 7:
        file = open ("seven.txt", 'r', encoding="UTF-8-sig")
        f = file.read()
    elif numbersIndex == 8:
        file = open ("eight.txt", 'r', encoding="UTF-8-sig")
        f = file.read()
    elif numbersIndex == 9:
        file = open ("nine.txt", 'r', encoding="UTF-8-sig")
        f = file.read()
    lbl3.configure(text = f)
    return numbersIndex   #Наконец, функция возвращает «номер имени».

    
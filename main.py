# Дано текстовий файл. Файл вміщює резульати вимірювань у форматі HH:MM XXX ,
# де HH:MM - час (H - години, M - хвилини), XXX - значення параменту (результат вимірювання).
# Користувач вводить певне значення AAA. Програма виводить всі значення часу,
# при яких результати вимірювання XXX перевищює введене користувачем значення AAA.
import os

class TimeStamp:
     def __init__(self, _time,_resault):
        self.time = _time
        self.resault = _resault


path = "input.txt"
# Дано текстовий файл. Файл вміщює резульати вимірювань у форматі HH:MM XXX ,
# де HH:MM - час (H - години, M - хвилини), XXX - значення параменту (результат вимірювання).

def main():
    text=read()
    dataBase=convert(text)
    aaa="not Numeric"
    while not aaa.isnumeric():
        aaa=input("Введіть ціле числове значення AAA: ") # Користувач вводить певне значення AAA.
    aaa=int(aaa)
    check_and_print(dataBase,aaa)

def read():
    file=open(path, "r")
    text=file.readlines()
    return text

def convert(text):
    dataBase=[]
    for line in text:
        splited = str.split(line," ")
        dataStamp=TimeStamp(splited[0],int(splited[1]))
        dataBase.append(dataStamp)
    return dataBase

def check_and_print(dataBase,aaa):
    for data in dataBase:        #Програма виводить всі значення часу,
        if data.resault>aaa:     #при яких результати вимірювання XXX перевищює введене користувачем значення AAA.
            print(data.time) 

if __name__ == '__main__':
    main()
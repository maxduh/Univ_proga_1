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
    dataBase=check_database(dataBase,aaa)
    print_database(dataBase)

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

def check_database(dataBase,aaa):
    dataBase_new=[]
    for data in dataBase:       
        if data.resault>aaa:     #при яких результати вимірювання XXX перевищює введене користувачем значення AAA.
            dataBase_new.append(data.time)
    return dataBase_new

def print_database(dataBase):
    for data in dataBase:        #Програма виводить всі значення часу
        print(data)  

if __name__ == '__main__':
    main()
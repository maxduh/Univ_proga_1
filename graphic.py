import PySimpleGUI as sg
import main as main_code



def main():
    sg.theme('DarkAmber')

    layout = [  [sg.Listbox("",size=(40,10),key="-Listbox-")],
                [sg.Text('Введіть ціле числове значення AAA: ')],
                [sg.Input(key='-INPUT-',size=(40,1),)],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    window = sg.Window('Window Title', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break

        input_value=values["-INPUT-"]
        if(input_value.isnumeric()):
            text=main_code.read()
            dataBase=main_code.convert(text)
            input_value=int(input_value)
            dataBase=main_code.check_database(dataBase,input_value)
            window['-Listbox-'].update(dataBase)
        else:
            sg.popup("Введіть ціле числове значення", keep_on_top=True)

    window.close()


if __name__=="__main__":
    main()

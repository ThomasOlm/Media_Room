import PySimpleGUI
import random

PySimpleGUI.theme('DarkBlue')   # Add a touch of color

messages = []
users    = []
current_user = ("bob", "john", "jeb")


layout = [  [PySimpleGUI.Output(size=(75,10), key='-OUTPUT-')],
            [PySimpleGUI.Text('Enter song to play'), PySimpleGUI.InputText()],
            [PySimpleGUI.Button('Ok'), PySimpleGUI.Button('Cancel')] ]


def main():
    window = PySimpleGUI.Window("Cool guys media room", layout).Finalize()

    while True:
        event, values = window.read()

        if event == PySimpleGUI.WINDOW_CLOSED or event == 'Cancel':
            break

        messages.append(values[0])
        users.append(random.choice(current_user))

        print(users[-1]+ ":")
        print(messages[-1])

        if len(users) > 10:
            window.FindElement('-OUTPUT-').Update('')
            users.clear()
            messages.clear()


    window.close()

main()
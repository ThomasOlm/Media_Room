import PySimpleGUI
import random
import subprocess


PySimpleGUI.theme('DarkBlue')   # Add a touch of color

messages = []
users    = []
current_user = ("bob", "john", "jeb")
current_song = "Current Song is: Roxane"

layout = [  [PySimpleGUI.Output(size=(75,10), key='-OUTPUT-')],
            [PySimpleGUI.Text(current_song, key='-SONG-')],
            [PySimpleGUI.Text('Enter song to play'), PySimpleGUI.InputText()],
            [PySimpleGUI.Button('Ok'), PySimpleGUI.Button('Cancel')]]


# this code will run on the raspberry pi
# this func should take in a string of a song and return a youtube link for the first video matching that string
def youtube_search(song_name):
    try:
        command = ['youtube-dl', 'ytsearch:"' + song_name + '"', '-g']
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                universal_newlines=True).stdout.split()
        print(result)
    except BaseException as E:
        print(E)

# this func should take in a string of a song and return a playing audio file
def handle_audio_call(song,window):
    current_song = "Current Song:" + song
    window.FindElement('-SONG-').Update(current_song)
    youtube_search(song)

# once program is fleshed out, this will be where the GUI connects to the socket
def send_audio_call(song):
    pass

def main():

    window = PySimpleGUI.Window("Cool guys media room", layout).Finalize()

    while True:
        event, values = window.read()

        if event == PySimpleGUI.WINDOW_CLOSED or event == 'Cancel':
            break

        messages.append(values[0])
        users.append(random.choice(current_user))

        ## make sure that each message is only starting a new line if a new user
        if len(users) >= 2:
            if users[-1] == users[-2]:
                print(messages[-1])
            else:
                print(users[-1] + ":")
                print(messages[-1])
        else:
            print(users[-1]+ ":")
            print(messages[-1])

        # check to see if the string starts with play, and if so call the string -> audio func
        if messages[-1].startswith("-play"):
            song = messages[-1][5:]
            handle_audio_call(song, window)


        ## clear the screen
        if len(users) > 10:
            window.FindElement('-OUTPUT-').Update('')
            users.clear()
            messages.clear()


    window.close()

main()
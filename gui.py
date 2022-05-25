
import PySimpleGUI as sg
import converter
import threading

def run_converter():
    filepath = values['-FILE-']
    window['-STATUS-'].update("Processing")
    window.refresh()
    cc = converter.main(filepath)
    if cc == 1:
        window['-STATUS-'].update("Error")
        window['-WROTE-'].update(visible=False)
        window['-PATH-'].update(visible=False)
    else:
        window['-STATUS-'].update("Complete")
        window['-WROTE-'].update(visible=True)
        window['-PATH-'].update(cc, visible=True)


layout = [
    [sg.T("")],
    [sg.Text("Choose a file: "), sg.Input(key='-FILE-'), sg.FileBrowse(), sg.Button("Convert", key='-CONVERT-')],
    [sg.Text('Status: '), sg.Text("Waiting for file", key='-STATUS-')],
    [sg.Text("Wrote to File: ", visible=False, key='-WROTE-'), sg.Text("", visible=False, key='-PATH-')]
]

window = sg.Window("Demo", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-CONVERT-':
        threading.Thread(target=run_converter).start()


window.close()

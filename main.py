import PySimpleGUI as sg
import os
import shutil

def _change_hud(hudname,skin_path):
        shutil.copytree(f"hud/{hudname}",skin_path,dirs_exist_ok=True)
        print(f"Skin files:{skin_path}")

def _main_window():
    sg.theme('DarkPurple4')
    skinlist = sg.Listbox(skin_list, size=(30, 1), font=('Arial Bold', 10), expand_y=True, enable_events=True, key='-SKIN-LIST-')
    hudlist = sg.Listbox(os.listdir("hud/"), size=(30, 1), font=('Arial Bold', 10), expand_y=True, enable_events=True, key='-HUD-LIST-')
    layout = [[skinlist],
        [sg.Button('Change', key="change")],[hudlist]]

    window = sg.Window('', layout, size=(600, 400))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "change":
            skin_path = skinlist.get()
            hud_path = hudlist.get()
            skin_path_change = f"{skin_list_path}/{skin_path[0]}"
            _change_hud(hud_path[0], skin_path_change)
    window.close()

def _start_window():
    global skin_list, skin_list_path

    sg.theme('DarkPurple4')
    layout = [[sg.Text('Путь к папке OSU'), sg.Input(), sg.FolderBrowse(key="-IN-"), sg.Button('Ok', key="main_window")]]
    window = sg.Window('Skin Editor', layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "main_window":
            skin_list_path = values[0]
            skin_list = os.listdir(values[0])
            _main_window()
    window.close()
    return skin_list_path, skin_list

if __name__ == "__main__":
    _start_window()
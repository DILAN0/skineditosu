import PySimpleGUI as sg
import os,zipfile,pathlib
import shutil

def _creat_skin(hudname, skin_path):
    try:
        os.mkdir("temp")
    except FileExistsError:
        shutil.rmtree("temp")
        os.mkdir("temp")
    shutil.copytree(skin_path, "temp", dirs_exist_ok=True)
    shutil.copytree(f"hud/{hudname}", "temp", dirs_exist_ok=True)
    directory = pathlib.Path("temp/")
    with zipfile.ZipFile(f'{skin_path}+{hudname}.osk', mode='w',
                         compression=zipfile.ZIP_DEFLATED) as zf:
        for file in directory.iterdir():
            zf.write(file, arcname=file.name)
    os.startfile(f"{skin_path}+{hudname}.osk")

def _change_hud(hudname,skin_path):

    shutil.copytree(f"hud/{hudname}",skin_path,dirs_exist_ok=True)
    print(f"Skin files:{skin_path}")

def _main_window():
    sg.theme('DarkPurple4')
    skinlist = sg.Listbox(skin_list, size=(30, 1), font=('Arial Bold', 10), expand_y=True, enable_events=True, key='-SKIN-LIST-')
    hudlist = sg.Listbox(os.listdir("hud/"), size=(30, 1), font=('Arial Bold', 10), expand_y=True, enable_events=True, key='-HUD-LIST-')
    layout = [[skinlist],[hudlist]
        ,[sg.Button('Change', key="change")], [sg.Button('Create', key="create")]]

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
        if event == "create":
            skin_path = skinlist.get()
            hud_path = hudlist.get()
            skin_path_change = f"{skin_list_path}/{skin_path[0]}"
            _creat_skin(hud_path[0], skin_path_change)
    window.close()

def _start_window():
    global skin_list, skin_list_path

    sg.theme('DarkPurple4')
    layout = [[sg.Text('Путь к папке OSU'), sg.Input(), sg.FolderBrowse(key="-IN-"), sg.Button('Ok', key="main_window")]]
    window = sg.Window('Skin Editor', layout)
    while True:
        event, values = window.read()
        if event == "main_window":
            skin_list_path = values[0]
            skin_list = os.listdir(values[0])
            _main_window()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()
    return skin_list_path, skin_list

if __name__ == "__main__":
    _start_window()
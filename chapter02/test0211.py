import PySimpleGUI as sg

sg.theme("DarkBrown3")

layout = [
    [sg.T("テキスト")],
    [sg.I("入力欄")],
    [sg.ML("複数行テキスト １行目\n２行目", size=(30, 3))],
    [sg.Im("./chapter02/futaba.png")],
]
win = sg.Window("入力欄テスト", layout, font=(None, 14), size=(400, 300))

e, v = win.read()
win.close()
